from time import sleep
from machine import Pin
from neopixel import NeoPixel

# Initialize NeoPixel pin
neopixel_pin = Pin(21, Pin.OUT)

# Initialize NeoPixel object with 32 LEDs
npm = NeoPixel(neopixel_pin, 32)

# Define brightness (255 is full brightness)
on = 255

while True:
    # Set all LEDs to white (full brightness for R, G, B)
    npm.fill((on, on, on))
    npm.write()  # Apply changes
    
    print('LEDs ON')
    sleep(1)  # Wait for 1 second
    
    # Turn off all LEDs (R, G, B set to 0)
    npm.fill((0, 0, 0))
    npm.write()  # Apply changes
    
    print('LEDs OFF')
    sleep(1)  # Wait for 1 second
