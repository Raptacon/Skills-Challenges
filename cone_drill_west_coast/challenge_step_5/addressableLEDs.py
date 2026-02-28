import wpilib

class addressableLEDs:
    def __init__(self):
        #Ensure LEDs are connected to PWM, not DIO.
        self.led = wpilib.AddressableLED(9)
        self.led.setLength(30)
        self.led_buffer = []

    def lightLEDs(self):
        self.led_buffer = []
        for i in range(30):
            led_data = wpilib.AddressableLED.LEDData()
            led_data.setLED(wpilib.Color.kAzure)
            # d_data.setRGB(255, 0, 0)
            self.led_buffer.append(led_data)
        self.led.setData(self.led_buffer)
        self.led.start()