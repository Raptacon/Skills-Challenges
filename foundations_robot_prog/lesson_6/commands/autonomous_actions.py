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


class DiffDriveDonuts(commands2.CommandBase):
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
# FOR YOU: you can write any actions you want to include in your routine here.
# We've included the actions from Lesson 5 so you have examples readily available
# for reference. Remember to inherit from commands2.CommandBase and make
# __init__, execute, end, and isFinished methods. You can always schedule
# a specific action command in robot.py and run it in the simulator to test it.

# <your code here>

# ***
