import wpilib
import time
import itertools
import random

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
        self.controllerSensitivity = 0.5

        self.allactivateLEDs = []
        self.deadspace = [0,8,8,9,8,8,8,8,8,9,0,0,0]
        self.internaloffset = [0,1,0,0,-1,0,-1,0,-1,-1,-1]
        self.gridLength = 0
        self.gridWidth = 0

        self.offset = 0
        self.leftscore = 0
        self.rightscore = 0


    def lightLEDs(self, color):
        self.led_buffer = []
        for i in range(self.lengthLED):
            led_data = wpilib.AddressableLED.LEDData()
            # if i == self.activatedLED:
            led_data.setLED(color)
            # else:
                # led_data.setLED(wpilib.Color.kBlack)
            # d_data.setRGB(255, 0, 0)
            self.led_buffer.append(led_data)
        self.led.setData(self.led_buffer)
        self.led.start()

        # if self.activatedLED == self.lengthLED or self.activatedLED >= self.lengthLED:
        #     self.movementLED = -1
        # if self.activatedLED == 0 or self.activatedLED <= 0:
        #     self.movementLED = 1
        # self.activatedLED += self.movementLED

    def lightMatrix(self, gridwidth, gridlength, LEDPattern):
        self.led_buffer = []
        self.allactivateLEDs = []
        self.deadspace = []
        self.gridLength = gridlength
        self.gridWidth = gridwidth

        for length in range(self.gridLength):
            for width in range(self.gridWidth):
                if LEDPattern[length][width] == 1:
                    self.allactivateLEDs.append(self.determineLEDPosition(horizontal = width + 1, vertical = length))

        for i in range(len(self.allactivateLEDs)):
                led_data = wpilib.AddressableLED.LEDData()
                if self.allactivateLEDs[i] != 0:
                    led_data.setLED(wpilib.Color.kAzure)
                else:
                    led_data.setLED(wpilib.Color.kBlack)
                self.led_buffer.append(led_data)
                self.led.setData(self.led_buffer)
                self.led.start()

    def lightExtendedMatrix(self, gridwidth, gridlength, LEDPattern):
        self.led_buffer = []
        self.allactivateLEDs = []
        self.deadspace = []
        self.gridLength = gridlength
        self.gridWidth = gridwidth

        for width in range(self.gridWidth):
            for length in range(self.gridLength):
                if LEDPattern[length][width+self.offset] == 1:
                    self.allactivateLEDs.append(self.determineLEDPosition(horizontal = width, vertical = length))

        for i in range(self.lengthLED):
            led_data = wpilib.AddressableLED.LEDData()
            if i in self.allactivateLEDs:
                led_data.setLED(wpilib.Color.kAzure)
            else:
                led_data.setLED(wpilib.Color.kBlack)
            self.led_buffer.append(led_data)
        self.led.setData(self.led_buffer)
        self.led.start()

        self.offset += 1

    def lightPongStart(self, gridlength, gridwidth):
        self.led_buffer = []
        self.allactivateLEDs = []
        self.gridLength = gridlength
        self.gridWidth = gridwidth

        self.leftpongposition = 5
        self.rightpongposition = 5
        
        self.ballx = 0
        self.bally = 0
        self.ballvelocityY = round(random.uniform(-1.0,1.0))

        if random.randint(1,2) == 1:
            self.ballvelocityX = 1
        else:
            self.ballvelocityX = -1

        self.allactivateLEDs.append(self.determineLEDPosition(horizontal = 0, vertical = self.leftpongposition - 1))
        self.allactivateLEDs.append(self.determineLEDPosition(horizontal = 0, vertical = self.leftpongposition))
        self.allactivateLEDs.append(self.determineLEDPosition(horizontal = 0, vertical = self.leftpongposition + 1))
        
        self.allactivateLEDs.append(self.determineLEDPosition(horizontal = self.gridWidth - 1, vertical = self.rightpongposition - 1))
        self.allactivateLEDs.append(self.determineLEDPosition(horizontal = self.gridWidth - 1, vertical = self.rightpongposition))
        self.allactivateLEDs.append(self.determineLEDPosition(horizontal = self.gridWidth - 1, vertical = self.rightpongposition + 1))

    def lightPongPeriodic(self, xControllerPosition, yControllerPosition):
        self.led_buffer = []
        self.allactivateLEDs = []

        if self.ballx == 1:
            if (self.bally == self.leftpongposition 
                or self.bally == self.leftpongposition - 1 
                or self.bally == self.leftpongposition + 1):
                    self.ballvelocityX *= -1
            else:
                return("left")
        elif self.ballx == self.gridWidth - 1:
            if (self.bally == self.rightpongposition
                or self.bally == self.rightpongposition - 1
                or self.bally == self.rightpongposition + 1):
                    self.ballvelocityX *= -1
            else:
                return("right")
        else:
            print("Scores: " + str(self.leftscore) + "-" + str(self.rightscore))

        if self.leftpongposition >= 9:
            self.leftpongposition = 9
        else:
            self.leftpongposition += xControllerPosition * self.controllerSensitivity
        if self.leftpongposition <= 1:
            self.leftpongposition = 1
        else:       
            self.leftpongposition += xControllerPosition * self.controllerSensitivity       
        if self.rightpongposition >= 9:
            self.rightpongposition = 9
        else:
            self.rightpongposition += yControllerPosition * self.controllerSensitivity
        if self.rightpongposition <= 1:
            self.rightpongposition = 1
        else:
            self.rightpongposition += yControllerPosition * self.controllerSensitivity

        self.ballx += self.ballvelocityX
        self.bally += self.ballvelocityY

        if self.bally == 0:
            self.ballvelocityY *= -1
        if self.bally == self.gridWidth:
            self.ballvelocityY *= -1

        self.allactivateLEDs.append(self.determineLEDPosition(horizontal = 0, vertical = self.leftpongposition - 1))
        self.allactivateLEDs.append(self.determineLEDPosition(horizontal = 0, vertical = self.leftpongposition))
        self.allactivateLEDs.append(self.determineLEDPosition(horizontal = 0, vertical = self.leftpongposition + 1))
        
        self.allactivateLEDs.append(self.determineLEDPosition(horizontal = self.gridWidth - 1, vertical = self.rightpongposition - 1))
        self.allactivateLEDs.append(self.determineLEDPosition(horizontal = self.gridWidth - 1, vertical = self.rightpongposition))
        self.allactivateLEDs.append(self.determineLEDPosition(horizontal = self.gridWidth - 1, vertical = self.rightpongposition + 1))
        
        self.allactivateLEDs.append(self.determineLEDPosition(horizontal = self.ballx, vertical = self.bally))
        
        for i in range(self.lengthLED):
            led_data = wpilib.AddressableLED.LEDData()
            if i in self.allactivateLEDs:
                led_data.setLED(wpilib.Color.kAzure)
            else:
                led_data.setLED(wpilib.Color.kBlack)
            self.led_buffer.append(led_data)
        self.led.setData(self.led_buffer)
        self.led.start()

        print("Pong Positions: " + str(self.leftpongposition) + "-" + str(self.rightpongposition))

        return None

    def determineLEDPosition(self, horizontal, vertical):
        # if abs(horizontal) >= self.gridWidth:
        #     return 0
        # if abs(vertical) >= self.gridLength:
        #     return 0

        if vertical % 2 == 0:
            self.LEDPosition = (self.gridWidth - horizontal) + (vertical * self.gridLength) + list(itertools.accumulate(self.deadspace))[int(vertical)] * 2 + self.internaloffset[int(vertical)]
        else:
            self.LEDPosition = horizontal + (vertical * self.gridLength) + list(itertools.accumulate(self.deadspace))[int(vertical)] * 2 + self.internaloffset[int(vertical)]
        return self.LEDPosition