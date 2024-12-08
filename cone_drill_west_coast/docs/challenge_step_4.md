# Challenge Step 4

- Documentation helper: [metadocs.md](../../metadocs.md)
- Command line helper: [command_line_help.md](../../command_line_help.md)

## Overview

Welcome to Challenge Step 4! Now that you have a good grasp of how to program a West Coast robot to be driven using an Xbox controller, we're going to introduce you to operating the robot autonomously. Autonomous operation means that the robot performs actions without any human input. FRC matches often start with a 15-second period where robots run completely autonomously, so having good capabilities in this area is a major advantage toward winning games.

Fundamentally, every autonomous routine can be represented as a mapping from match time to actuator inputs. Mathematically, this would look like f: t -> {inputs}. If we defined such a function for all time points in the period and had a perfect understanding of the physical system, then we could run the same routine repeatedly and have the robot perform the same actions exactly the same way every time.

In reality, however, we do not have a perfect physical understanding. This means every individual routine run will be slightly different due to deviations between what we know and what reality is. To correct for this, we often use sensors to collect information about the physical world and define goal states that we want our robot to reach. Thus, a more complete autonomous routine mapping function would look like f: {t, sensors, state} -> {inputs, state}, where the mapping also includes control mechanisms that help us transition from the current state to the goal.

We won't cover sensors, states, and control theory here in this challenge step, though you will have the opportunity to learn more about these in the future if you so desire. Here, we'll stick to a basic time-to-input representation to have the robot complete the cone course.

## Code Development Steps

### [4.1](../challenge_step_4/commands/autonomous_actions.py)

#### Description

To create a comprehensive autonomous routine, we first need to define a set of atomic actions that will occur within that routine. An action could be driving straight, turning a specified angle, quickly stopping, etc. Each action will be respresented as a custom command class - this allows us organize complex behavior and better define rules for when commands should be considered complete.

We're going to define two actions here - one to drive the robot in a straight line, either forward or backward, and one to have the robot spin in place (do donuts).

#### Preexisting Assets

- commands2: WPILib package that provides code assets for the commands framework
- commands2.Command: base class for building new custom commands

#### Requirements

1. Import the commands2 package
2. Create a new class named "DiffDriveStraight" that inherits from commands2.Command.
    1. Write a constructor method that takes two arguments: the drivetrain subsystem, and the speed percentage at which the robot should drive.
        1. Call the parent class's constructor by calling the \_\_init\_\_() method from super()
        2. Store each argument as their own instance attributes
    2. Override the "execute" method, taking no arguments
        1. Use the drivetrain instance attribute's .tankDrive() method to drive the robot using the same speed for both sides. Pass the speed percentage instance attribute twice to this call as arguments, once for the left side and again for the right side. Then, pass False to the "square_inputs" argument to tell the drivetrain not to square the speed percentages. We want direct control, not transformed control.
    3. Override the "end" method, taking an argument called "interrupted"
        1. Use the drivetrain subsystem's .tankDrive() method to set the motor percentages for each side of the robot to be zero.
    4. Override the "isFinished" method, taking no arguments, to return False    
3. Create another new class named "DiffDriveDonuts" that inherits from commands2.Command.
    1. Write a constructor method that takes two arguments: the drivetrain subsystem, and the speed percentage at which the robot should drive.
        1. Call the parent class's constructor by calling the \_\_init\_\_() method from super()
        2. Store each argument as their own instance attributes
    2. Override the "execute" method, taking no arguments
        1. Use the drivetrain instance attribute's .tankDrive() method to drive the robot using the same speed for both sides. Pass the speed percentage instance attribute twice to this call as arguments, once for the left side and again for the right side. For the right side, multiply the speed percentage by -1 here - this will cause the two sides to go in opposite directions at the same speed. Then, pass False to the "square_inputs" argument to tell the drivetrain not to square the speed percentages. We want direct control, not transformed control.
    3. Override the "end" method, taking an argument called "interrupted"
        1. Use the drivetrain subsystem's .tankDrive() method to set the motor percentages for each side of the robot to be zero.  
    4. Override the "isFinished" method, taking no arguments, to return False 

#### Analogous Code

None

### [4.2](../challenge_step_4/subsystems/drivetrain.py)

#### Description

To use a subsystem for autonomous purposes, we need to minimize the impact of deadbands. A deadband on a motor (or a set of motors, like a drivetrain) is an input value below which the device will not operate. For example, if we set the percentage deadband to 25% and we pass the motor an output percentage value of 10%, then the motor will not run. Conversely, if we pass this motor 40%, then it will run at 40% output.

Deadbands (and, similarly, deadzones for joysticks) help smooth the operating experience for robot drivers. The DifferentialDrive class we used above defaults to add 2% to the motor deadbands for the whole drivetrain for this purpose. Motors also have fixed minimal deadbands due to physical limitations in exerting a rotating force above the force of friction.

With autonomous, we have full programmatic control and thus do not need to worry as much about jitteriness in driving the robot. And, generally, we want to have available as much of the full functionality of the robot as possible. Thus, we want to eliminate any deadbands that exist purely to help drivers, like the DifferentialDrive deadband.

#### Preexisting Assets

- \<drivetrain_instance_attribute\>.setDeadband(): applies a given deadband value to all motors in a drivetrain subsystem. Takes one argument: the deadband, between 0 and 1, below which motors will not operate

#### Requirements

1. Create a new method called "setDeadband" within this WestCoastDrivetrain class, taking one argument: the deadband percentage below which the drivetrain will not operate.
    1. Call the drivetrain instance attribute's own .setDeadband() method and pass it the deadband input parameter from your method

#### Analogous Code

```
def do_something(self, value):
    self.some_thing.do_something(value)
```

### [4.3](../challenge_step_4/robot.py)

#### Description

Now that you've updated the interface to WestCoastDrivetrain, you'll want to use the new method you wrote to eliminate the drivetrain's deadband.

#### Preexisting Assets

- <drivetrain_instance_attribute>.setDeadband(): applies a given deadband value to all motors in a drivetrain subsystem. Takes one argument: the deadband, between 0 and 1, below which motors will not operate

#### Requirements

1. Scroll up to the defined robotInit() method and identify the drivetrain instance attribute. Scroll back down to the 4.3 code writing section.
2. Set the deadband for that drivetrain to be zero.

#### Analogous Code

```
self.some_thing.do_something(value)
```

### Interlude - Describing Autonomous Routines

Now that we have a set of autonomous action commands, we need to compose them into autonomous routines. Routines accomplish one or more goals without human input. For example, in the 2024 FRC game, autonomous routines would shoot a piece that was pre-loaded on the robot, then go acquire a piece from the ground, then position the robot for shooting, then shoot the piece, and so on until the autonomous period ended. A common theme is that autonomous routines involve performing a small set of similar actions multiple times from different positions.

For this challenge step, we'll start by building a routine to drive forward for a couple of seconds, stop, and then come back. Then, we'll extend that routine to spin in place in one direction, stop, then spin back in the opposite direction.

To do this, we need to introduce a new aspect of the commands framework: command compositions. Command compositions allow you to build more complex commands by setting rules for runming multiple simpler commands together. You can find available compositions on the following webpage: https://robotpy.readthedocs.io/projects/commands-v2/en/latest/commands2.cmd/functions.html

You may notice that the compositions listed there are functions that return command objects rather than classes themselves. There is a class version of each composition, however we generally recommend using the simpler function interface unless you have an explicit reason to use a class.

### [4.4](../challenge_step_4/commands/autonomous_routines.py)

#### Description

We're going to start our journey into autonomous routines by filling out the drive straight routine. We've written a sequence command structure, which tells the robot to run commands in the order they are given, and told Python to return the command it produces. You will need to pass the individual commands that comprise the routine to the sequence call.

The routine will start by having the robot drive forward for 1 second. Then, the robot will stop sending power to the motors for one second, and finally the robot will drive backward for 1 second. In theory, the robot should return to its original position.

#### Preexisting Assets

- aa.DiffDriveStraight(): your custom command that drives the robot in a straight direction.

- aa.DiffDriveStraight.withTimeout(): tells the robot code how long to run the command for. Takes one argument: the number of seconds to run the command.

- commands2.cmd.waitSeconds(): creates a command object that does nothing but runs for a specified number of seconds. Takes the duration in seconds as its only argument.

#### Requirements

1. Use drive-straight command class you wrote in substep 4.1, and other commands as appropriate, in proper sequential order to complete the three routine actions outlined at the bottom of this substep's description. Command objects need to be instantiated and passed arguments to their constructors.
    - Note that commands execute once on every robot clock tick until terminated. You can think of this as an omnipresent while loop that runs your command code on every iteration.
    - To drive the robot backward, you'll need to multiply the speed given to the drive-straight command by -1.

#### Analogous Code

```
some_composition(SomeAction(required_thing, value).duration(time_value), some_action(time_value), SomeAction(required_thing, flipped_value).duration(time_value))
```

### [4.5](../challenge_step_4/robot.py)

#### Description

We wrote a motor percentage rescale calculation for you that ensures that the output percentage values you give fit properly within the new spectrum of possible values after changing the deadband. We want the motors to operate at 25% speed (0.25 as a float). The motors have a minimum output percentage of 4% (0.04 as a float) and a maximum output percentage of 100% (1 as a float).

#### Preexisting Assets

- rescale_motor_output(): function that linearly rescales a motor output percentage value to its deadband-censored spectrum. Takes three arguments: the output percentage you want the motor to run at, the minimum value of the motor's allowed percentage spectrum, and the maximum value of the motor's allowed percentage spectrum. The first argument has domain [-1, 1], the remaining have domain [0, 1]

#### Requirements

1. Create a speed variable set to the result of a rescale_motor_output() call. Pass the function the desired speed percentage, minimum output precentage, and maximum output percentage as expressed in this substep's description.

#### Analogous Code

```
value = some_function(first_input, second_input, third_input)
```

### [4.6, 4.8. 4.10](../challenge_step_4/robot.py)

#### Description

Once you have an autonomous routine in place, you can use use it in the robot's autonomousInit() method. Because we don't have any clock-specific adjustments to the routine, we will use it in the initialization call instead of the periodic call.

In the backend, the robot executor runs a scheduler that determines which commands to run on a given clock tick. Before, we changed the default command of the drivetrain subsystem, which automatically scheduled that command. Now, we need to explicitly schedule our autonomous routine commands. Once the command completes, it will be removed from the schedule.

#### Preexisting Assets

- aa.drive_straight_routine(): a routine that drives a robot forward at a given speed. Takes two arguments: the drivetrain that will run the routine, and a speed percentage value.
- aa.\<your_spin_routine\>(): a routine that spins the robot in-place. Takes two arguments: the drivetrain that will run the routine, and a speed percentage value. Won't be available until you complete substep 4.7.
- aa.\<your_complete_drive_routine\>(): a routine that combines straight driving and spinning in place. Takes two arguments: the drivetrain that will run the routine, and a speed percentage value. Won't be available until you complete substep 4.9.

#### Requirements

1. (4.6) Call the drive straight routine, passing it any required subsystems and the speed variable you created in substep 4.5, and schedule it. Confirm the routine works by sim testing and deploying this code to the robot.
2. (4.8) Once you've completed substep 4.7, come back here and delete the code you wrote in requirement (1). Then, call the spin-in-place routine, passing it any required subsystems and the speed variable you created in substep 4.5, and schedule it. Confirm the routine works by sim testing and deploying this code to the robot.
3. (4.10) Once you've completed substep 4.9, come back here and delete the code you wrote in requirement (2). Then, call the complete drive routine, passing it any required subsystems and the speed variable you created in substep 4.5, and schedule it. Confirm the routine works by sim testing and deploying this code to the robot.

#### Analogous Code

(for one routine call)

```
some_routine(self.required_thing, value).schedule_it()
```

### [4.7](../challenge_step_4/commands/autonomous_routines.py)

#### Description

Now that you've confirmed that the drive straight routine works, we're going to build out the spinning-in-place routine. The donut routine will be very similar to the drive straight routine, except it will use the other custom command class you wrote. We're going to let you write out the full function definition so you get practice writing functions in addition to classes.

#### Preexisting Assets

- commands2.cmd.sequence(): command composition that runs any commands given to it in the order they are given. Takes an arbitrary number of arguments, with each one being an instantiated command object.

- commands2.cmd.waitSeconds(): creates a command object that does nothing but runs for a specified number of seconds. Takes the duration in seconds as its only argument.

- aa.DiffDriveDonuts(): your custom command that makes the robot do circles in-place.

- aa.DiffDriveDonuts.withTimeout(): tells the robot code how long to run the command for. Takes one argument: the number of seconds to run the command.

#### Requirements

1. Create a new function for the donut routine, taking a drivetrain subsystem and a speed percentage as arguments.
2. Within this function, create a variable set to be a composed command returned by a commands2.cmd.sequence() call. Pass arguments to this sequence call defined as follows:
    1. Instantiate a command object using your custom donut drive class. Your custom command will need to be passed the drivetrain and speed percentage (given as arguments to your routine function, defined in requirement (1)) to its constructor. Make this command run for one second.
    2. Have the robot wait for one second.
    3. Repeat requirement (2.1) for the third command, but multiply the speed percentage by -1 to make the robot spin the opposite direction.
3. At the end of your routine function, return the composed command variable you created in requirement 2.
4. At the top of the [robot.py](../challenge_step_4/robot.py) file, import your routine function.

#### Analogous Code

The code will be highly analogous to drive_straight_routine

### [4.9](../challenge_step_4/commands/autonomous_routines.py)

#### Description

To finish, we'll combine the drive straight and spin-in-place routines together to make a complete routine. They will be separated by a one second wait.

#### Preexisting Assets

- commands2.cmd.sequence(): command composition that runs any commands given to it in the order they are given. Takes an arbitrary number of arguments, with each one being an instantiated command object.

- commands2.cmd.waitSeconds(): creates a command object that does nothing but runs for a specified number of seconds. Takes the duration in seconds as its only argument.

- drive_straight_routine(): a routine that drives a robot forward at a given speed. Takes two arguments: the drivetrain that will run the routine, and a speed percentage value.

- \<your_spin_routine\>(): a routine that spins the robot in-place. Takes two arguments: the drivetrain that will run the routine, and a speed percentage value.

The requirements for this step are as follows:

1. Create a new function for the combined drive routine, taking a drivetrain subsystem and a speed percentage as arguments.
2. Within this function, create and return a sequence command composition. This composition should start with the drive straight routine, then have the robot wait for a second, then finish with the spin-in-place routine.
3. At the top of the [robot.py](../challenge_step_4/robot.py) file, import your routine function.

#### Analogous Code

None - you're free as a bird now
