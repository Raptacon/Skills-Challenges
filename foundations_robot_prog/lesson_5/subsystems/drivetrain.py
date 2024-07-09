import commands2
import wpilib
import wpilib.drive


class WestCoastDrivetrain(commands2.SubsystemBase):
    def __init__(self, left_motors, right_motors):
        """
        Set up the drivetrain with two collections of motors, one for each side
        of the robot, and pass them into a differential drive interface.

        Args:
            left_motors: motor controller group containing motors for the left
                side of the drivetrain
            right_motors: motor controller group containing motors for the right
                side of the drivetrain

        Returns:
            None
        """
        # Store motors within the object
        self.left_motors = left_motors
        self.right_motors = right_motors

        # Invert the rotation direction on one side of the drivetrain, because
        # the motors on each side face opposite from one another
        self.right_motors.setInverted(True)

        # Enable differential drive functionality within the subsystem
        self.drive_train = wpilib.drive.DifferentialDrive(self.left_motors, self.right_motors)

    # ***
    # FOR YOU: to use a subsystem for autonomous purposes, we need to minimize
    # the impact of deadbands. A deadband on a motor (or a set of motors, like)
    # a drivetrain) is an input value below which the device will not operate.
    # For example, if we set the input percentage deadband to 25% and we pass
    # the motor an input percentage of 10%, then the motor will not run.
    # Conversely, if we pass this motor 40%, then it will run at 40% output.

    # Deadbands (and, similarly, deadzones for joysticks) help smooth the
    # operating experience for robot drivers. The DifferentialDrive class
    # we used above defaults to add 2% to the motor deadbands for the whole
    # drivetrain for this purpose. Motors also have fixed minimal deadbands
    # due to physical limitations in exerting a rotating force above the
    # force of friction.

    # With autonomous, we have full programmatic control and thus do not
    # need to worry as much about jitteriness. And, generally, we want to
    # have available as much of the full functionality of the robot as possible.
    # Thus, we want to eliminate any deadbands that exist purely to help drivers,
    # like the DifferentialDrive deadband.

    # To do this, write code meeting the following requirements:
    # 1) Create a new method called "setDeadband" within this WestCoastDrivetrain
    #    class, taking one argument: the deadband percentage below which the
    #    drivetrain will not operate.
    #       a) Call the drivetrain instance attribute's own .setDeadband() method
    #          and pass it the deadband input argument from your method

    # Your code will be analagous to the following:
    # def setParameter(self, value):
    #   self.attribute.setParameter(value)

    # <your code here>

    # ***

    def tankDrive(self, left_input_perc, right_input_perc, square_inputs=True):
        """
        Operate the drivetrain using tank drive, meaning that the speeds for
        each side of the drivetrain are explicitly specified using human input.

        Args:
            left_input_perc: float with domain [-1, 1] setting percentage of
                output to run the left drive motors at
            right_input_perc: float with domain [-1, 1] setting percentage of
                output to run the right drive motors at
            square_inputs: True if the two input percentages should be squared
                before passing to the drivetrain, False otherwise. Defaults to True

        Returns:
            None
        """
        # Operate the robot using tank drive
        self.drive_train.tankDrive(
            left_input_perc, right_input_perc, squareInputs=square_inputs
        )
