
import wpilib
from raptacon3200.utils.leds import Strip


class MyRobot(wpilib.TimedRobot):
    """Main robot class"""

    def robotInit(self):
        """Robot-wide initialization code should go here"""
        self.breakbeam = wpilib.DigitalInput(-1)  # The DIO port 0-9 on the RIO. You will have to physically verify this.
        self.kLEDBuffer = -1  # Count the number of LEDs on the bot. What happens if you get it wrong?
        self.leds = wpilib.AddressableLED(-1)  # The PWM port 0-9 on the RIO. You will have to physically verify this.

        self.ledData = [wpilib.AddressableLED.LEDData() for _ in range(self.kLEDBuffer)]
        self.strip = Strip(self.ledData, "Whatever")
        self.currentHue = 243   # Pick your favorite Hue
        self.currentBright = 0  # Pick how bright you'd like the LEDs

        self.leds.setLength(self.kLEDBuffer)
        self.leds.setData(self.ledData)
        self.leds.start()

    def autonomousInit(self):
        """Called when autonomous mode is enabled"""
        pass

    def autonomousPeriodic(self):
        pass

    def teleopPeriodic(self):
        """Called when operation control mode is enabled"""

        # Create a Smart Dashboard Entry for displaying the value of the breakbeam

        # Create some logic that checks to see if the breakbeam is broken an if so, do something with your LEDs

        # If the breakbean is NOT broken do something else, stop the LEDS or change colors

        # Don't forget to write a unit test for this!

        # To test, and pass this challenge, deploy your code to a bot, and observe the LEDS are not doing anything
        # when the beam is broken, observe the LEDS are flashing/moving/exit
        # do this several times to ensure that your logic is correct and repeatable
