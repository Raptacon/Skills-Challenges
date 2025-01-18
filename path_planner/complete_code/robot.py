# Internal imports
from commands.default_swerve_drive import DefaultDrive
from subsystems.drivetrain.drivetrain import SwerveDrivetrain

# Third-party imports
import commands2
import wpilib
import wpimath
from pathplannerlib.path import PathPlannerPath
from pathplannerlib.auto import AutoBuilder, PathPlannerAuto


class PathPlannerRobot(commands2.TimedCommandRobot):
    def __init__(self) -> None:
        super().__init__(period=50 / 1000)

    def robotInit(self):
        self.drivetrain = SwerveDrivetrain()
        self.driver_controller = wpilib.XboxController(0)

    def robotPeriodic(self):
        commands2.CommandScheduler.getInstance().run()

    def disabledInit(self):
        self.drivetrain.stop_driving()
        self.drivetrain.reset_pose_estimator()

    def disabledPeriodic(self):
        pass

    def autonomousInit(self):
        path = PathPlannerPath.fromPathFile("3_angular_only")
        self.drivetrain.setDefaultCommand(AutoBuilder.followPath(path))
        #self.drivetrain.setDefaultCommand(PathPlannerAuto('test_auto'))

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
