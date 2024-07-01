# ***
# FOR YOU: now that you've seen every part of the commands framework and
# written a fair amount of robot code, we have a challenge for you - write a
# command class from scratch! You'll implement tank drive, which you worked with
# closely in lesson 3, as a command.

# The requirements for this class are as follows:
# 1) Import the commands2 package at the top of the code
# 2) Create a new class that inherits from commands2.CommandBase
# 3) Write a constructor method that takes three arguments: the voltage input
#    percentage for the left side, the voltage input percentage for the right side,
#    and the drivetrain subsystem.
#       a) Store each argument as their own instance attributes
#       b) Add the drivetrain subsytem as a requirement of the command instance
# 4) Override the "execute" method, taking no arguments
#       a) Use the drivetrain subsystem's .tankDrive() method to drive the robot
#          using tank drive. Pass the called left input percentage and right input
#          percentage as arguments. Remember, with commands these inputs are callable
#          functions that need to be called to get the current float values.
# 5) Override the "end" method, taking an argument called "interrupted"
#       a) Use the drivetrain subsystem's .tankDrive() method to set the voltage
#          percentages for each side of the robot to be zero.
# 6) Override the "isFinished" method, taking no arguments, to return False

# Your code will be very analagous to the ArcadeDrive command class we wrote
# earlier. Use it as a guide and figure out where to change things to implement
# tank drive in place of arcade drive.

import commands2


class TankDrive(commands2.CommandBase):
    def __init__(self, left_input_percentage, right_input_percentage, drivetrain):
        super().__init__()

        self.left_input_percentage = left_input_percentage
        self.right_input_percentage = right_input_percentage
        self.drivetrain = drivetrain

        self.addRequirements(self.drivetrain)     

    def execute(self):
        self.drivetrain.tankDrive(self.left_input_percentage(), self.right_input_percentage())
    
    def end(self, interrupted):
        self.drivetrain.tankDrive(0, 0)
    
    def isFinished(self):
        return False


# ***
