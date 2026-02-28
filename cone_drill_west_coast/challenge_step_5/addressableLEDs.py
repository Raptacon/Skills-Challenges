import wpilib

class addressableLEDs:
    def __init__(self):
        self.potato = 5
        self.led = wpilib.AddressableLED(9)
        self.led.setLength(24)
        self.led_buffer = []

    def lightLEDs(self):
        for i in range(24):
            led_data = wpilib.AddressableLED.LEDData()
            led_data.setLED(wpilib.Color.kRed)
            # d_data.setRGB(255, 0, 0)
            self.led_buffer.append(led_data)
        self.led.setData(self.led_buffer)
        self.led.start()