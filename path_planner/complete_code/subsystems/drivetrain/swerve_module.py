# Native imports
import math
import logging as log
from typing import Tuple

# Internal imports
from config import RobotConfig
from constants import SwerveModuleMk4iConsts, SwerveModuleMk4iL2Consts
from sensors.utils import configureSparkMaxCanRates

# Third-party imports
import ntcore
import phoenix6
import rev
from wpimath.kinematics import SwerveModulePosition, SwerveModuleState
from wpimath.geometry import Rotation2d, Translation2d

"""
This is a basic swerve drive module for a robot running
https://www.swervedrivespecialties.com/products/mk4-swerve-module
with L1 standard and 2 falcon 500
https://store.ctr-electronics.com/falcon-500-powered-by-talon-fx/
and a
https://store.ctr-electronics.com/cancoder/
Other defaults may be added in future

Constants used from https://github.com/SwerveDriveSpecialties/swerve-lib/tree/develop/src
"""


class SwerveModuleMk4iSparkMaxFalconCanCoder:
    """
    Module for Mk4i with 2 brushless Falcon 500s and a CANcoder swerve drive
    """
    def __init__(
        self,
        name: str,
        drivetrain_location: Tuple[float, float],
        channel_base: int,
        invert_drive: bool = False,
        invert_steer: bool = False,
        encoder_calibration: float = 0,
        swerve_level_constants: SwerveModuleMk4iConsts=SwerveModuleMk4iL2Consts()
    ) -> None:
        """
        Creates a new swerve module at location in robot.
        
        Channels are defined as:
            - channelBase = drive
            - channelBase + 1 = steer
            - channelBase + 2 = CANcoder

        Encoders are rotated by encoder_calibration.

        Drivetrain location specifies the x and y coordinates of the module relative to the center of the drivetrain.
        """
        # Overall instantiation
        self.constants = swerve_level_constants
        self.name = name
        self.drivetrain_location = Translation2d(*drivetrain_location)

        self.id_lookup = {
            "drive_motor": channel_base,
            "steer_motor": channel_base + 1,
            "absolute_encoder": channel_base + 2
        }

        # Physical device instantiation
        self.drive_motor = rev.SparkMax(self.id_lookup["drive_motor"] , rev.SparkLowLevel.MotorType.kBrushless)
        self.steer_motor = rev.SparkMax(self.id_lookup["steer_motor"], rev.SparkLowLevel.MotorType.kBrushless)
        self.absolute_encoder = phoenix6.hardware.CANcoder(self.id_lookup["absolute_encoder"])

        self.drive_motor_encoder = self.drive_motor.getEncoder()
        self.steer_motor_encoder = self.steer_motor.getEncoder()

        self.drive_motor_pid = self.drive_motor.getClosedLoopController()
        self.steer_motor_pid = self.steer_motor.getClosedLoopController()

        # Configuration setup
        drive_motor_config = rev.SparkMaxConfig()
        steer_motor_config = rev.SparkMaxConfig()

        absolute_encoder_configurator = phoenix6.configs.CANcoderConfigurator(self.id_lookup["absolute_encoder"])
        absolute_encoder_config = phoenix6.configs.CANcoderConfiguration()

        # Absolute encoder configuration
        absolute_encoder_configurator = phoenix6.configs.CANcoderConfigurator(self.id_lookup["absolute_encoder"])
        absolute_encoder_config = phoenix6.configs.CANcoderConfiguration()
        absolute_encoder_config.magnet_sensor.absolute_sensor_discontinuity_point = 1
        absolute_encoder_config.magnet_sensor.magnet_offset = encoder_calibration
        absolute_encoder_config.magnet_sensor.sensor_direction = 1

        status = absolute_encoder_configurator.apply(absolute_encoder_config, 0.25)
        if not status.is_ok():
            raise RuntimeError(
                f"Failed to configure CAN encoder on id {self.id_lookup['absolute_encoder']}. Error {status}"
            )

        status = self.absolute_encoder.get_position().set_update_frequency(self.constants.kCanStatusFrameHz, 0.25)
        if not status.is_ok():
            raise RuntimeError(
                f"Failed to configure CAN encoder on id {self.id_lookup['absolute_encoder']}. Error {status}"
            )

        # Steer motor configuration
        configureSparkMaxCanRates(steer_motor_config, drive_motor_flag=False)
        steer_motor_config.setIdleMode(rev.SparkBase.IdleMode.kCoast)

        (
            steer_motor_config.closedLoop
            .setFeedbackSensor(rev.ClosedLoopConfig.FeedbackSensor.kPrimaryEncoder)
            .pid(*RobotConfig.swerve_steer_pid)
            .positionWrappingEnabled(True)
            .positionWrappingInputRange(0, 360.0)
        )

        (
            steer_motor_config.encoder
            .quadratureMeasurementPeriod(self.constants.quadratureMeasurementRateMs)
            .quadratureAverageDepth(self.constants.quadratureAverageDepth)
            .positionConversionFactor(self.constants.steerPositionConversionFactor)
            .velocityConversionFactor(self.constants.steerVelocityConversionFactor)
        )

        self.steer_motor.configure(
            steer_motor_config, rev.SparkBase.ResetMode.kNoResetSafeParameters,
            rev.SparkBase.PersistMode.kPersistParameters
        )

        self.steer_motor.setInverted(invert_steer)

        # Drive motor configuration
        configureSparkMaxCanRates(drive_motor_config, drive_motor_flag=True)
        drive_motor_config.setIdleMode(rev.SparkBase.IdleMode.kBrake)

        (
            drive_motor_config.closedLoop
            .setFeedbackSensor(rev.ClosedLoopConfig.FeedbackSensor.kPrimaryEncoder)
            .pid(*RobotConfig.swerve_drive_pid)
        )

        (
            drive_motor_config.encoder
            .positionConversionFactor(self.constants.drivePositionConversionFactor)
            .velocityConversionFactor(self.constants.driveVelocityConversionFactor)
        )

        self.drive_motor.configure(
            drive_motor_config, rev.SparkBase.ResetMode.kNoResetSafeParameters,
            rev.SparkBase.PersistMode.kPersistParameters
        )

        self.drive_motor.setInverted(invert_drive)

        # Baseline relative encoders
        self.baseline_relative_encoders()

    def baseline_relative_encoders(self) -> None:
        """
        """
        self.drive_motor_encoder.setPosition(0)
        current_absolute_rotation = self.absolute_encoder.get_absolute_position(refresh=True)
        if not current_absolute_rotation.status.is_ok():
            raise RuntimeError("Failed to retrieve starting absolute encoder position baselining relative encoders")
        self.steer_motor_encoder.setPosition((current_absolute_rotation.value_as_double * 360.0) % (360.0))

    def current_position(self) -> SwerveModulePosition:
        """
        """
        drive_position = self.drive_motor_encoder.getPosition()
        steer_position = Rotation2d.fromDegrees(self.steer_motor_encoder.getPosition())
        return SwerveModulePosition(drive_position, steer_position)

    def set_state(self, state: SwerveModuleState) -> None:
        """
        """
        self.steer_motor_pid.setReference(state.angle.degrees, rev.SparkBase.ControlType.kPosition, 0)
        self.drive_motor_pid.setReference(state.speed, rev.SparkBase.ControlType.kVelocity, 0)
