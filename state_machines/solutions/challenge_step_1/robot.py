#!/usr/bin/env python3
#
# Copyright (c) FIRST and other WPILib contributors.
# Open Source Software; you can modify and/or share it under the terms of
# the WPILib BSD license file in the root directory of this project.
#

import wpilib
from raptacon3200.utils.leds import Strip

class MyRobot(wpilib.TimedRobot):
    """Main robot class"""

    def robotInit(self):
        """Robot-wide initialization code should go here"""
        self.kLEDBuffer = 20
        self.breakbeam = wpilib.DigitalInput(0)
        self.leds = wpilib.AddressableLED(0)
        self.ledData = [wpilib.AddressableLED.LEDData() for _ in range(self.kLEDBuffer)]
        self.strip = Strip(self.ledData, "Ken")
        self.currentHue = 243
        self.currentBright = 0
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
        self.smartdashboard = wpilib.SmartDashboard
        self.smartdashboard.putBoolean("BreakBeam", self.breakbeam.get())

        # Set the LEDs
        self.leds.setData(self.ledData)

        if self.breakbeam.get():
            self.strip.periodic()
        else:
            pass