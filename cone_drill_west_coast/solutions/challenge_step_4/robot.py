import commands2
import phoenix5
import wpilib

from commands.autonomous_routines import (
    rescale_motor_output,
    drive_straight_routine
)
from commands.tank_drive import TankDrive
from subsystems.drivetrain import WestCoastDrivetrain

# ***
# FOR YOU: once you've completed blocks 2 and/or 3 in
# commands/autonomous_routines.py, import your routine functions here.
# The code will be analogous to the following:

# from folder.file_name_no_extention import (function1, function2)

from commands.autonomous_routines import (
    drive_donut_routine,
    combined_drive_routine
)

# ***


class WestCoastRobot(commands2.TimedCommandRobot):
    """
    Robot with West Coast drivetrain subsystem. Uses differential drive for
    mobility. 
    """
    def robotInit(self):
        """
        Robot initializer - sets up drivetrain subsystem and component motors
        """
        # Easy access to TimedCommandRobot functionality
        super().__init__()

        # Four drive motors instantiated with the appropriate ports
        right_front_motor = phoenix5.WPI_TalonFX(31)
        right_back_motor = phoenix5.WPI_TalonFX(30)
        left_front_motor = phoenix5.WPI_TalonFX(21)
        left_back_motor = phoenix5.WPI_TalonFX(20)

        # Motors on each side of the robot collected to provide common instructions
        self.left_drive_motors = wpilib.MotorControllerGroup(left_front_motor, left_back_motor)
        self.right_drive_motors = wpilib.MotorControllerGroup(right_front_motor, right_back_motor)

        # Xbox controller interface with command framework functionality
        self.driver_controller = commands2.button.CommandXboxController(0)

        # West Coast Drivetrain subsystem
        self.drivetrain = WestCoastDrivetrain(self.left_drive_motors, self.right_drive_motors)

    def disabledInit(self):
        """
        Beginning setup and one-time component shutdown upon entering 
        the disabled state
        """
        pass

    def disabledPeriodic(self):
        """
        Continual robot shutdown procedures
        """
        pass

    def autonomousInit(self):
        """
        Autonomous routine initialization
        """
        # ***
        # FOR YOU (4.3)

        self.drivetrain.setDeadband(0)

        # ***

        # ***
        # FOR YOU (4.5)

        speed = rescale_motor_output(0.25, 0.04, 1)

        # ***

        # ***
        # FOR YOU (4.6, 4.8, 4.10)

        if False:
            drive_straight_routine(self.drivetrain, speed).schedule()
            drive_donut_routine(self.drivetrain, speed).schedule()
        combined_drive_routine(self.drivetrain, speed).schedule()

        # ***


    def autonomousPeriodic(self):
        """
        Autonomous routine execution
        """
        pass

    def teleopInit(self):
        """
        Set up operations for the teleoperated period
        """
        # We want driving to be smooth, so we set the drivetrain deadband back
        # to its default value
        self.drivetrain.setDeadband(0.02)

        # We set up a manual tank drive so we can reposition the robot easily
        self.drivetrain.setDefaultCommand(
            TankDrive(
                lambda: self.driver_controller.getLeftY(),
                lambda: self.driver_controller.getRightY(),
                self.drivetrain
            )
        )

    def teleopPeriodic(self):
        """
        Run driver operations on every clock tick
        """
        pass

    def testInit(self):
        """
        Debug code
        """
        pass

    def testPeriodic(self):
        """
        Debug code
        """
        pass


if __name__ == "__main__":
    wpilib.run(WestCoastRobot)
