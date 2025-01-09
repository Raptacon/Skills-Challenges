# Native imports
from typing import Tuple

# Internal imports
from config import RobotConfig
from constants import SwerveDriveConsts
from .swerve_module import SwerveModuleMk4iSparkMaxFalconCanCoder

# Third-party imports
import navx
from commands2 import Subsystem
from wpimath.estimator import SwerveDrive4PoseEstimator
from wpimath.geometry import Pose2d, Rotation2d
from wpimath.kinematics import ChassisSpeeds, SwerveDrive4Kinematics, SwerveModulePosition


class SwerveDrivetrain(Subsystem):
    """
    """
    def __init__(self, starting_pose: Pose2d = Pose2d(*RobotConfig.default_start_pose)) -> None:
        """
        """
        self.constants = SwerveDriveConsts()

        # must do in front-left, front-right, back-left, back-right order
        self.swerve_modules = [
            SwerveModuleMk4iSparkMaxFalconCanCoder(
                "frontLeft", (self.constants.moduleFrontLeftX, self.constants.moduleFrontLeftY),
                RobotConfig.swerve_module_channels[0], encoder_calibration=RobotConfig.swerve_abs_encoder_calibrations[0]
            ),
            SwerveModuleMk4iSparkMaxFalconCanCoder(
                "frontRight", (self.constants.moduleFrontRightX, self.constants.moduleFrontRightY),
                RobotConfig.swerve_module_channels[1], encoder_calibration=RobotConfig.swerve_abs_encoder_calibrations[1]
            ),
            SwerveModuleMk4iSparkMaxFalconCanCoder(
                "backLeft", (self.constants.moduleBackLeftX, self.constants.moduleBackLeftY),
                RobotConfig.swerve_module_channels[2], encoder_calibration=RobotConfig.swerve_abs_encoder_calibrations[2]
            ),
            SwerveModuleMk4iSparkMaxFalconCanCoder(
                "backRight", (self.constants.moduleBackRightX, self.constants.moduleBackRightY),
                RobotConfig.swerve_module_channels[3], encoder_calibration=RobotConfig.swerve_abs_encoder_calibrations[3]
            )
        ]

        self.drive_kinematics = SwerveDrive4Kinematics(
            *[swerve_module.drivetrain_location for swerve_module in self.swerve_modules] # -> Translation2d()
        )

        self.gyroscope = navx.AHRS.create_spi()
        self.heading_offset = 0

        self.pose_estimator = SwerveDrive4PoseEstimator(
            self.drive_kinematics,
            self.current_heading(),
            self.current_module_positions(),
            starting_pose
        )

    def current_heading(self) -> Rotation2d:
        """
        """
        return Rotation2d.fromDegrees(self.gyroscope.getFusedHeading() - self.heading_offset)

    def reset_heading(self) -> Rotation2d:
        """
        """
        self.heading_offset = self.gyroscope.getFusedHeading()

    def drive(
        self,
        velocity_vector_x: float,
        velocity_vector_y: float,
        angular_velocity: float,
        field_relative: bool = False
    ) -> None:
        """
        """
        if field_relative:
            chassis_speeds = ChassisSpeeds.fromFieldRelativeSpeeds(
                velocity_vector_x, velocity_vector_y, angular_velocity, self.current_heading()
            )
        else:
            chassis_speeds = ChassisSpeeds(velocity_vector_x, velocity_vector_y, angular_velocity)

        module_states = self.drive_kinematics.toSwerveModuleStates(chassis_speeds)
        module_states = self.drive_kinematics.desaturateWheelSpeeds(module_states, self.constants.maxTranslationMPS)

        for i, module_state in enumerate(module_states):
            self.swerve_modules[i].set_state(module_state)

    def current_module_positions(self) -> Tuple[SwerveModulePosition]:
        """
        """
        return tuple([swerve_module.current_position() for swerve_module in self.swerve_modules])

    def current_pose(self) -> Pose2d:
        """
        """
        return self.pose_estimator.getEstimatedPosition()

    def update_pose_estimator(self) -> None:
        """
        """
        self.pose_estimator.update(self.current_heading(), self.current_module_positions())
        for swerve_module in self.swerve_modules:
            swerve_module.update_telemetry()

    def reset_pose_estimator(self, current_pose: Pose2d = Pose2d(*RobotConfig.default_start_pose)) -> None:
        """
        """
        self.pose_estimator.resetPosition(self.current_heading(), self.current_module_positions(), current_pose)

    def periodic(self) -> None:
        """
        """
        self.update_pose_estimator()
