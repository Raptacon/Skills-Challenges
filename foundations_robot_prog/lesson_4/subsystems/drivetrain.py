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

    def tankDrive(self, left_voltage_perc, right_voltage_perc):
        """
        Operate the drivetrain using tank drive, meaning that the speeds for
        each side of the drivetrain are explicitly specified using human input.

        Args:
            left_voltage_perc: float with domain [-1, 1] setting percentage of
                max voltage to send to the left drive motors
            right_voltage_perc: float with domain [-1, 1] setting percentage of
                max voltage to send to the right drive motors

        Returns:
            None
        """
        # Operate the robot using tank drive
        self.drive_train.tankDrive(left_voltage_perc, right_voltage_perc)

    def arcadeDrive(self, speed_percentage, turn_angle_percentage):
        """
        The arcadeDrive method brings the differential drive's arcade drive
        capabilities to our subsytem. Arcade drive means that we tell the robot
        how fast we want to go and how much we want to turn. This is a notably
        different way to interact with the same differential drive system.

        This method has two parameters: speed_percentage is expected to be a float
        of domain [-1, 1] that gives the percentage of the robot's maximum speed
        to move. 1 equates to 100% of the maximum, while -1 equates to 100% of the
        maximum in the opposite direction. Depending on how you set up your motors,
        1 is typically the forward direction while -1 is typically backwards.
        turn_angle_percentage is expcted to be a float of domain [-1, 1] that
        gives the percentage of the robot's maximum turn sharpness. 1 equates to
        100% of the maxiumum to the right, while -1 equates to 100% of the maximum
        to the left.
        """
        # ***
        # FOR YOU: similar to what we did with tank drive, we're going to use
        # a method provided by the DifferentialDrive instance attribute to do
        # arcade drive. This saves us from manually figuring out how to translate
        # speed and rotation into motor values for each side of the robot.

        # You'll use the following method:
        # <your_diff_drive_instance_attribute>.arcadeDrive(): takes speed and
        # turn percentages, as described in the above docstring, to operate
        # the drivetrain.

        # Call the .arcadeDrive() method from your differential drive instance
        # attribute, passing it the speed and turn percentage values given in
        # the parameters above. The code will be analagous to the following:
        # self.subsytem_operator.operate(speed_input, turn_input)

        # <your code here>

        # ***

        # Delete the "pass" below once you've written some code
        pass
