import commands2
import phoenix5
import wpilib

from commands.tank_drive import TankDrive
from subsystems.drivetrain import WestCoastDrivetrain

####################################################################################
# Welcome to Lesson 6! You've learned all of the foundational material, and now
# it's time to let your ideas fly! You can think of your own autonomous actions to
# write, compose them into your own routine, and use that routine on the robot.

# There won't be a lot of structure to this lesson, as you are building
# your own code. We generally recommend that you write some action commands in
# the commands/autonomous_actions.py file, import them here and use them in
# the .autonomousInit() method below to test, write a composed routine
# in the commands/autonomous_routines.py file, then finally delete the use of action
# commands here and replace them with your routine functions.

# Be sure to sim test your code before deploying to the robot, and start by using
# slow speeds (0.25 motor percentage value or lower) to safely see how your
# routine looks on the robot.

# Look for "FOR YOU" within the code - this signals that you have something to do 
####################################################################################

from commands.autonomous_actions import (
    DiffDriveStraight,
    DiffDriveDonuts,

    # ***
    # FOR YOU: you will import your action commands here.
    # Add the names of any commands you want to bring in here, separated by commas

    # <your code here>

    # ***
)

from commands.autonomous_routines import (
    rescale_motor_output,
    drive_straight_routine,
    drive_donut_routine,
    combined_drive_routine,

    # ***
    # FOR YOU: you will import your routine functions here.
    # Add the names of any functions you want to bring in here, separated by commas

    # <your code here>

    # ***
)


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
        # Subsystem added deadband is set to 0
        self.drivetrain.setDeadband(0)

        # We're providing the rescaled speed percentage to make a motor operate
        # at 15% output. You can use this function, passing a second argument of 0.04
        # and a third argument of 1, to rescale other speeds you may want to use
        speed = rescale_motor_output(0.15, 0.04, 1)

        # ***
        # FOR YOU: you can instantiate and schedule any action commands and/or
        # routines here. An example of this from Lesson 5 would be:
        # combined_drive_routine(self.drivetrain, speed).schedule()

        # <your code here>

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
