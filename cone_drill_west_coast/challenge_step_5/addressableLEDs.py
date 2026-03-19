import wpilib
import time
import itertools
import random
import math

class addressableLEDs:
    def __init__(self):
        #Ensure LEDs are connected to PWM, not DIO.

        self.lengthLED = 255
        # self.lengthLED = 256

        self.activatedLED = 0
        self.movementLED = 1
        self.speedLED = 0.1
        
        self.led = wpilib.AddressableLED(2)
        self.led.setLength(self.lengthLED)
        self.led_buffer = []

        self.LEDPosition = 0

        self.allactivateLEDs = []
        self.deadspace = [0,8,8,9,8,8,8,8,8,9,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        self.internaloffset = [0,1,0,0,-1,0,-1,0,-1,-1,-1,0,0,0,0,0,0,0]
        # self.deadspace = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        # self.internaloffset = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
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

        for i in range(self.lengthLED):
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
                print("width = " + str(width) + "length = " + str(length))
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

        self.leftpongposition = 4
        self.rightpongposition = 4
        self.controllerSensitivity = 0.51

        self.ballx = 9
        self.bally = 5
        self.ballvelocityY = 0.25

        if self.leftscore <= self.rightscore:
            self.ballvelocityX = 0.1
        else:
            self.ballvelocityX = -0.1

        self.allactivateLEDs.append(self.determineLEDPosition(horizontal = 0, vertical = self.leftpongposition - 1))
        self.allactivateLEDs.append(self.determineLEDPosition(horizontal = 0, vertical = self.leftpongposition))
        self.allactivateLEDs.append(self.determineLEDPosition(horizontal = 0, vertical = self.leftpongposition + 1))
        
        self.allactivateLEDs.append(self.determineLEDPosition(horizontal = self.gridWidth - 1, vertical = self.rightpongposition - 1))
        self.allactivateLEDs.append(self.determineLEDPosition(horizontal = self.gridWidth - 1, vertical = self.rightpongposition))
        self.allactivateLEDs.append(self.determineLEDPosition(horizontal = self.gridWidth - 1, vertical = self.rightpongposition + 1))

        self.allactivateLEDs.append(self.determineLEDPosition(horizontal = self.ballx, vertical = self.bally))

    def lightPongPeriodic(self, xControllerPosition, yControllerPosition, leftauto, rightauto):
        self.led_buffer = []
        self.allactivateLEDs = []


        if self.ballx <= 1 and self.ballvelocityX <= 0:
            if (round(self.bally) == self.leftpongposition
                or round(self.bally) == self.leftpongposition - 1
                or round(self.bally) == self.leftpongposition + 1
                or (round(self.bally) == self.leftpongposition - 2 and self.ballx == -1)
                or (round(self.bally) == self.leftpongposition + 2 and self.ballx == -1)
                ):
                    self.ballvelocityX *= -1
            else:
                return("left")
        elif self.ballx >= self.gridWidth - 2 and self.ballvelocityX >= 0:
            if (round(self.bally) == self.rightpongposition
                or round(self.bally) == self.rightpongposition - 1
                or round(self.bally) == self.rightpongposition + 1
                or (round(self.bally) == self.rightpongposition - 2 and self.ballx == self.gridWidth)
                or (round(self.bally) == self.rightpongposition + 2 and self.ballx == self.gridWidth)
                ):
                    self.ballvelocityX *= -1
            else:
                return("right")
        else:
            print("Scores: " + str(self.leftscore) + "-" + str(self.rightscore))


        if leftauto:
            self.leftpongposition = round(self.bally)
        else:
            self.leftpongposition += round(xControllerPosition * self.controllerSensitivity)
        if rightauto:
            self.rightpongposition = round(self.bally)
        else:
            self.rightpongposition += round(yControllerPosition * self.controllerSensitivity)

        if self.leftpongposition >= self.gridLength - 1:
            self.leftpongposition = self.gridLength - 2
        elif self.leftpongposition <= 0:
            self.leftpongposition = 1
        if self.rightpongposition >= self.gridLength - 1:
            self.rightpongposition = self.gridLength - 2
        elif self.rightpongposition <= 0:
            self.rightpongposition = 1

        self.ballx += self.ballvelocityX
        self.bally += self.ballvelocityY

        if self.bally <= 0:
            self.ballvelocityY *= -1
        if self.bally >= self.gridLength - 1:
            self.ballvelocityY *= -1
        self.allactivateLEDs.append(self.determineLEDPosition(horizontal = 0, vertical = self.leftpongposition - 1))
        self.allactivateLEDs.append(self.determineLEDPosition(horizontal = 0, vertical = self.leftpongposition))
        self.allactivateLEDs.append(self.determineLEDPosition(horizontal = 0, vertical = self.leftpongposition + 1))
        
        self.allactivateLEDs.append(self.determineLEDPosition(horizontal = self.gridWidth - 1, vertical = self.rightpongposition - 1))
        self.allactivateLEDs.append(self.determineLEDPosition(horizontal = self.gridWidth - 1, vertical = self.rightpongposition))
        self.allactivateLEDs.append(self.determineLEDPosition(horizontal = self.gridWidth - 1, vertical = self.rightpongposition + 1))
        
        self.allactivateLEDs.append(self.determineLEDPosition(horizontal = int(round(self.ballx)), vertical = int(round(self.bally))))
        
        for i in range(self.lengthLED):
            led_data = wpilib.AddressableLED.LEDData()
            if i in self.allactivateLEDs:
                led_data.setLED(wpilib.Color.kAzure)
            else:
                led_data.setLED(wpilib.Color.kBlack)
            self.led_buffer.append(led_data)
        self.led.setData(self.led_buffer)
        self.led.start()

        # print("Pong Positions: " + str(self.leftpongposition) + "-" + str(self.rightpongposition))
        # print("Ball Position: " + str(self.ballx) + ", " + str(self.bally))

        return None

    def determineLEDPosition(self, horizontal, vertical):
        if abs(horizontal) >= self.gridWidth:
            return 0
        if abs(vertical) >= self.gridLength:
            return 0

        # print("horizontal = " + str(horizontal) + ", vertical = " + str(vertical))
        if vertical % 2 == 0:
            self.LEDPosition = (self.gridWidth - horizontal) + (vertical * self.gridLength) + list(itertools.accumulate(self.deadspace))[int(vertical)] * 2 + self.internaloffset[int(vertical)]
        else:
            self.LEDPosition = horizontal + (vertical * self.gridLength) + list(itertools.accumulate(self.deadspace))[int(vertical)] * 2 + self.internaloffset[int(vertical)]
        return self.LEDPosition