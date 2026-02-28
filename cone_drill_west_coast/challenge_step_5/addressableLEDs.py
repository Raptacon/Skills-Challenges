import wpilib
import time

class addressableLEDs:
    def __init__(self):
        #Ensure LEDs are connected to PWM, not DIO.
        self.lengthLED = 10
        self.activatedLED = 0
        self.movementLED = 1
        self.speedLED = 0.1
        
        self.led = wpilib.AddressableLED(9)
        self.led.setLength(self.lengthLED)
        self.led_buffer = []

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

        time.sleep(self.speedLED)