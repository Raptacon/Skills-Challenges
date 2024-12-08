# Challenge Step 3

- Documentation helper: [metadocs.md](../../metadocs.md)
- Command line helper: [command_line_help.md](../../command_line_help.md)

## Overview

Welcome to Challenge Step 3! Now that you've built a subsytem, you're going to use it in more complicated ways through commands.

Subystems define what things are physically on the robot and provide basic interfaces for using them. Commands define what action a subsystem should take for a given period of time. You should know that a subsystem can only be operated on by one command at a time - if a subsystem were told to perform multiple actions at the same time, it would get very confused.

Additionally, we're going to expand our usage of the Xbox controller to include a button. Buttons are digital (true/false) inputs which can be pressed by the driver to trigger specific commands. The button we'll program will allow us to switch from our starting drive system to an alternative one. The drive system we'll start with is arcade drive - once we're done programming it, we'll return to tank drive.

## Code Development Steps

### [3.1](../challenge_step_3/subsystems/drivetrain.py)

#### Description

We'll start by diving back into WestCoastDrivetrain, where we already have the tank drive code from the last challenge step. We'll expand the capabilities of our class by incorporating arcade drive. Arcade drive means that we provide both a single signed speed percentage for the whole robot and a single signed turn angle percentage to allow steering. A negative value for either indicates the opposite direction of a positive value.

Arcade drive is somewhat similar to a car - the gas petal would be similar to providing the speed percentage, while the steering wheel would be similar to providing the turn angle percentage.

Similar to what we did with tank drive, we're going to use a method provided by the instance attribute of type DifferentialDrive to do arcade drive. This saves us from manually figuring out how to translate speed and rotation into motor values for each side of the robot.

#### Preexisting Assets

- \<your_diff_drive_instance_attribute\>.arcadeDrive(): takes speed and turn percentages, as described in the docstring of WestCoastDrivetrain.arcadeDrive(), to operate the drivetrain

#### Requirements

1. Scroll up to the constructor (\_\_init\_\_) method of WestCoastDrivetrain and identify the instance attribute created using DifferntialDrive. Scroll back down to arcadeDrive(). We'll fill in this method in the following requirements.
2. Call the arcade drive method from your differential drive instance attribute. Note that this is the arcade drive method for DifferentialDrive, <em>not</em> for WestCoastDrivetrain.
3. In the same line of code as requirement (2), pass as arguments to that method the speed and turn percentage values given in the parameters described in the preexisting assets.

#### Analogous Code

```
self.actor.do_something(first_parameter, second_parameter)
```

### [3.2](../challenge_step_3/commands/arcade_drive.py)

Now we'll transition to creating commands. The first step here is to create instance attributes to store each of the constructor input parameters for later use, similar to what we did for the subsystem.

One key but possibly confusing point here is that everything in Python is considered an object, even functions. This means that we can save our callable functions to instance attributes just like any other object. A common pattern with programming commands is to pass it callables that continually ("periodically") update the values they return over the course of the game.

#### Preexisting Assets

- Use the parameters given in the constructor (\_\_init\_\_) method

#### Requirements

1. Create separate instance attributes for each of the three input parameters of the constructor.

#### Analogous Code

```
self.first_thing = first_thing
self.second_thing = second_thing
self.third_thing = third_thing
```

### [3.3](../challenge_step_3/commands/arcade_drive.py)

#### Description

Now, we need to assign the drivetrain subsystem to the command so the robot code executor knows to run this command on the drivetrain. By knowing the subsystems that every command uses, the robot executor can prevent a situation where multiple commands try to use the same subsystem at the same time.

In WPILib lingo, we say that a command "requires" one or more subsystems in order to perform its actions. Note that commands can require multiple subsystems, but subsystems can only be required by one active command at a single moment in time. This means there is a one-to-many (1:M) relationship between commands and subsystems (commands:subsystems) on any given tick of the robot clock.

#### Preexisting Assets

- self.addRequirements(): takes one or more subsystems as arguments, telling the robot executor that this command requires the given subsystems to perform its action

#### Requirements

1. Identify which instance attribute contains the drivetrain subsystem, and add it as a requirement for the ArcadeDrive command.

#### Analogous Code

```
self.require_something(self.thing_required)
```

### [3.4](../challenge_step_3/commands/arcade_drive.py)

#### Description

We've attached parts of the robot to the arcade drive command - now, let's tell the robot what it should actually do when the command is running. The .execute() method of a command is where these actions are defined. Want we want is for the robot to drive according to the speed and turn angle given by the driver via the joysticks.

To do this, we're going to use the specific arcade drive interface we wrote in substep (3.1) and pass it the speed and turn angle percentages. Both percentages have domain [-1, 1] - the docstring for arcadeDrive() in the [drivetrain interface](../challenge_step_3/subsystems/drivetrain.py) has more information on how these translate to moving the robot.

#### Preexisting Assets

- Instance attributes created in substep (3.2)
- \<your_drivetrain_instance_attribute\>.arcadeDrive(): operates the drivetrain using speed and turn variables. Takes two arguments, the first being the percentage of max robot speed of domain [-1, 1], the second being the percentage of max turn rate of domain [-1, 1].

#### Requirements

1. Use the arcade drive interface and your instance attributes for speed percentage and turn percentage to operate the drivetrain. Remember that the percentages are callable functions, not floats, but .arcadeDrive() will expect floats as arguments.

#### Analogous Code

```
self.actor.do_something(self.first_updating_thing(), self.second_updating_thing())
```

### [3.5](../challenge_step_3/commands/arcade_drive.py)

#### Description

At some point, whether by choice, by interruption, or by changing operating mode (autonomous, teleoperated, disabled), a command will stop running. We need to define within the .end() method what the desired behavior is once the command, well, ends.

For arcade drive, we're going to tell the drivetrain motors to completely stop whenever this end method is called. To do that, we'll set the speed and turn percentages to both be zero.

#### Preexisting Assets

- \<your_drivetrain_instance_attribute\>.arcadeDrive(): operates the drivetrain using speed and turn variables. Takes two arguments, the first being the percentage of max robot speed of domain [-1, 1], the second being the percentage of max turn rate of domain [-1, 1].

#### Requirements

1. Call arcade drive from the drivetrain instance attribute, passing the method zeros as its speed and turn angle arguments to tell the drive motors to stop.

#### Analogous Code

```
self.actor.do_something(stop_value, stop_value)
```

### [3.6](../challenge_step_3/robot.py)

#### Description

The ArcadeDrive command is complete, now we need to use it in our robot code. We're going to set the default command for the drivetrain to be an instance of this command. The speed will be given using the vertical (Y) value of the left joystick, while the turn rate will be given using the horizontal (X) value of the right joystick.

To instantiate the command, we're going to make use of lambda functions. Functions take some set of inputs, run some code using those inputs, and return a resulting set of outputs. A lambda function allows us to define a function without saving it or giving it a name. Lambda functions can take any number of arguments and return the result of the written expression when it gets called. Lambdas are often used as arguments to other functions or methods, allowing it to be called as often as needed within that logic.

#### Preexisting Assets

- \<drivetrain_instance_attribute\>.setDefaultCommand(): sets the default (runs if no other command is running) command for the calling subsystem. Because our custom drivetrain class inherits from the SubsystemBase class, it has a setDefaultCommand method taken from that parent class. .setDefaultCommand() takes one argument, an instantiated command object.

- commands.arcade_drive.ArcadeDrive(): custom command class that tells the robot executor to use arcade drive to operate the drivetrain. Takes three arguments: a callable function returning the speed percentage, a callable function returning the turn rate percentage, and the drivetrain subsystem. Note that we directly imported this class, so you should not include the "commands.arcade_drive." part in your code.

#### Requirements

1. Set a variable to be an instantiated arcade drive command. The constructor of the command takes callable left Y joystick and right X joystick values as its first two arguments and the drivetrain instance attribute as its third argument.
2. Set the default command of the drivetrain instance attribute to be the command object you created in requirement (1).

#### Analogous Code

```
some_command = SomeCommand(
    lambda: self.accessor.get_some_value(),
    lambda: self.accessor.get_other_value(),
    self.required_thing
)
self.some_thing.do_something(some_command)
```

### [3.7](../challenge_step_3/commands/tank_drive.py)

#### Description

Now that you've seen every part of the commands framework and written a fair amount of robot code, we have a challenge for you - write a command class from scratch! You'll implement tank drive, with which you worked closely in challenge step 2, as a command.

#### Preexisting Assets

- commands2: WPILib package that provides code assets for the commands framework
- commands2.Command: base class for building new custom commands

#### Requirements

1. Import the commands2 package at the top of the code
2. Create a new class that inherits from commands2.Command
3. Write a constructor method that takes three arguments: the output percentage for the left side, the output input percentage for the right side, and the drivetrain subsystem.
    1. Store each argument as their own instance attributes
    2. Add the drivetrain subsystem as a requirement of the command instance
4. Override the "execute" method, taking no arguments
    1. Use the drivetrain subsystem's .tankDrive() method to drive the robot using tank drive. Pass the called left input percentage and right input percentage as arguments. Remember, with commands these inputs are callable functions that need to be called to get the current float values
5. Override the "end" method, taking an argument called "interrupted"
    1. Use the drivetrain subsystem's .tankDrive() method to set the output percentages for each side of the robot to be zero.
6. Override the "isFinished" method, taking no arguments, to return False

#### Analogous Code

Your code will be very analogous to the ArcadeDrive command class we wrote earlier. Use it as a guide and figure out where to change things to implement tank drive in place of arcade drive.

### [3.8](../challenge_step_3/robot.py)

#### Description

At this point, you've written a tank drive command class, but we are currently not using it in our robot code. We need to import our custom class into this file, allowing us to use it in our robot class. This is similar to what we do with third-party libraries, except here we do it with our own code.

#### Preexisting Assets

- commands.tank_drive.\<name_of_your_tank_drive_command_class\>: custom command class that implements tank drive for a DifferentialDrive subsystem 

#### Requirements

1. Import only your tank drive class from the tank drive file in the commands folder.

#### Analogous Code

```
from some_folder.some_file import SomeClass
```

### [3.9](../challenge_step_3/robot.py)

Now, we'll run the custom tank drive command that you wrote in substep 3.7 when the Y button is pressed on the controller. Buttons are considered digital inputs, where a press results in a True Boolean while no press results in a False Boolean for the button.

#### Preexisting Assets

- \<driver_controller_instance_attribute\>.y().onTrue(): calls the "y" method on the Xbox controller to return a trigger for a new command. The trigger's "onTrue" method specifies what command should be triggered when the trigger state is set to True (in this case, when the Y button is returning True). .onTrue() takes one argument, an instantiated command to run.

- \<your_custom_tank_drive_class\>: custom command class, imported in substep 3.8, that tells the robot executor to use tank drive to operate the drivetrain. Takes three arguments: a callable function returning the left output percentage, a callable function returning the right output percentage, and the drivetrain subsystem.

#### Requirements

1. Scroll up to the WestCoastRobot.robotInit() definition. Identify the Xbox driver controller instance attribute and drivetrain instance attribute. Scroll back down to to the .teleopPeriodic() method, which we'll fill in over the remaining requirements.
2. Set a variable to be an instantiated tank drive command. In that command's constructor, pass callable left Y joystick and right Y joystick values as its first two arguments the drivetrain instance attribute as its third argument.
3. Run that tank drive command when the Y button has been pressed on the driver's controller. 

#### Analogous Code

```
some_command = SomeCommand(
    lambda: self.accessor.get_some_value(),
    lambda: self.accessor.get_other_value(),
    self.required_thing
)
self.some_thing.do_something(some_command)
```