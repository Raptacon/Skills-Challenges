import commands2


class TankDrive(commands2.CommandBase):
    def __init__(self, left_input_percentage, right_input_percentage, drivetrain):
        super().__init__()

        self.left_input_percentage = left_input_percentage
        self.right_input_percentage = right_input_percentage
        self.drivetrain = drivetrain

        self.addRequirements(self.drivetrain)     

    def execute(self):
        self.drivetrain.tankDrive(self.left_input_percentage, self.right_input_percentage)
    
    def end(self):
        self.drivetrain.tankDrive(0, 0)
    
    def isFinished(self):
        return False
