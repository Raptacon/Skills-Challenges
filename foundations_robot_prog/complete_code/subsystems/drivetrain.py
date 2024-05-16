import commands2
import wpilib


class WestCoastDrivetrain(commands2.SubsystemBase):
    def init(self, left_motors, right_motors):
        self.left_motors = left_motors
        self.right_motors = right_motors

        # For one motor, positive value means clockwise spin while for other
        # positive value means counterclockwise spin
        self.right_motors.setInverted(True)

        self.drive_train = wpilib.drive.DifferentialDrive(self.left_motors, self.right_motors)
