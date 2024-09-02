import commands2
import wpilib
import wpilib.drive


class WestCoastDrivetrain(commands2.SubsystemBase):
    """
    We've created a "WestCoastDrivetrain" subsystem class to house our drive motor
    groups for each side of the robot and allow us to readily use these motors
    to drive. In a competition-ready version of this class, we would also track
    data on how far the motors have travelled, as well as the voltage value of the motors
    over time for diagnostic purposes.
    
    The methods written within a drivetrain class typically serve one of two purposes:
    a) provide an interface for using the drive motors to operate the robot, or
    b) reset diagnostic data values or set motor speeds to zero when entering
    the disabled state. Here, we have one method of purpose (a) called "tankDrive".

    Our class inherits from a foundational subsystem base class that we brought in from
    the commands2 part of the RobotPy ecosystem. This tells the robot code executor
    that it is working with a virtual representation of an integrated set of physical
    components. In full use of this robot code framework, there are specific ways,
    called commands, that we can use to tell subsystems what to do. We'll explore these
    more in the next lesson.
    """
    def __init__(self, left_motors, right_motors):
        """
        This constructor method has two parameters: the motor controller group
        for the left side of the drivetrain, and the motor controller group for the
        right side of the drivetrain. Drivetrain constructor methods typically
        take in all of the driver motors and set up a generic integrated interface for
        using them. Other methods will provide more specific interfaces that build
        on top of the generic interface.
        """
        # ***
        # FOR YOU (3.1)

        # <your code here>

        # ***

        # ***
        # FOR YOU (3.2)

        # <your code here>

        # ***

        # ***
        # FOR YOU (3.3)

        # <your code here>

        # ***

        # Delete the "pass" below once you've written some code
        pass

    def tankDrive(self, left_voltage_perc, right_voltage_perc):
        """
        The tankDrive method brings the differential drive's tank drive capabilities
        to our subsystem. Tank drive means that we directly tell the drivetrain how
        fast we want each side of the drivetrain to go. This extends the work we did
        telling a single motor how fast we wanted it to go using the joystick.

        This method has two paramters: left_voltage_perc is expected to be a float
        in the domain [-1, 1] that gives the percentage of the left-side motors'
        maximum voltage to apply. 1 equates to 100% of the maximum, while -1 equates
        to 100% of the maximum in the opposite direction. right_voltage_perc is the
        same as left_voltage_perc but for the right side motors.
        """
        # ***
        # FOR YOU (3.4)

        # <your code here>

        # ***
        
        # Delete the "pass" below once you've written some code
        pass
