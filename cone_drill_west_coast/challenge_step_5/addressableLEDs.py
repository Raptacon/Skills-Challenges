import wpilib
import time

class addressableLEDs:
    def __init__(self):
        #Ensure LEDs are connected to PWM, not DIO.
        self.lengthLED = 255
        self.activatedLED = 0
        self.movementLED = 1
        self.speedLED = 0.1
        
        self.led = wpilib.AddressableLED(1)
        self.led.setLength(self.lengthLED)
        self.led_buffer = []

        self.LEDPosition = 0

        self.allactivateLEDs = []
        self.gridLength = 0
        self.gridWidth = 0

    def lightLEDs(self):
        self.led_buffer = []
        for i in range(self.lengthLED):
            led_data = wpilib.AddressableLED.LEDData()
            if i == self.activatedLED:
                led_data.setLED(wpilib.Color.kAzure)
            else:
                led_data.setLED(wpilib.Color.kBlack)
            # d_data.setRGB(255, 0, 0)
            self.led_buffer.append(led_data)
        self.led.setData(self.led_buffer)
        self.led.start()

        if self.activatedLED == self.lengthLED or self.activatedLED >= self.lengthLED:
            self.movementLED = -1
        if self.activatedLED == 0 or self.activatedLED <= 0:
            self.movementLED = 1
        self.activatedLED += self.movementLED

    def lightMatrix(self, LEDPattern):
        self.led_buffer = []
        for width in LEDPattern:
            self.gridLength += 1
            for length in LEDPattern:
                if LEDPattern == 1:
                    self.allactivateLEDs.append(self.determineLEDPosition(horizontal = width, vertical = length))

        for i in self.allactivateLEDs:
            led_data = wpilib.AddressableLED.LEDData()
            if self.allactivateLEDs[i] != 0:
                led_data.setLED(wpilib.Color.kAzure)
            else:
                led_data.setLED(wpilib.Color.kBlack)
            self.led_buffer.append(led_data)
        self.led.setData(self.led_buffer)
        self.led.start()

    def determineLEDPosition(self, horizontal, vertical):
        self.LEDPosition = (self.gridLength(horizontal % 2) + (self.gridWidth + 1) + vertical)
        return self.LEDPosition