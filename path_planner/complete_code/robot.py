import commands2


class PathPlannerRobot(commands2.TimedCommandRobot):
    def robotInit(self):
        pass

    def robotPeriodic(self):
        commands2.CommandScheduler.getInstance().run()

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
