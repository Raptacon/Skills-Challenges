import commands2
import phoenix5
import wpilib

from subsystems.drivetrain import WestCoastDrivetrain

####################################################################################
# Welcome to Lesson 3! Now that we've moved one side of the drivetrain by using
# the motors, let's expand upon this and actuate the other side of the drivetrain.
# By having control of both sides, we'll be able to drive the robot!

# We can now start to think about the whole drivetrain as a subsystem. Subsystems
# are an integrated set of components that work together to provide a focused
# range of functionality. For example, an arm subsystem may consist of three motors:
# one to raise the arm, one to extend it, and another to run a piece grabber.
# Drivetrain subsystems are typically comprised of the drive motors and sensors
# that track the distance driven and the heading (direction) of the robot. 

# If you look at the package imports above, you'll notice that we import our own
# drivetrain class from our own subsystems folder. It is generally advised to
# organize Python code that either provides similar functionality or operates
# temporally in a common part of the program's overall control flow in
# the same folders/modules. Part of this lesson will require you to write code
# within the WestCoastDrivetrain class.

# Look for "FOR YOU" within the code - this signals that you have something to do 
####################################################################################


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
        # FOR YOU: we're going to instantiate the drivetrain using our custom class.
        # If you have not finished coding up WestCoastDrivetrain, please open
        # the /subsystems/drivetrain.py file, follow the instructions, and come back.

        # Here, we'll create a drivetrain instance attribute within our robot - 
        # we want to be able to use the drivetrain object in the robot methods below
        # while ensuring that data associated with the drivetrain is maintained.
        # To do this, set an instance attribute to be a constructed WestCoastDrivetrain
        # object, passing the two motor groups for the two sides of the robot as
        # arguments to the constructor. This will be analogous to the following:
        # self.subsystem = Subsystem(self.some_motors, self.other_motors)

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
        # FOR YOU: last lesson we used one joystick to operate one side of the robot -
        # now, we'll use the other joystick to operate the other side of the robot too.
        # As part of the drivetrain class, you created a tankDrive method (see 
        # /subsystem/drivetrain.py for more details or to write that code if you haven't
        # already). We're going to pass the up/down values of each of the joysticks
        # as arguments to the tankDrive method. Remember - pressing all the way up
        # on a joystick gives a Y value of -1, while pressing all the way down gives
        # a Y value of 1.

        # You'll need three methods to operate the robot using tank drive:

        # <your_drivetrain_attribute>.tankDrive(): passes motor voltage percentage
        # values (1 = 100%, -1 = 100% in opposite direction) to each side of the
        # robot directly in order to drive. The code here will be analagous to the
        # following:
        # self.subsystem.operate(leftInput, rightInput)

        # <your_controller_attribute>.getLeftY(): retrieves how far the left joystick
        # has been pressed up/down as a numeric value between -1 and 1. The code
        # will be analagous to the following:
        # self.device.getJoystickVerticalPercentage()

        # <your_controller_attribute>.getRightY(): same as getLeftY() but for the right
        # joystick

        # Call the drivetrain's tankDrive method, passing it the left and right
        # joystick Y values

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
