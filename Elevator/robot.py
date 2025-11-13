import commands2
import rev
import wpilib
import wpimath



class WestCoastRobot(commands2.TimedCommandRobot):
    def robotInit(self):
        super().__init__()
        
        self.driver_controller = wpilib.XboxController(1)
        self.intake_motor = rev.SparkFlex(11, rev.SparkLowLevel.MotorType.kBrushless)
        self.motor_encoder = self.intake_motor.getEncoder()
        self.motor_config = rev.SparkBaseConfig()
        self.goal = 0
        self.motorPID = self.intake_motor.getClosedLoopController()

        
        self.motor_config.inverted(False)
        (self.motor_config.closedLoop
            .pid(0.2, 0, 0)
            .outputRange(-0.3, 0.3)
            .setFeedbackSensor(rev.ClosedLoopConfig.FeedbackSensor.kPrimaryEncoder)
        )
        
        (
            self.motor_config.limitSwitch
            .forwardLimitSwitchEnabled(True)
            .forwardLimitSwitchType(rev.LimitSwitchConfig.Type.kNormallyOpen)
            .reverseLimitSwitchEnabled(True)
            .reverseLimitSwitchType(rev.LimitSwitchConfig.Type.kNormallyOpen)
        )
        
        self.conversionFactor = 1.09
        self.motor_config.encoder.positionConversionFactor(self.conversionFactor).velocityConversionFactor(self.conversionFactor / 60)
        self.intake_motor.configure(self.motor_config, rev.SparkBase.ResetMode.kNoResetSafeParameters, rev.SparkBase.PersistMode.kPersistParameters)

    def teleopInit(self):
        self.intake_motor.set(0)
        self.motor_encoder.setPosition(0)
        self.goal = 0
    def teleopPeriodic(self):
        
        # Button Binds
        self.ButtonA = self.driver_controller.getAButtonPressed()
        self.ButtonB = self.driver_controller.getBButtonPressed()
        self.ButtonX = self.driver_controller.getXButtonPressed()
        self.ButtonY = self.driver_controller.getYButtonPressed()
        self.RightY = self.driver_controller.getRightY()
        if self.RightY > 0.3:
            self.RightY = 0.3
        if self.RightY < -0.3:
            self.RightY = -0.3
        
        self.intake_motor.setVoltage((self.RightY)* -12)

        self.encoder_value = self.motor_encoder.getPosition()

        # check if values update
        self.toplimitswitch_tripped = self.intake_motor.getForwardLimitSwitch().get()
        self.bottomlimitswitch_tripped = self.intake_motor.getReverseLimitSwitch().get()

        if (self.toplimitswitch_tripped and self.intake_motor.get() > 0) or (self.bottomlimitswitch_tripped and self.intake_motor.get() < 0):
            self.intake_motor.set(0)

        wpilib.SmartDashboard.putNumber("Motor Speed", self.intake_motor.get())
        wpilib.SmartDashboard.putBoolean("TopTripped", self.toplimitswitch_tripped)
        wpilib.SmartDashboard.putBoolean("BottomTripped", self.bottomlimitswitch_tripped)
        wpilib.SmartDashboard.putNumber("Encoder Value", self.encoder_value)

        # 1u = .375in or .9525cm
        if self.ButtonA:
            self.goal = 30
        if self.ButtonX:
            self.goal = 20
        if self.ButtonY:
            self.goal = 10
        if self.ButtonB:
            self.goal = 0
        self.motorPID.setReference(self.goal, rev.SparkLowLevel.ControlType.kPosition, rev.ClosedLoopSlot.kSlot0)

        wpilib.SmartDashboard.putNumber("Goal Value", self.goal)