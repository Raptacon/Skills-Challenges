# Lesson 5

## Overview

Welcome to Lesson 5! Now that you have a good grasp of how to program a West Coast robot to be driven using an Xbox controller, we're going to introduce you to operating the robot autonomously. Autonomous operation means that the robot performs actions without any human input. FRC matches often start with 15 seconds where robots run completely autonomously, so having good capabilities in this area is a major advantage toward winning games.

Fundamentally, every autonomous routine can be represented as a mapping from match time to actuator inputs. Mathematically, this would look like f: t -> {inputs}. If we defined such a function for all time points in the period and had a perfect understanding of the physical system, then we could run the same routine repeatedly and have the robot perform the same actions exactly the same way every time. In reality, however, we do not have a perfect physical understanding. This means every individual routine run will be slightly different due to deviations between what we know and what reality is. To correct for this, we often use sensors to collect information about the physical world and define goal states that we want our robot to reach. Thus, a more complete autonomous routine mapping function would look like f: {t, sensors, state} -> {inputs, state}, where the mapping also includes control mechanisms that help us transition from the current state to the goal.

We won't cover sensors, states, and control theory here in this lesson, though you will have the opportunity to learn more about these in the future if you so desire. For this lesson, we'll stick to a basic time-to-input representation and have the robot perform some simple actions.

## Code Development Steps

Clicking the step number header will open the file requiring code. Within the opened code file, look for "FOR YOU (\<development_step_number_here\>)" within the code - this signals that you have something to do.

The recommended completion path for this lesson is as follows:

3. Write the first code block in commands/autonomous_routines.py, then come back here and use it. Use the method you wrote in step 2 here and rescale the input speed here as well. Sim test and deploy your code.
4. Write the second code block in commands/autonomous_routines.py, then come back here and use it. Sim test and deploy your code.
5. Write the third code block in commands/autonomous_routines.py, then come back here and use it. Sim test and deploy your code.

### [5.1](../lesson_5/commands/autonomous_actions.py)

To create a comprehensive autonomous routine, we first need to define a set of atomic actions that will occur within that routine. An action could be driving straight, turning a specified angle, quickly stopping, etc. Each action will be respresented as a custom command class - this allows us organize complex behavior and better define rules for when commands should be considered complete.

We're going to define two actions here - one to drive the robot in a straight line, either forward or backward, and one to have the robot spin in place (do donuts).

To do this, write code that meets the following requirements:

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
3. Create another new class called "DiffDriveDonuts" that inherits from commands2.Command.
    1. Write a constructor method that takes two arguments: the drivetrain subsystem, and the speed percentage at which the robot should drive.
        1. Call the parent class's constructor by calling the \_\_init\_\_() method from super()
        2. Store each argument as their own instance attributes
    2. Override the "execute" method, taking no arguments
        1. Use the drivetrain instance attribute's .tankDrive() method to drive the robot using the same speed for both sides. Pass the speed percentage instance attribute twice to this call as arguments, once for the left side and again for the right side. For the right side, multiply the speed percentage by -1 here - this will cause the two sides to go in opposite directions at the same speed. Then, pass False to the "square_inputs" argument to tell the drivetrain not to square the speed percentages. We want direct control, not transformed control.
    3. Override the "end" method, taking an argument called "interrupted"
        1. Use the drivetrain subsystem's .tankDrive() method to set the motor percentages for each side of the robot to be zero.  
    4. Override the "isFinished" method, taking no arguments, to return False 

### [5.2](../lesson_5/subsystems/drivetrain.py)

To use a subsystem for autonomous purposes, we need to minimize the impact of deadbands. A deadband on a motor (or a set of motors, like a drivetrain) is an input value below which the device will not operate. For example, if we set the input percentage deadband to 25% and we pass the motor an input percentage of 10%, then the motor will not run. Conversely, if we pass this motor 40%, then it will run at 40% output.

Deadbands (and, similarly, deadzones for joysticks) help smooth the operating experience for robot drivers. The DifferentialDrive class we used above defaults to add 2% to the motor deadbands for the whole drivetrain for this purpose. Motors also have fixed minimal deadbands due to physical limitations in exerting a rotating force above the force of friction.

With autonomous, we have full programmatic control and thus do not need to worry as much about jitteriness. And, generally, we want to have available as much of the full functionality of the robot as possible. Thus, we want to eliminate any deadbands that exist purely to help drivers, like the DifferentialDrive deadband.

To do this, write code meeting the following requirements:

1. Create a new method called "setDeadband" within this WestCoastDrivetrain class, taking one argument: the deadband percentage below which the drivetrain will not operate.
    1. Call the drivetrain instance attribute's own .setDeadband() method and pass it the deadband input argument from your method

Your code will be analagous to the following:

```
def setParameter(self, value):
    self.attribute.setParameter(value)
```

### [5.3](../lesson_5/robot.py)

Once you've updated subsystems/drivetrain.py, you'll need to call the drivetrain instance attribute's .setDeadband() method to set the overall drivetrain's deadband to be zero.

The code will be analogous to the following:

```
self.subsystem.setParameter(-1)
```

### Interlude - Describing Autonomous Routines

Now that we have a set of autonomous action commands, we need to compose them into autonomous routines. Routines accomplish one or more goals without human input. For example, in the 2024 FRC game, autonomous routines would shoot a piece that was pre-loaded on the robot, then go acquire a piece from the ground, then position the robot for shooting, then shoot the piece, and so on until the autonomous period ended. A common theme is that autonomous routines involve performing a small set of similar actions multiple times from different positions.

For this lesson, we'll start by building a routine to drive forward for a couple of seconds, stop, and then come back. Then, we'll extend that routine to spin in place in one direction, stop, then spin back in the opposite direction.

To do this, we need to introduce a new aspect of the commands framework: command compositions. Command compositions allow you to build more complex commands by setting rules for how to run multiple simpler commands together. You can find available compositions on the following webpage: https://robotpy.readthedocs.io/projects/commands-v2/en/latest/commands2.cmd/functions.html

You may notice that the compositions listed there are functions that return command objects rather than classes themselves. There is a class version of each composition, however we generally recommend using the simpler function interface unless you have an explicit reason to use a class.

We're going to make usse of the following compositions here:

- commands2.cmd.sequence(): runs a given set of commands in the order they are provided as arguments. Our sequence will be: drive forward -> wait -> drive backward -> wait -> spin one way -> wait -> spin back.

### [5.4](../lesson_5/commands/autonomous_routines.py)

We're going to start by filling out the drive straight routine. We've written the sequence command structure and told Python to return the command it produces. You will need to pass the individual commands that comprise the routine to the sequence call.

The routine will start by having the robot drive forward for 1 second. Then, the robot will stop sending power to the motors for one second, and finally the robot will drive backward for 1 second. In theory, the robot should return to its original position.

Use command composition functions and the "drive straight" class you wrote in the actions file to create comamnd objects for the three steps described above. To run a single drive straight step, you use your custom command and a timeout method call to run it for a set. duration. Note that commands execute on every clock tick until terminated. To drive the robot backward, you'll need to multiply the speed given in the args above by -1. Directly pass each composed command as separate arguments to the sequence call - you do not need to assign them to variables first.

You will need the following to do this:

- commands2.cmd.waitSeconds(): creates a command object that does nothing but runs for a specified number of seconds. Takes the duration in seconds as its only argument.

- aa.DiffDriveStraight(): your custom command that drives the robot in a straight direction.

The code will be analagous to the following:

```
some_composition(wait_some_time(), actionCommand(input1, input2)).stopAfter(seconds),
wait_some_time(),
some_composition(wait_some_time(), actionCommand(input1, -1 * input2)).stopAfter(seconds)
```

### [5.5](../lesson_5/robot.py)

We wrote the motor percentage rescale calculation for you, now you'll need to use it. We want the motors to operate at 25% speed (0.25 as a float). The motors have a minimum output percentage of 4% (0.04 as a float) and a maximum output percentage of 100% (1 as a float).

Set a speed variable to be the result of a rescale_motor_output() call. Pass the function the desired speed percentage, minimum output precentage, and maximum output percentage as described above.

Your code will be analogous to the following:

```
value = some_function(input1, input2, input3)
```

### [5.6, 5.8. 5.10](../lesson_5/robot.py)

Once you have an autonomous routine in place, you can use use it here. Because we don't have any clock-specific adjustments to the routine, we will use it in the initialization call instead of the periodic call.

In the backend, the robot executor runs a scheduler that determines which commands to run on a given clock tick. Before, we changed the default command of the drivetrain subsytem, which automatically scheduled that command. Now, we need to explicitly schedule our autonomous routine commands. Once the command completes, it will be removed from the schedule.

We recommend that you start by calling the drive straight routine and scheduling it (5.6). Then, you should delete that code and replace it by calling the spin-in-place routine and scheduling it (5.8). Finally, you should delete that code and replace it by calling the complete drive routine that does both (5.10). For each routine call, you will pass it the drivetrain instance attribute of this robot class and the speed variable you created above.

One routine call and schedule will be analogous to the following:

```
some_routine(self.subsystem, drive_parameter).putOnSchedule()
```

### [5.7](../lesson_5/commands/autonomous_routines.py)

Now, we're going to build out the spinning-in-place routine. The donut routine will be very similar to the drive straight routine, except it will use the other custom command class you wrote. We're going to let you write out the full function definition so you get practice writing functions in addition to classes.

The requirements for this step are as follows:

1. Create a new function for the donut routine, taking a drivetrain subsystem and a speed percentage as arguments.
2. Within this function, immediately return the result of a commands2.cmd.sequence() composition call. Pass arguments to this sequence call defined as follows:
    1. Instantiate a command object using your custom donut drive class. Your custom command will need to be passed the drivetrain and speed percentage given above as arguments to its constructor. Then, immediately call .withTimeout() from that object, passing this method 1 (for 1 second) as its only argument.
    2. Use a commands2.cmd.waitSeconds() call to make a command that does nothing for 1 second.
    3. Repeat the above sub-requirement for the third command, but multiply the speed percentage by -1 to make the robot spin the opposite direction.

The code will be highly analogous to drive_straight_routine

### [5.9](../lesson_5/commands/autonomous_routines.py)

To finish, we'll combine the drive straight and spin-in-place routines together to make a complete routine. They will be separated by a one second wait.

The requirements for this step are as follows:

1. Create a new function for the combined drive routine, taking a drivetrain subsystem and a speed percentage as arguments.
2. Within this function, immediately return the result of a commands2.cmd.sequence() composition call. Pass arguments to this sequence call defined as follows:
    1. Call drive_straight_routine(), defined above, to make the first command. Pass it the drivetrain and speed percentage given above.
    2. Use a commands2.cmd.waitSeconds() call to make a command that does nothing for 1 second.
    3. Call your donut route function to make the third command. Pass it the drivetrain and speed percentage given above.
