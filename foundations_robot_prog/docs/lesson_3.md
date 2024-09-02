# Lesson 3

## Overview

Welcome to Lesson 3! Now that we've moved one side of the drivetrain by using the motors, let's expand upon this and actuate the other side of the drivetrain. By having control of both sides, we'll be able to drive the robot!

We can now start to think about the whole drivetrain as a subsystem. Subsystems are an integrated set of components that work together to provide a focused range of functionality. For example, an arm subsystem may consist of three motors: one to raise the arm, one to extend it, and another to run a piece grabber Drivetrain subsystems are typically comprised of the drive motors and sensors that track the distance driven and the heading (direction) of the robot. 

If you look at the package imports above, you'll notice that we import our own drivetrain class from our own subsystems folder. It is generally advised to organize Python code that either provides similar functionality or operates temporally in a common part of the program's overall control flow in the same folders/modules. Part of this lesson will require you to write code within the WestCoastDrivetrain class.

## Code Development Steps

Clicking the step number header will open the file requiring code. Within the opened code file, look for "FOR YOU (\<development_step_number_here\>)" within the code - this signals that you have something to do.

### [3.1](../lesson_3/subsystems/drivetrain.py)

The first step in setting up the drivetrain subsystem is to  store the motors as instance attributes. This will allow use to use them in other methods within this class and extract data from them at any time. We specifically use instance attributes because we want to be able to create our drivetrain using the specific motors that exist on our physical robot - we could use a different manufacturer's motors on a different robot.

Create instance attributes for each motor controller group and set each one equal to its respective parameter (left_motors, right_motors) given above. The code should be analagous to the following:

```
self.some_motors = some_group_of_motors
self.more_motors = group_of_more_motors
```

### [3.2](../lesson_3/subsystems/drivetrain.py)

Now we need to ensure that pressing the left and right joysticks in the same direction results in each side of the drivetrain propelling the robot same direction. The motors face opposite to one another - you can imagine two arrows that each extrudes separately from the shaft of a motor out beyond the side of the chassis. Those arrows would point in opposite directions. This means that a clockwise rotation of the right motors would result in forward motion, while a clockwise rotation of the left motors would result in backward motion. Take a look at the robot to confirm this. We want the same joystick value to correspond to the same motion direction for both sides of the drivetrain, which means we need to invert the spin for one side of motors.

Positive voltage percentage values correspond to clockwise spin, while negative voltage percentage values correspond to counterclockwise spin. Keep in mind that pushing up on a joystick results in our motor getting negative voltage percentage values, and we want pushing up to result in forward motion.

Looking at the robot and thinking about the relationship between joystick inputs and motor spin direction, invert the spin of the motors on one side of the drivetrain. You'll need the following method to do this:

- \<attribute_for_appropriate_group_of_motors\>.setInverted(): tells the motors within the group whether to flip the direction of rotation. Takes one Boolean argument, where True means the direction should be flipped.

The code should be analagous to the following:

```
self.some_motor.changeSpinDirection(True)
```

### [3.3](../lesson_3/subsystems/drivetrain.py)

To wrap up the constructor, we're going to create that generic interface for using the drive motors. WPILib provides a differential drive interface that can be used to operate two-sided drivetrains like our West Coast robot. Differential drive means that the robot moves according to the difference between the velocities of the two sides of the robot. For example, if both sides are propelling forward at 10 meters per second, then the robot will go forward at 10 meters per second. If the left side is going forward at 15 meters per second and the right side is going forward at 5 meters per second, however, then the robot will continue to go forward but will also turn right at a rate proportional to the difference in the velocities. The precise pathing of the robot can be calculated using kinematics, which is the physics of motion.

To operate the drivetrain using differential drive, you'll need to create an object using the following class:

- wpilib.drive.DifferentialDrive: provides a generic differential drive interface along with methods for more specific interfaces. Takes in two groups of motors as arguments.

Create a drive train instance attribute set equal to a DifferentialDrive object. Pass the motor group instance attributes you created earlier as arguments.

Your code should be analagous to the following:

```
self.subsystem_operator = Operator(self.some_motors, self.more_motors)
```

### [3.4](../lesson_3/subsystems/drivetrain.py)

Instead of manually sending the voltage values to each of their respective motor groups, we're going to use a method provided by the DifferentialDrive class to do this for us. Generally, if an open source package provides the capabilities we're looking for with a clean but appropriately configurable interface, then we should use what the package provides.

The DifferentialDrive class also provides other specific interfaces for operating the motors, making it a useful abstraction of different drive systems for two-sided drivetrains like ours. We'll have you use another popular interface, arcade drive, in the next lesson.

Here, you will use the following method to do tank drive:

- \<attribute_for_diff_drive\>.tankDrive(): takes left and right motor voltage percentage values, as described in the above docstring, to operate the two sides of the drivetrain.

Call the tankDrive method from your differential drive instance attribute, passing it the voltage percentage values given in the parameters above.

Your code should be analagous to the following:

```
self.subsytem_operator.operate(leftInput, rightInput)
```

### [3.5](../lesson_3/robot.py)

Here, we'll create a drivetrain instance attribute within our robot - we want to be able to use the drivetrain object in the robot methods below while ensuring that data associated with the drivetrain is maintained. To do this, set an instance attribute to be a constructed WestCoastDrivetrain object, passing the two motor groups for the two sides of the robot as arguments to the constructor.

This will be analogous to the following:

```
self.subsystem = Subsystem(self.some_motors, self.other_motors)
```

### [3.6](../lesson_3/robot.py)

Last lesson we used one joystick to operate one side of the robot - now, we'll use the other joystick to operate the other side of the robot too. As part of the drivetrain class, you created a tankDrive method. We're going to pass the up/down values of each of the joysticks as arguments to the tankDrive method. Remember - pressing all the way up on a joystick gives a Y value of -1, while pressing all the way down gives a Y value of 1.

You'll need three methods to operate the robot using tank drive:

- \<your_drivetrain_attribute\>.tankDrive(): passes motor voltage percentage values (1 = 100%, -1 = 100% in opposite direction) to each side of the robot directly in order to drive.

- \<your_controller_attribute\>.getLeftY(): retrieves how far the left joystick has been pressed up/down as a numeric value between -1 and 1.

- \<your_controller_attribute\>.getRightY(): same as getLeftY() but for the right joystick

Call the drivetrain's tankDrive method, passing it the left and right joystick Y values.

The code here will be analagous to the following:

```
leftInput = self.device.getLeftJoystickVerticalPercentage()
rightInput = self.device.getRightJoystickVerticalPercentage()
self.subsystem.operate(leftInput, rightInput)
```