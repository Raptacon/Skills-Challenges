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
        # FOR YOU: the first step in setting up the drivetrain subsystem is to 
        # store the motors as instance attributes. This will allow use to use them
        # in other methods within this class and extract data from them at any time.
        # We specifically use instance attributes because we want to be able to
        # create our drivetrain using the specific motors that exist on our physical
        # robot - we could use a different manufacturer's motors on a different robot.

        # Create instance attributes for each motor controller group and set each one
        # equal to its respective parameter (left_motors, right_motors) given above.
        # The code should be analagous to the following:
        # self.some_motors = some_group_of_motors
        # self.more_motors = group_of_more_motors

        # <your code here>

        # ***

        # ***
        # FOR YOU: now we need to ensure that pressing the left and right joysticks
        # in the same direction results in each side of the drivetrain propelling the
        # robot same direction. The motors face opposite to one another - you can imagine
        # two arrows that each extrudes separately from the shaft of a motor out beyond
        # the side of the chassis. Those arrows would point in opposite directions.
        # This means that a clockwise rotation of the right motors would result in
        # forward motion, while a clockwise rotation of the left motors would result
        # in backward motion. Take a look at the robot to confirm this. We want the same
        # joystick value to correspond to the same motion direction for both sides of the
        # drivetrain, which means we need to invert the spin for one side of motors.

        # Positive voltage percentage values correspond to clockwise spin, while negative
        # voltage percentage values correspond to counterclockwise spin. Keep in mind
        # that pushing up on a joystick results in our motor getting negative voltage
        # percentage values, and we want pushing up to result in forward motion.

        # Looking at the robot and thinking about the relationsthip between joystick
        # inputs and motor spin direction, invert the spin of the motors on one side of
        # the drivetrain. You'll need the following method to do this:

        # <attribute_for_appropriate_group_of_motors>.setInverted(): tells the motors
        # within the group whether to flip the direction of rotation. Takes one Boolean
        # argument, where True means the direction should be flipped. The code should
        # be analagous to the following:
        # self.some_motor.changeSpinDirection(True)

        # <your code here>

        # ***

        # ***
        # FOR YOU: to wrap up the constructor, we're going to create that generic
        # interface for using the drive motors. WPILib provides a differential
        # drive interface that can be used to operate two-sided drivetrains like
        # our West Coast robot. Differential drive means that the robot moves according
        # to the difference between the velocities of the two sides of the robot.
        # For example, if both sides are propelling forward at 10 meters per second,
        # then the robot will go forward at 10 meters per second. If the left side
        # is going forward at 15 meters per second and the right side is going forward
        # at 5 meters per second, however, then the robot will continue to go forward
        # but will also turn right at a rate proportional to the difference in the
        # velocities. The precise pathing of the robot can be calculated using
        # kinematics, which is the physics of motion.

        # To operate the drivetrain using differential drive, you'll need to create
        # an object using the following class:

        # wpilib.drive.DifferentialDrive: provides a generic differential drive
        # interface along with methods for more specific interfaces. Takes in
        # two groups of motors as arguments.

        # Create a drive train instance attribute set equal to a DifferentialDrive
        # object. Pass the motor group instance attributes you created earlier as
        # arguments. Your code should be analagous to the following:
        # self.subsystem_operator = Operator(self.some_motors, self.more_motors)

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
        # FOR YOU: instead of manually sending the voltage values to each of their
        # respective motor groups, we're going to use a method provided by the
        # DifferentialDrive class to do this for us. Generally, if an open source
        # package provides the capabilities we're looking for with a clean but
        # appropriately configurable interface, then we should use what the package
        # provides.

        # The DifferentialDrive class also provides other specific interfaces for
        # operating the motors, making it a useful abstraction of different drive
        # systems for two-sided drivetrains like ours. We'll have you use another
        # popular interface, arcade drive, in the next lesson.

        # Here, you will use the following method to do tank drive:
        # <attribute_for_diff_drive>.tankDrive(): takes left and right motor voltage
        # percentage values, as described in the above docstring, to operate the
        # two sides of the drivetrain.

        # Call the tankDrive method from your differential drive instance attribute,
        # passing it the voltage percentage values given in the parameters above.
        # Your code should be analagous to the following:
        # self.subsytem_operator.operate(leftInput, rightInput)

        # <your code here>

        # ***
        
        # Delete the "pass" below once you've written some code
        pass
