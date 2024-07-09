# ***
# FOR YOU: to create a comprehensive autonomous routine, we first need to
# define a set of atomic actions that will occur within that routine. An action
# could be driving straight, turning a specified angle, quickly stopping, etc.
# Each action will be respresented as a custom command class - this allows us
# organize complex behavior and better define rules for when commands should
# be considered complete.

# We're going to define two actions here - one to drive the robot in a
# straight line, either forward or backward, and one to have the robot spin
# in place (do donuts).

# To do this, write code that meets the following requirements:
# 1) Import the commands2 package
# 2) Create a new class named "DiffDriveStraight" that inherits from
#    commands2.CommandBase.
#    suggest the robot is driving straight.
#       a) Write a constructor method that takes two arguments: the drivetrain
#          subsystem, and the speed percentage at which the robot should drive.
#               i) Store each argument as their own instance attributes
#       b) Override the "execute" method, taking no arguments
#               i) Use the drivetrain instance attribute's .tankDrive() method
#                  to drive the robot using the same speed for both sides. Pass
#                  the speed percentage instance attribute twice to this call
#                  as arguments, once for the left side and again for the
#                  right side. Then, pass False to the "square_inputs" argument
#                  to tell the drivetrain not to square the speed percentages.
#                  We want direct control, not transformed control.
#       c) Override the "end" method, taking an argument called "interrupted"
#               i) Use the drivetrain subsystem's .tankDrive() method to set the
#                  motor percentages for each side of the robot to be zero.  
#       d) Override the "isFinished" method, taking no arguments, to return False    
# 3) Create another new class called "DiffDriveDonuts" that inherits from
#    commands2.CommandBase.
#       a) Write a constructor method that takes two arguments: the drivetrain
#          subsystem, and the speed percentage at which the robot should drive.
#               i) Store each argument as their own instance attributes
#       b) Override the "execute" method, taking no arguments
#               i) Use the drivetrain instance attribute's .tankDrive() method
#                  to drive the robot using the same speed for both sides. Pass
#                  the speed percentage instance attribute twice to this call
#                  as arguments, once for the left side and again for the
#                  right side. For the right side, multiply the speed percentage
#                  by -1 here - this will cause the two sides to go in opposite
#                  directions at the same speed. Then, pass False to the
#                  "square_inputs" argument to tell the drivetrain not to square
#                  the speed percentages. We want direct control, not transformed
#                  control.
#       c) Override the "end" method, taking an argument called "interrupted"
#               i) Use the drivetrain subsystem's .tankDrive() method to set the
#                  motor percentages for each side of the robot to be zero.  
#       d) Override the "isFinished" method, taking no arguments, to return False 

import commands2


class DiffDriveStraight(commands2.CommandBase):
    def __init__(self, drivetrain, speed):
        self.drivetrain = drivetrain
        self.speed = speed

    def execute(self):
        self.drivetrain.tankDrive(self.speed, self.speed, square_inputs=False)

    def end(self, interrupted):
        self.drivetrain.tankDrive(0, 0)

    def isFinished(self):
        return False


class DiffDriveDonuts(commands2.Command):
    def __init__(self, drivetrain, speed):
        self.drivetrain = drivetrain
        self.speed = speed

    def execute(self):
        self.drivetrain.tankDrive(self.speed, -1 * self.speed, square_inputs=False)

    def end(self, interrupted):
        self.drivetrain.tankDrive(0, 0)

    def isFinished(self):
        return False

# ***
