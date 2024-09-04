# ***
# FOR YOU (4.1)

import commands2


class DiffDriveStraight(commands2.Command):
    def __init__(self, drivetrain, speed):
        super().__init__()
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
        super().__init__()
        self.drivetrain = drivetrain
        self.speed = speed

    def execute(self):
        self.drivetrain.tankDrive(self.speed, -1 * self.speed, square_inputs=False)

    def end(self, interrupted):
        self.drivetrain.tankDrive(0, 0)

    def isFinished(self):
        return False

# ***
