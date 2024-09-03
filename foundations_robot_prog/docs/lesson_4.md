# Lesson 4

## Overview

Welcome to Lesson 4! Now that you've built a subsytem, you're going to use it in more complicated ways through commands. Subystems define what is on the robot and a basic interface for using it. Commands define what action a subsystem should take for a given period of time. You should know that a subsystem can only be operated on by one command at at time.

Additionally, we're going to expand our usage of the Xbox controller to use buttons. Buttons can be used by the driver to trigger specific commands. The button we'll use will allow us to switch from our starting drive system to a different one. We're going to introduce you to arcade drive before returning to tank drive. 

## Code Development Steps

Clicking the step number header will open the file requiring code. Within the opened code file, look for "FOR YOU (\<development_step_number_here\>)" within the code - this signals that you have something to do.

### [4.1](../lesson_4/subsystems/drivetrain.py)

Similar to what we did with tank drive, we're going to use a method provided by the DifferentialDrive instance attribute to do arcade drive. This saves us from manually figuring out how to translate speed and rotation into motor values for each side of the robot.

You'll use the following method:

- \<your_diff_drive_instance_attribute\>.arcadeDrive(): takes speed and turn percentages, as described in the above docstring, to operate the drivetrain.

Call the .arcadeDrive() method from your differential drive instance attribute, passing it the speed and turn percentage values given in the parameters above.

The code will be analagous to the following:

```
self.subsytem_operator.operate(speed_input, turn_input)
```

### [4.2](../lesson_4/commands/arcade_drive.py)

The first step is to create instance attributes to store each of the input parameters for later use, similar to what we did for the subsystem. One key but possibly confusing point here is that everything in Python is considered an object, even functions. This means that we can save our callable functions to instance attributes just like any other object.

Create instance attributes for each of the three input parameters above.

The code should be analagous to the following:

```
self.some_input = some_input
self.other_input = other_input
self.subsystem_to_use = subsystem_to_use
```

### [4.3](../lesson_4/commands/arcade_drive.py)

Now, we need to assign the drivetrain subsystem to the command so the robot code executor knows to run this command on the drivetrain. By knowing the subsystems that every command uses, the robot executor can prevent multiple commands trying to use the same subsystem at the same time.

You'll need the following method to write this code:

- self.addRequirements(): takes one or more subsytems as arguments, telling the robot exector that this command requires the given subsytems to perform its action

Add the instance attribute for the drivetrain subsystem as a requirement for this command.

Your code should be analagous to the following:

```
self.myCommandNeeds(self.needed_subsystem)
```

### [4.4](../lesson_4/commands/arcade_drive.py)

Let's tell the robot what it should do when running arcade drive. We're going to use the specific arcade drive interface we wrote in the drivetrain subsystem and pass it the speed and turn angle percentages. Both percentages have domain [-1, 1] - the drivetrain interface has more information on how these translate to moving the robot.

You'll need the following method:

- \<your_drivetrain_instance_attribute\>.arcadeDrive(): operates the drivetrain using speed and turn variables. Takes two arguments, the first being the percentage of max robot speed of domain [-1, 1], the second being the percentage of max turn rate of domain [-1, 1].

Use the arcadeDrive interface and your instance attributes for speed percentage and turn percentage to operate the drivetrain. Remember that the percentages are callable functions, not floats, but arcadeDrive will expect floats as arguments.

The code will be analagous to the following:

```
self.subsystem.operate(self.some_input(), self.other_input())
```

### [4.5](../lesson_4/commands/arcade_drive.py)

We're going to tell the drivetrain motors to stop whenever this end method is called. To do that, we'll set the speed and turn percentages to both be zero.

You'll need the following method:
- \<your_drivetrain_instance_attribute\>.arcadeDrive(): operates the drivetrain using speed and turn variables. Takes two arguments, the first being the percentage of max robot speed of domain [-1, 1], the second being the percentage of max turn rate of domain [-1, 1].

Pass zeros as arguments to the arcade drive call to tell the drive motors to stop.

The code will be analagous to the following:

```
self.subsystem.operate(stop_value, stop_value)
```

### [4.6](../lesson_4/robot.py)

At this point, we have a tank drive class written, but we are currently not using it in our robot code. We need to import our custom class into this file, allowing us to use it in our robot class. This is similar to what we do with third-party libraries, except here we do it with our own code.

Import your tank drive class from the tank drive file in the commands folder.

The code will be analagous to the following:

```
from folder.file import MyClass
```

### [4.7](../lesson_4/robot.py)

We're going to set the default command for the drivetrain to be an instance of the ArcadeDrive command we wrote earlier. The speed will be given using the vertical value of the left joystick, while the turn rate will be given using the horizontal value of the right joystick.
        
To instantiate the command, we're going to make use of lambda functions. A lambda function allows us to define a function without saving it or giving it a name. Lambda functions can take any number of arguments and return the result of the expression given when it gets called. Lambdas are often used as arguments to other functions or methods, allowing it to be called as often as needed within that logic.

You'll need the following:

- \<drivetrain_instance_attribute\>.setDefaultCommand(): sets the default command for the subsystem the method is attached to. Because our custom drivetrain subsystem inherits from SubsystemBase, it has a setDefaultCommand method taken from the parent class. .setDefaultCommand() takes one argument, an instantiated command object.

- ArcadeDrive(): custom command class that tells the robot executor to use arcade drive to operate the drivetrain. Takes three arguments: a callable function returning the speed percentage, a callable function returning the turn rate percentage, and the drivetrain subsystem.

Set the default command of the drivetrain instance attribute to be arcade drive, passing callable left Y joystick and right X joystick values as the frist two arguments and the drivetrain instance attribute as the third argument. Remember, the Y axis on a joystick is vertical and the X axis is horizontal.

The code will be analagous to the following:

```
self.subsystem.giveDefaultCommand(
    Command(
        lambda: self.input_device.getLeftVertical(),
        lambda: self.input_device.getRightHorizontal(),
        self.subsystem
    )
)
```

### [4.8](../lesson_4/commands/tank_drive.py)

Now that you've seen every part of the commands framework and written a fair amount of robot code, we have a challenge for you - write a command class from scratch! You'll implement tank drive, which you worked with closely in lesson 3, as a command.

The requirements for this class are as follows:
1. Import the commands2 package at the top of the code
2. Create a new class that inherits from commands2.Command
3. Write a constructor method that takes three arguments: the output percentage for the left side, the output input percentage for the right side, and the drivetrain subsystem.
    1. Store each argument as their own instance attributes
    2. Add the drivetrain subsytem as a requirement of the command instance
4. Override the "execute" method, taking no arguments
    1. Use the drivetrain subsystem's .tankDrive() method to drive the robot using tank drive. Pass the called left input percentage and right input percentage as arguments. Remember, with commands these inputs are callable functions that need to be called to get the current float values
5. Override the "end" method, taking an argument called "interrupted"
    1. Use the drivetrain subsystem's .tankDrive() method to set the output percentages for each side of the robot to be zero.
6. Override the "isFinished" method, taking no arguments, to return False

Your code will be very analagous to the ArcadeDrive command class we wrote earlier. Use it as a guide and figure out where to change things to implement tank drive in place of arcade drive.

### [4.9](../lesson_4/robot.py)

Now, we'll run the custom tank drive command class that you wrote when the Y button is pressed on the controller. Buttons are considered digital inputs, where a press results in a True Boolean while no press results in a False Boolean for the button.

You'll need the following:

- \<driver_controller_instance_attribute\>.y().onTrue(): calls the "y" method on the Xbox controller to return a trigger for a new command. The trigger's "onTrue" method specifies what command should be triggered when the trigger state is set to True (in this case, when the Y button is returning True). .onTruce() takes one argument, an instantiated command to run.

- \<your_custom_tank_drive_class\>: custom command class that tells the robot executor to use tank drive to operate the drivetrain. Takes three arguments: a callable function returning the left output percentage, a callable function returning the right output percentage, and the drivetrain subsystem.

Run an instantiated TankDrive command when the Y button has been pressed on the driver's controller. Pass callable left Y joystick and right Y joystick values as the frist two arguments to TankDrive and the drivetrain instance attribute as the third argument to TankDrive.

The code will be analagous to the following:

```
self.input_device.button().whenTrue(
    Command(
        lambda: self.input_device.getLeftVertical(),
        lambda: self.input_device.getRightVertical(),
        self.subsystem
    )
)
```