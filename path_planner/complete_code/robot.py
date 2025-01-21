# Internal imports
from commands.default_swerve_drive import DefaultDrive
from subsystems.drivetrain.drivetrain import SwerveDrivetrain

from commands.shortyIntake import Intake
from subsystems.sparkyIntake import SparkyIntake
from subsystems.sparkyIntakePivot import IntakePivot
from subsystems.sparkyIntakePivotController import pivotController

# Third-party imports
import commands2
import wpilib
import wpimath
from commands2.button import Trigger
from pathplannerlib.path import PathPlannerPath
from pathplannerlib.auto import AutoBuilder, PathPlannerAuto


class PathPlannerRobot(commands2.TimedCommandRobot):
    def __init__(self) -> None:
        super().__init__(period=50 / 1000)

    def robotInit(self):
        self.drivetrain = SwerveDrivetrain()
        self.driver_controller = wpilib.XboxController(0)
        self.mechController = wpilib.XboxController(1)
        self.auto_chooser = AutoBuilder.buildAutoChooser()
        wpilib.SmartDashboard.putData("Select auto routine", self.auto_chooser)

        Trigger(self.isDisabled).debounce(3).onTrue(
            commands2.cmd.runOnce(
                self.drivetrain.set_motor_stop_modes(to_drive=False, to_break=False, all_motor_override=True),
                self.drivetrain
            )
        )
        self.intake = SparkyIntake()
        self.pivot = IntakePivot()
        self.intakePivotController = pivotController()
        self.intakePivotController.setIntakeRotationSubsystem(self.pivot)

    def robotPeriodic(self):
        commands2.CommandScheduler.getInstance().run()

    def disabledInit(self):
        self.drivetrain.stop_driving()
        self.drivetrain.reset_pose_estimator()

    def disabledPeriodic(self):
        pass

    def autonomousInit(self):
        self.drivetrain.set_motor_stop_modes(to_drive=True, to_break=True, all_motor_override=True)
        #path = PathPlannerPath.fromPathFile("3_angular_only")
        #self.drivetrain.setDefaultCommand(AutoBuilder.followPath(path))
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
        self.intake.setDefaultCommand(Intake(
            self.intake,
            self.intakePivotController,
            lambda: wpimath.applyDeadband(self.mechController.getLeftTriggerAxis(), 0.05),
            lambda: self.mechController.getRightBumper(),
            lambda: self.mechController.getAButtonPressed(),
        ))

    def teleopPeriodic(self):
        pass

    def testInit(self):
        pass

    def testPeriodic(self):
        pass
