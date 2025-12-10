# Challenge Step 2

- Documentation helper: [metadocs.md](../../metadocs.md)
- Command line helper: [command_line_help.md](../../command_line_help.md)

## Overview

Welcome to Challenge Step 2! Now that we've moved one side of the drivetrain by using the motors, let's expand upon this and actuate the other side of the drivetrain. By having control of both sides, we'll be able to drive the robot!

We can now start to think about the whole drivetrain as a subsystem. Subsystems are an integrated set of components that work together to provide a focused range of functionality. For example, an arm subsystem may consist of three motors: one to raise the arm, one to extend it, and another to run a piece grabber. Drivetrain subsystems are typically comprised of the drive motors and sensors that track the distance driven and the heading (direction) of the robot. 

If you look at the package imports in our [robot.py](../challenge_step_2/robot.py) file, you'll notice that we import our own drivetrain class from our own subsystems folder. It is generally advised to organize Python code that either a) provides similar functionality, or b) operates temporally in a common part of the program's overall control flow, in the same folders/modules. Part of this step will require you to write code within the custom WestCoastDrivetrain class that is imported into robot.py.

## Code Development Steps

### [2.1](../challenge_step_2/subsystems/drivetrain.py)

#### Description

The first step in setting up the drivetrain subsystem is to store the motors as instance attributes. This will allow us to use them in other methods within this class and extract data from them at any time. We specifically use instance attributes because we want to be able to create our drivetrain using the specific motors that exist on our physical robot - we could use a different manufacturer's motors on a different robot.

#### Preexisting Assets

- Use the parameters given in the constructor (\_\_init\_\_) method

#### Requirements

1. Create instance attributes for each motor controller group and set each one equal to its respective parameter (left_motors, right_motors).

#### Analogous Code

```
self.one_thing = given_one_thing
self.second_thing = given_second_thing
```

### [2.2](../challenge_step_2/subsystems/drivetrain.py)

#### Description

Now we need to ensure that pressing the left and right joysticks in the same direction results in each side of the drivetrain propelling the robot same direction. The motors face opposite to one another - you can imagine two arrows that each extrude separately from the shaft of a motor out beyond the side of the chassis. Those arrows would point in opposite directions.

Now, imagine perpendicular rotation around those arrows - this represents motor rotation. Facing forward, clockwise rotation of the right motors would result in backward motion, while clockwise rotation of the left motors would result in forward motion. Take a look at the robot to confirm this.

We want the same joystick value (recall that values can be between 1 and -1) to correspond to the same motion direction for both sides of the drivetrain. Because a) the same sign of the joystick values results in the same rotation direction, and b) the same rotation direction results in opposite robot motion direction for each side of the robot, we need to invert the spin for one side of motors.

On motors, positive output percentage values correspond to clockwise spin, while negative output percentage values correspond to counterclockwise spin. Pushing up on a joystick returns a negative joystick value, which when passed to a motor means the motor getting negative output percentage values. We want pushing up on the joysticks to result in forward motion, which means we want these negative values to correspond to forward motion.

#### Preexisting Assets

- \<attribute_for_appropriate_group_of_motors\>.setInverted(): tells the motors within the group whether to flip the direction of rotation. Takes one Boolean argument, where True means the direction should be flipped.

#### Requirements

1. Look at the robot and think about the relationship between joystick inputs and motor spin direction. Determine which motor needs to be inverted so pushing the joysticks in the same direction results in the robot moving in that direction
2. Invert the spin of the motors on one side of the drivetrain (the side determined appopriate in requirement (1))

#### Analogous Code

```
self.thing.do_something(a_boolean)
```

### [2.3](../challenge_step_2/subsystems/drivetrain.py)

#### Description

To wrap up the constructor, we're going to create a generic interface for using the drive motors. WPILib provides a differential drive interface that can be used to operate two-sided drivetrains like our West Coast robot. Differential drive means that the robot moves according to the difference between the velocities of the two sides of the robot.

For example, if both sides are propelling forward at 10 meters per second, then the robot will go forward at 10 meters per second. If the left side is going forward at 15 meters per second and the right side is going forward at 5 meters per second, however, then the robot will continue to go forward but will also turn right at a rate proportional to the difference in the velocities.

The precise pathing of the robot can be calculated using kinematics, which is the physics of motion.

#### Preexisting Assets

- wpilib.drive.DifferentialDrive: provides a generic differential drive interface along with methods for more specific interfaces. Takes in two groups of motors as arguments.

#### Requirements

1. Create a drive train instance attribute set to a constructed DifferentialDrive object. Pass the motor group instance attributes you created in substep (2.1) as arguments.

#### Analogous Code

```
self.actor = SomeActor(self.one_thing, self.other_thing)
```

### [2.4](../challenge_step_2/subsystems/drivetrain.py)

#### Description

Instead of manually sending the output values to each of their respective motor groups, we're going to use a method provided by the DifferentialDrive class to do this for us. Generally, if an open source package provides the capabilities we're looking for with a clean but appropriately configurable interface, then we should use what the package provides.

We're going to use a specific differential drive interface called tank drive. Tank drive means that we directly provide the output values of each side of the robot.

The generic DifferentialDrive class also provides other specific interfaces for operating the motors, making it a useful abstraction of different drive systems for two-sided drivetrains like ours. We'll have you use another popular interface, arcade drive, in the next challenge step.

#### Preexisting Assets

- Use the parameters given in the WestCoastDrivetrain.tankDrive() method
- \<attribute_for_diff_drive\>.tankDrive(): takes left and right motor output percentage values, as described in the WestCoastDrivetrain.tankDrive() docstring, to operate the two sides of the drivetrain.

#### Requirements

1. Call the tank drive method from your differential drive instance attribute. Note that this is the tank drive method for DifferentialDrive, <em>not</em> for WestCoastDrivetrain.
2. In the same line of code as requirement (1), pass as arguments to that method the output percentage values given in the parameters described in the preexisting assets.

#### Analogous Code

```
self.actor.do_something(first_parameter, second_parameter)
```

### [2.5](../challenge_step_2/robot.py)

#### Description

Now that we completed the WestCoastDrivetrain class, we'll create a drivetrain instance attribute within our robot - we want to be able to use the drivetrain object in all methods that the robot class provides. Additionally, we want to ensure that data associated with the drivetrain is maintained - this helps with both maintaining the state of the robot and debugging it.

#### Preexisting Assets

- subsystems.drivetrain.WestCoastDrivetrain: custom drivetrain class that we wrote to interface with the robot. Note that we directly imported this class, so you should not include the "subsystems.drivetrain." part in your code.

#### Requirements

1. Create an instance attribute, giving a constructed WestCoastDrivetrain object as its value.
2. In the same line of code as requirement (1), pass as arguments to the constructor the two motor groups for the two sides of the robot.

#### Analogous Code

```
self.drive_thing = DriveThing(self.some_thing, self.other_thing)
```

### [2.6](../challenge_step_2/robot.py)

#### Description

In challenge step 1, we used one joystick to operate one side of the robot - now, we'll use the other joystick to operate the other side of the robot too. As part of the WestCoastDrivetrain class, you filled in code for a .tankDrive() method. We're going to pass the up/down (or Y axis) values of each joystick as arguments to that method.

Remember - pressing all the way up on a joystick gives a Y value of -1, while pressing all the way down gives a Y value of 1.

#### Preexisting Assets

- \<your_drivetrain_attribute\>.tankDrive(): passes motor output percentage values (1 = 100%, -1 = 100% in opposite direction) to each side of the robot directly in order to drive

- \<your_controller_attribute\>.getLeftY(): retrieves how far the left joystick has been pressed up/down as a numeric value between -1 and 1

- \<your_controller_attribute\>.getRightY(): same as getLeftY() but for the right joystick

#### Requirements

1. Briefly scroll up to the robotInit() method defined within WestCoastRobot. Identify the instance attribute for the Xbox driver controller. Also make note of the drivetrain instance attribute you created in substep (2.5).
2. Scroll back down to the defined teleopPeriodic() method. Begin filling it in by retrieving the Y values from both the left and right joysticks. These are accessible using the Xbox driver controller instance attribute.
3. Finish filling in teleopPeriodic() by calling your drivetrain instance attribute's tank drive method, passing it the left and right joystick Y values from requirement (2) as arguments.

#### Analogous Code

```
some_value = self.value_accessor.get_some_value()
other_value = self.value_accessor.get_other_value()
self.drive_thing.do_something(some_value, other_value)
```
