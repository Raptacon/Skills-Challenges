# Challenge Step 1

- Documentation helper: [metadocs.md](../../metadocs.md)
- Command line helper: [command_line_help.md](../../command_line_help.md)

## Overview

Welcome to the first challenge step! In this step, we're going to get started with robot code. To program an FRC robot, we'll be making extensive use of the WPILib Python package. Packages are blocks of Python code that we can install on our system and use as part of our software. Python has a massive open source community that makes and supports tons of freely available and easily installable packages. WPILib, provided via a broader package called RobotPy, is one such package.

You can find documentation on RobotPy at https://robotpy.readthedocs.io/en/stable/index.html

Python software that uses WPILib starts with a [robot.py](../challenge_step_1/robot.py) file. Here, we write a class that represents our robot virtually and exposes functionality that will be directly used to operate the robot. If you are familiar with the concept of a "main" file, robot.py will be our equivalent of that.

We've taken care of much of the boilerplate for setting up the class. This way, you can focus on writing logic for operating the robot. That said, we encourage you to read through the docstrings and comments explaining what each part is doing. We'll be working on other parts of the class in future challenge steps.

## Code Development Steps

### [1.1](../challenge_step_1/robot.py)

#### Description

In Challenge Step 1, we'll focus on operating one side of a West Coast drivetrain. As you can see when loooking over the robot, we have two motors actuating the gears a given side - this gives our robot more power. It also means we can effectively treat the two motors as one motor. So, we'll start by representing our drive motors virtually.

#### Preexisting Assets

- phoenix5.WPI_TalonFX: this class represents one Talon motor on the robot. It takes a CAN bus port as an argument for its constructor method, telling the robot where on the CAN network it should send instructions for operating the motor. Look at the number on each motor set to see what port you should use.

- wpilib.MotorControllerGroup: this collects multiple motors together and forwards the instructions it receives to all of those motors. We want the drive motors on the same side to operate exactly the same. The constructor takes an arbitrary number of motors as arguments.

#### Requirements

1. Create two motors using the correct ports, and collect them with a motor controller group. The motor controller group must be an instance attribute - you can do this by using self.\<name\> = \<value\> syntax.

#### Analagous Code

```
self.one_thing = ThingClass(one_thing_port)
self.second_thing = ThingClass(second_thing_port)
self.thing_collector = Collector(self.one_thing, self.second_thing)
```

### [1.2](../challenge_step_1/robot.py)

#### Description

We need to set up some method of manually operating our motors. Here we'll create an XboxController and later we'll use one of its joysticks.

#### Preexisting Assets

- wpilib.XboxController: represents an Xbox controller as an input device to the robot. It takes one argument - a port number telling the driver station which input device to reference for receiving instructions.

#### Requirements

1. Create an instance attribute set to a created XboxController object. Give the controller port 0.

#### Analagous Code

```
self.thing = ThingConstructor(thing_port)
```

### [1.3](../challenge_step_1/robot.py)

#### Description

We have our physical devices represented virtually, now we need to use them! We're going to actuate one side of our drivetrain by pressing up and down on a joystick.

We control a motor programmatically by giving the motor a percentage of its maximum output, as well as a direction in the form of a sign (+/-). At maximum output, the motor goes at full speed; at 50% of the max output, it goes at half speed. Percentages are given using a float between -1 and 1, with 1 being 100% and -1 being 100% in the opposite direction.

For our joystick input, you only need to know two things for now (we'll focus heavily on driver controllers later on):

- The .getLeft* methods access the left joytick, .getRight* the right
- Pushing all the way up on a joystick gives a Y value of -1, pushing all the way down a Y value of 1, keeping it in the middle a value of 0

#### Preexisting Assets

- \<your_motor_controller_group_attribute\>.set(): tells the robot what percentage of maximum output to give to each motor in the collection. Takes one argument with a value between -1 and 1

- \<your_driver_controller_attribute\>.getLeftY(): retrieves how far the left joystick has been pressed up/down as a numeric value between -1 and 1, as described above

#### Requirements

1. Using your motor group instance attribute and Xbox controller instance attribute, set the speed and direction of the motors using the up/down (Y) value of the left joystick on the controller.

#### Analagous Code

```
self.physical_things.do_something(self.device_thing.retrieve_something())
```
