import commands2
import phoenix5
import wpilib

from commands.arcade_drive import ArcadeDrive
from subsystems.drivetrain import WestCoastDrivetrain

####################################################################################
# Welcome to Lesson 4! Now that you've built a subsytem, you're going to
# use it in more complicated ways through commands. Subystems define what is
# on the robot and a basic interface for using it. Commands define what action
# a subsystem should take for a given period of time. You should know that
# a subsystem can only be operated on by one command at at time.

# Additionally, we're going to expand our usage of the Xbox controller
# to use buttons. Buttons can be used by the driver to trigger specific
# commands. The button we'll use will allow us to switch from our
# starting drive system to a different one. We're going to introduce you to
# arcade drive before returning to tank drive. 

# Look for "FOR YOU" within the code - this signals that you have something to do 
####################################################################################

# ***
# FOR YOU: do not do this step until you've finished writing the tank drive class,
# then come back here.

# At this point, we have a tank drive class written, but we are currently not using
# it in our robot code. We need to import our custom class into this file, allowing
# us to use it in our robot class. This is similar to what we do with third-party
# libraries, except here we do it with our own code.

# Import your tank drive class from the tank drive file in the commands folder.
# The code will be analagous to the following:
# from folder.file import MyClass

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
        # FOR YOU: we're going to set the default command for the drivetrain to be
        # an instance of the ArcadeDrive command we wrote earlier. The speed
        # will be given using the vertical value of the left joystick, while the
        # turn rate will be given using the horizontal value of the right joystick.
        
        # To instantiate the command, we're going to make use of lambda functions.
        # A lambda function allows us to define a function without saving it
        # or giving it a name. Lambda functions can take any number of
        # arguments and return the result of the expression given when it gets
        # called. Lambdas are often used as arguments to other functions or
        # methods, allowing it to be called as often as needed within that
        # logic.

        # You'll need the following:
        # <drivetrain_instance_attribute>.setDefaultCommand(): sets the
        # default command for the subsystem the method is attached to.
        # Because our custom drivetrain subsystem inherits from SubsystemBase,
        # it has a setDefaultCommand method taken from the parent class.
        # .setDefaultCommand() takes one argument, an instantiated command
        # object.

        # ArcadeDrive(): custom command class that tells the robot executor to
        # use arcade drive to operate the drivetrain. Takes three arguments: a
        # callable function returning the speed percentage, a callable function
        # returning the turn rate percentage, and the drivetrain subsystem.

        # Set the default command of the drivetrain instance attribute to be
        # arcade drive, passing callable left Y joystick and right X joystick
        # values as the frist two arguments and the drivetrain instance attribute
        # as the third argument. Remember, the Y axis on a joystick is vertical and
        # the X axis is horizontal. The code will be analagous to the following:
        # self.subsystem.giveDefaultCommand(
        #   Command(
        #       lambda: self.input_device.getLeftVertical(),
        #       lambda: self.input_device.getRightHorizontal(),
        #       self.subsystem
        #   )
        #)

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
        # FOR YOU: now, we'll run the custom tank drive command class that you wrote
        # when the Y button is pressed on the controller. Buttons are considered
        # digital inputs, where a press results in a True Boolean while no press
        # results in a False Boolean for the button.

        # You'll need the following:
        # <driver_controller_instance_attribute>.y().onTrue(): calls the "y" method
        # on the Xbox controller to return a trigger for a new command. The trigger's
        # "onTrue" method specifies what command should be triggered when the
        # trigger state is set to True (in this case, when the Y button is returning
        # True). .onTruce() takes one argument, an instantiated command to run.

        # <your_custom_tank_drive_class>: custom command class that tells the robot
        # executor to use tank drive to operate the drivetrain. Takes three
        # arguments: a callable function returning the left voltage percentage, a
        # callable function returning the right voltage percentage, and the
        # drivetrain subsystem.

        # Run an instantiated TankDrive command when the Y button has been pressed
        # on the driver's controller. Pass callable left Y joystick and right Y
        # joystick values as the frist two arguments to TankDrive and the drivetrain
        # instance attribute as the third argument to TankDrive. The code will be
        # analagous to the following:
        # self.input_device.button().whenTrue(
        #   Command(
        #       lambda: self.input_device.getLeftVertical(),
        #       lambda: self.input_device.getRightVertical(),
        #       self.subsystem
        #   )
        #)

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
