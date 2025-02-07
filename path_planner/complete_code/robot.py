# Internal imports
from commands.default_swerve_drive import DefaultDrive
from subsystems.drivetrain.drivetrain import SwerveDrivetrain
from vision import Vision

# Third-party imports
import commands2
import wpilib
import wpimath
from commands2.button import Trigger
from pathplannerlib.path import PathPlannerPath
from pathplannerlib.auto import AutoBuilder, PathPlannerAuto
from wpilib import SmartDashboard

class PathPlannerRobot(commands2.TimedCommandRobot):
    def __init__(self) -> None:
        super().__init__(period=50 / 1000)

    def robotInit(self):
        self.drivetrain = SwerveDrivetrain()
        self.driver_controller = wpilib.XboxController(0)
        self.vision = Vision(self.drivetrain)

        Trigger(self.isDisabled).debounce(3).onTrue(
            commands2.cmd.runOnce(
                self.drivetrain.set_motor_stop_modes(to_drive=False, to_break=True, all_motor_override=True),
                self.drivetrain
            )
        )

    def robotPeriodic(self):
        commands2.CommandScheduler.getInstance().run()

    def disabledInit(self):
        self.drivetrain.stop_driving()
        self.drivetrain.reset_pose_estimator(self.drivetrain.current_pose())
        pass

    def disabledPeriodic(self):
        pass

    def autonomousInit(self):
        self.drivetrain.set_motor_stop_modes(to_drive=True, to_break=True, all_motor_override=True)
        path = PathPlannerPath.fromPathFile("3_angular_only")
        self.drivetrain.setDefaultCommand(AutoBuilder.followPath(path))

        self.drivetrain.setDefaultCommand(PathPlannerAuto('1M_1D_translation'))
        pass


        auto_routine = self.auto_chooser.getSelected()
        if auto_routine:
             auto_routine.schedule()

    def autonomousPeriodic(self):
        pass

    def teleopInit(self):
        self.drivetrain.set_motor_stop_modes(to_drive=True, to_break=True)
        self.drivetrain.set_motor_stop_modes(to_drive=False, to_break=False)
        self.drivetrain.setDefaultCommand(
            DefaultDrive(
                self.drivetrain,
                lambda: wpimath.applyDeadband(-1 * self.driver_controller.getLeftY(), 0.06),
                lambda: wpimath.applyDeadband(-1 * self.driver_controller.getLeftX(), 0.06),
                lambda: wpimath.applyDeadband(-1 * self.driver_controller.getRightX(), 0.1),
                False
            )
        )

    def teleopPeriodic(self):
        self.vision.getCamEstimate()
        bestTarget = self.vision.getBestTarget()
        if bestTarget == None:
            return
        targetID, yaw, pitch, skew, areaPercent = self.vision.getTargetData(bestTarget)
        SmartDashboard.putNumber(f"target id", targetID)
        SmartDashboard.putNumber(f"target yaw", yaw)
        SmartDashboard.putNumber(f"target pitch", pitch)
        SmartDashboard.putNumber(f"target skew", skew)
        SmartDashboard.putNumber(f"target area", areaPercent)



    def testInit(self):
        pass

    def testPeriodic(self):
        pass
