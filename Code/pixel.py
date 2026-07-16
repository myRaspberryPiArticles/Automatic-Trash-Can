import board
import neopixel
from time import sleep

green = (255, 0, 0, 0)
red = (0, 255, 0, 0)
white = (0, 0, 0, 255)
off = (0, 0 ,0 ,0)

# 1. Setup: Change to the number of LEDs in your ring (usually 12, 16, or 24)
num_pixels = 16 

# 2. Pin: Using GPIO 10
pixel_pin = board.D10

# 3. Create the pixels object with the RGBW order
# This is the "Solid and Reliable" fix you need!
pixels = neopixel.NeoPixel(
    pixel_pin, 
    num_pixels, 
    brightness=0.3, # between 0 and 1
    auto_write=True, 
    pixel_order=neopixel.RGBW  # This tells the Pi to send 4 bits of data per LED
)

if __name__ == "__main__":
    # 4. Set a solid color
    # The format is (Green, Red, Blue, White)
    print("ready and waiting")
    pixels.fill((255, 0, 0, 0))
    sleep(3)
    print("flashlight")
    pixels.fill((0, 0, 0, 255))
    sleep(1)
    print("busy")
    pixels.fill((0, 255, 0, 0))
    sleep(10)

    # This sets Red, Green, Blue, and White all to zero
    pixels.fill((0, 0, 0, 0))
    print("off")

