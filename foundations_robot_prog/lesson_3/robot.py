import commands2
import phoenix5
import wpilib

from subsystems.drivetrain import WestCoastDrivetrain


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

        # Xbox controller interface
        self.driver_controller = wpilib.XboxController(0)

        # ***
        # FOR YOU (3.5): 

        # <your code here>

        # ***

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
        Kick off default robot operation interfaces
        """
        pass

    def teleopPeriodic(self):
        """
        This code executes on every internal clock tick while the robot is in its
        teleoperated state. You can think of this as a time-spaced "while" loop that
        keeps running until the robot exists the teleoperated state.

        The "periodic" teleoperated method is often used perform specific manuevers
        with the drivetrain and/or to actuate our mechanisms.
        """
        # ***
        # FOR YOU (3.6)

        # <your code here>

        # ***

        # Delete the "pass" below once you've written some code
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
