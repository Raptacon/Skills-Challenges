import wpilib
from robotpy_ext.autonomous import StatefulAutonomous, state
from raptacon3200.utils.leds import Strip


class BreakBeam(StatefulAutonomous):
    MODE_NAME = "Break Beam"

    def __init__(self, led_strip, led_data, breakbeam):
        self.led_strip = led_strip
        self.led_data = led_data
        self.breakbeam = breakbeam
        self.smartdashboard = wpilib.SmartDashboard
        super().__init__()

    @state(first=True)
    def idle_state(self):
        self.smartdashboard.putBoolean("BreakBeam", not self.breakbeam.get())
        if not self.breakbeam.get():
            self.next_state("beam_broken")
        else:
            self.next_state("beam_not_broken")

    @state()
    def beam_broken(self):
        # Turn the LEDS red
        for led in self.led_data:
            led.setRGB(255, 0, 0)
        
        self.led_strip.setData(self.led_data)

        self.next_state("idle_state")

    @state()
    def beam_not_broken(self):
        # Turn the LEDS off
        for led in self.led_data:
            led.setRGB(0, 0, 0)

        self.led_strip.setData(self.led_data)

        self.next_state("idle_state")


class MyRobot(wpilib.TimedRobot):
    def robotInit(self):
        # Initialize the LED strip
        self.kLEDBuffer = 20
        self.breakbeam = wpilib.DigitalInput(0)
        self.led_strip = wpilib.AddressableLED(0)
        self.led_data = [
            wpilib.AddressableLED.LEDData() for _ in range(self.kLEDBuffer)
        ]
        self.strip = Strip(self.led_data, "State Machine")
        self.currentHue = 243
        self.currentBright = 0
        self.led_strip.setLength(self.kLEDBuffer)
        self.led_strip.setData(self.led_data)
        self.led_strip.start()

        # Initialize timer
        self.timer = wpilib.Timer()
        self.timer.start()

        # Initialize the state machine
        self.led_state_machine = BreakBeam(
            self.led_strip, self.led_data, self.breakbeam
        )

    def teleopInit(self):
        self.led_state_machine.on_enable()

    def teleopPeriodic(self):
        self.led_state_machine.on_iteration(self.timer.get())

    def disabledInit(self):
        self.led_state_machine.on_disable()


if __name__ == "__main__":
    wpilib.run(MyRobot)
