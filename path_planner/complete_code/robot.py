import commands2
import wpilib
import wpimath

from commands.default_swerve_drive import DefaultDrive
from subsystems.drivetrain.drivetrain import SwerveDrivetrain


class PathPlannerRobot(commands2.TimedCommandRobot):
    def __init__(self) -> None:
        super().__init__(period=50 / 1000)

    def robotInit(self):
        self.drivetrain = SwerveDrivetrain()
        self.driver_controller = wpilib.XboxController(0)

    def robotPeriodic(self):
        commands2.CommandScheduler.getInstance().run()
        #self.drivetrain.update_pose_estimator()

    def disabledInit(self):
        self.drivetrain.stop_driving()

    def disabledPeriodic(self):
        pass

    def autonomousInit(self):
        pass

    def autonomousPeriodic(self):
        pass

    def teleopInit(self):
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
        pass

    def testInit(self):
        pass

    def testPeriodic(self):
        pass
