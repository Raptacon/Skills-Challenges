import commands2
import phoenix5
import wpilib

####################################################################################
# Welcome to Lesson 2! In this lesson, we're going to get started with robot code.

# To program an FRC robot, we'll be making extensive use of the WPILib Python
# package. Packages are blocks of Python code that we can install on our system
# and use as part of our software. Python has a massive open source community
# that makes and supports tons of freely available and easily installable packages.
# WPILib, provided via a broader package called RobotPy, is one such package.
# You can find documentation on RobotPy at
# https://robotpy.readthedocs.io/en/stable/index.html

# Python software that uses WPILib starts with a robot.py file. Here, we write
# a class that represents our robot virtually and exposes functionality that
# will be directly used to operate the robot. If you are familiar with the concept
# of a "main" file, robot.py will be our equivalent of that.

# We've taken care of much of the boilerplate for setting up the class. This way,
# you can focus on writing logic for operating the robot. That said, we encourage
# you to read through the docstrings and comments explaining what each part is
# doing. We'll be working on other parts of the class in future lessons.

# Look for "FOR YOU" within the class - this signals that you have something to do 
####################################################################################


class WestCoastRobot(commands2.TimedCommandRobot):
    """
    We've created a "WestCoastRobot" class to express all of our robot code to
    WPILib. This class has a number of different methods, each representing
    different phases of booting up the robot and progressing through match gameplay.

    WPILib strongly follows object-oriented programming principles, and one such
    principle we see here is inheritance. "Inheritance" is when one class brings
    in the data attributes and methods of another. For example, if we make a
    class to represent a mammal and say that a mammal is warm-blooded, then when
    we make a class to represent a dog and inherit from the mammal class,
    the dog will also be warm blooded.

    Here, our robot class inherits from a generic timed robot class that we
    brought in from the commands2 part of the RobotPy ecosystem. Any robot
    built off of this timed robot class will execute code based on an internal
    clock that ticks on a fixed interval. We'll explore this more later when we
    start looking at autonomous routines.
    """
    def robotInit(self):
        """
        The code in robotInit is executed as soon as the robot is powered on or
        when new code is deployed. It is typically used to set up virtual
        representations of physical aspects of the robot, like motors, drivetrains,
        sensors, and much more!

        When creating instance attributes, we'll use self.<attribute_name>
        syntax. This lets us create data elements within a specific object.
        """
        # This lets us cleanly refer to the functionality in the timed robot class
        super().__init__()

        # ***
        # FOR YOU: in Lesson 2, we'll focus on operating one side of a West Coast
        # drivetrain. As you saw when we looked over the robot, we have two motors
        # actuating the gears a given side - this gives our robot more power. It
        # also means we can effectively treat the two motors as one motor.
        # So, we'll start by representing our drive motors virtually.

        # To do this, you'll need two classes:

        # phoenix5.WPI_TalonFX: this class represents one Talon motor on the robot.
        # It takes a CAN bus port as an argument for its constructor, telling the
        # robot where on the CAN network it should send instructions for operating
        # the motor. Look at the motors to see what ports we should use.

        # wpilib.MotorControllerGroup: this collects multiple motors together and
        # forwards the instructions it receives to all of those motors. We want the
        # drive motors on the same side to operate exactly the same. The constructor
        # takes an arbitrary number of motors as arguments.

        # Create two motors using the correct ports, and collect them with a motor
        # controller group. The motor controller group must be an instance attribute
        # by using self.<name> = <value> syntax.

        # <your code here>

        # ***

        # ***
        # FOR YOU: we need to set up some method of manually operating our
        # motors. Here we'll create an XboxController and later we'll use
        # one of its joysticks.

        # Here, you'll need the wpilib.XboxController class. It represents an
        # Xbox controller as an input device to the robot. It takes one argument -
        # a port number telling the driver station which input device to reference
        # for receiving instructions.

        # Create an instance attribute set to a created XboxController object.
        # Give the controller port 0.

        # <your code here>

        # ***

    def disabledInit(self):
        """
        This code executes immediately when the robot is switched into its disabled
        state. When the robot is disabled, it should stop functioning and do
        nothing. This state is often used to ensure safety.
        """
        # "pass" is a Python keyword saying that we are doing nothing in this method
        pass

    def disabledPeriodic(self):
        """
        This code executes on every internal clock tick while the robot is in its
        disabled state. You can think of this as a time-spaced "while" loop that
        keeps running until the robot exists the disabled state. 
        """
        pass

    def autonomousInit(self):
        """
        This code executes immediately when the robot is switched into its autonomous
        state. When the robot is autonomous, it operates with absolutely zero human
        input. FRC matches often start with a 15-second autonomous period.

        The "init" autonomous method is often used to set up the starting positional
        parameters of the robot and provide a standard set of instructions.
        """
        pass

    def autonomousPeriodic(self):
        """
        This code executes on every internal clock tick while the robot is in its
        autonomous state. You can think of this as a time-spaced "while" loop that
        keeps running until the robot exists the autonomous state.

        The "periodic" autonomous method is often used to perform a sequence of
        specific operations as the robot progresses through its autonomous routine.
        """
        pass

    def teleopInit(self):
        """
        This code executes immediately when the robot is switched into its
        teleoperated state. When the robot is teleoperated, it operates according
        to explicit instructions given by a human driver. FRC matches often have
        a 2 minute and 15 second teleoperated period.

        The "init" teleoperated method is often used to provide a standard
        instruction interface for a select choice of robot mechanisms.
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
        # FOR YOU: we have our physical devices represented virtually, now we
        # need to use them! We're going to actuate one side of our drivetrain
        # by pressing up and down on a joystick.

        # We control a motor programmatically by giving the motor a percentage
        # of its maximum voltage, as well as a direction in the form of a sign (+/-).
        # At maximum voltage, the motor goes at full speed; at 50% of the max
        # voltage, it goes at half speed. Percentages are given using a float
        # between -1 and 1, with 1 being 100% and -1 being 100% in the opposite
        # direction.

        # For our joystick input, you only need to know two things for now (we'll
        # focus heavily on driver controllers later on):
        # -> the .getLeft* methods access the left joytick, .getRight* the right
        # -> pushing all the way up on a joystick gives a Y value of -1, pushing
        #    all the way down a Y value of 1, keeping in the middle a value of 0

        # You'll need two methods that will be called from our instance attributes:

        # wpilib.MotorControllerGroup().set(): tells the robot what percentage
        # of maximum voltage to give to each motor in the collection. Takes one
        # argument with a value between -1 and 1

        # wpilib.XboxController().getLeftY(): retrieves how far the left joystick
        # has been pressed up/down as a numeric value between -1 and 1, as
        # described above

        # Using your motor group instance attribute and Xbox controller instance
        # attribute, set the speed and direction of the motors using the up/down
        # (Y) value of the left joystick on the controller.

        # <your code here>

        # Delete the "pass" when you have some code written above
        pass

        # ***

    def testInit(self):
        """
        The test state is used to debug a specific block of code. We use this
        to try out some new code that we've written while avoiding conflicts
        with the existing code in the other state methods.
        """
        pass

    def testPeriodic(self):
        """
        The test state is used to debug a specific block of code. We use this
        to try out some new code that we've written while avoiding conflicts
        with the existing code in the other state methods.
        """
        pass


# This is fancy Python syntax telling the interpreter to run the indented code block
# when executing this script.

# If you're familiar with the "main" file in Java, this code effectively makes
# this .py script the "main" file of our program
if __name__ == "__main__":
    # WPILib will operate the robot according to the logic we defined in our class
    wpilib.run(WestCoastRobot)
