import commands2
from subsystems.drivetrain.drivetrain import SwerveDrivetrain


class PathPlannerRobot(commands2.TimedCommandRobot):
    def robotInit(self):
        self.drivetrain = SwerveDrivetrain()

    def robotPeriodic(self):
        commands2.CommandScheduler.getInstance().run()
        self.drivetrain.update_pose_estimator()

    def disabledInit(self):
        pass

    def disabledPeriodic(self):
        pass

    def autonomousInit(self):
        pass

    def autonomousPeriodic(self):
        pass

    def teleopInit(self):
        pass

    def teleopPeriodic(self):
        pass

    def testInit(self):
        pass

    def testPeriodic(self):
        pass
