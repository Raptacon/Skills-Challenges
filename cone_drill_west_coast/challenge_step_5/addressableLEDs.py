
self.potato = 5
self.led = wpilib.AddressableLED(9)
self.led.setLength(24)
led_buffer = []
while self.potato > 0:
    for i in range(24):
        led_data = wpilib.AddressableLED.LEDData()
        led_data.setLED(wpilib.Color.kRed)
        # d_data.setRGB(255, 0, 0)
        led_buffer.append(led_data)
        self.potato -= 5
self.led.setData(led_buffer)
self.led.start()
self.led.setData(led_buffer)
sleep(1)
self.led.setData(led_buffer)
led_buffer = []

while self.potato < 0:
    for i in range(24):
        led_data = wpilib.AddressableLED.LEDData()
        led_data.setLED(wpilib.Color.kAzure)
        # d_data.setRGB(0, 0, 255)
        led_buffer.append(led_data)
        self.potato += 5

self.led.setData(led_buffer)
self.led.start()
sleep(1)
