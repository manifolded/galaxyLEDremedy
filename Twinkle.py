import board
import neopixel
import random
import time

num_pixels = 300
my_strip = neopixel.NeoPixel(board.D18, num_pixels, auto_write=False)
loop_iteration_period = 20 # msec

# Random brightness assigned to every pixel, updated periodically

def twinkleFrame(my_strip):
    for pixel_idx in range(0, num_pixels):
        red = random.randint(0, 255)
        my_strip[pixel_idx] = (red, red, red) # to get white


def iteration(my_strip):
    twinkleFrame(my_strip)
    my_strip.show()
    time.sleep(loop_iteration_period/1000.0)

while True:
    iteration(my_strip)




