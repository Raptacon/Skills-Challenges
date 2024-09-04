import commands2
import phoenix5
import wpilib
import wpimath

from commands.arcade_drive import ArcadeDrive
from commands.tank_drive import TankDrive
from subsystems.drivetrain import WestCoastDrivetrain


class WestCoastRobot(commands2.TimedCommandRobot):
    def robotInit(self):
        super().__init__()

        right_front_motor = phoenix5.WPI_TalonFX(31)
        right_back_motor = phoenix5.WPI_TalonFX(30)
        left_back_motor = phoenix5.WPI_TalonFX(20)
        left_front_motor = phoenix5.WPI_TalonFX(21)

        left_drive_motors = wpilib.MotorControllerGroup(left_front_motor, left_back_motor)
        right_drive_motors = wpilib.MotorControllerGroup(right_front_motor, right_back_motor)

        self.drivetrain = WestCoastDrivetrain(left_drive_motors, right_drive_motors)

        self.driver_controller = commands2.button.CommandXboxController(0)


    def disabledInit(self):
        pass

    def disabledPeriodic(self):
        pass

    def autonomousInit(self):
        pass

    def autonomousPeriodic(self):
        pass

    def teleopInit(self):
        if True:
            self.drivetrain.setDefaultCommand(
                TankDrive(
                    lambda: wpimath.applyDeadband(
                        self.driver_controller.getLeftY(),
                        0.1,
                        1
                    ),
                    lambda: wpimath.applyDeadband(
                        self.driver_controller.getRightY(),
                        0.1,
                        1
                    ),
                    self.drivetrain
                )
            )
        else:
            self.drivetrain.setDefaultCommand(
                ArcadeDrive(
                    lambda: wpimath.applyDeadband(
                        self.driver_controller.getLeftY(),
                        0.1,
                        1
                    ),
                    lambda: wpimath.applyDeadband(
                        self.driver_controller.getRightX(),
                        0.1,
                        1
                    ),
                    self.drivetrain
                )
            )

    def teleopPeriodic(self):
        pass
        #print(f"Current status of A button: {self.driver_controller.a()}")

    def testInit(self):
        pass

    def testPeriodic(self):
        pass


if __name__ == "__main__":
    wpilib.run(WestCoastRobot)
