import commands2
import phoenix5
import wpilib

from commands.arcade_drive import ArcadeDrive
from subsystems.drivetrain import WestCoastDrivetrain

# ***
# FOR YOU (4.6)

from commands.tank_drive import TankDrive

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
        pass

    def autonomousPeriodic(self):
        """
        Autonomous routine execution
        """
        pass

    def teleopInit(self):
        """
        The teleoperated initialization method is often used to set default commands.
        Default commands run on their required subsystems unless another command
        is running. If that new command stops, then the default command starts
        running again.

        Basic joystick control of the drivetrain is very frequently set as a default
        command within this teleopInit method, because we want the driver to always
        manually move the robot around the field unless the driver tells the robot
        to perform a specific maneuver.
        """
        # ***
        # FOR YOU (4.7)

        self.drivetrain.setDefaultCommand(
            ArcadeDrive(
                lambda: self.driver_controller.getLeftY(),
                lambda: self.driver_controller.getRightX(),
                self.drivetrain
            )
        )

        # ***

    def teleopPeriodic(self):
        """
        Like we've done before, we'll use the teleoperated periodic method to tell
        the robot what to do on every clock tick. In this case, we'll poll the
        Xbox controller for whether the Y button has been pressed on every tick.
        If the button has been pressed, we'll switch over to using tank drive to
        operate the robot.
        """
        # ***
        # FOR YOU (4.9)

        self.driver_controller.y().onTrue(
            TankDrive(
                lambda: self.driver_controller.getLeftY(),
                lambda: self.driver_controller.getRightY(),
                self.drivetrain
            )
        )

        # ***

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
