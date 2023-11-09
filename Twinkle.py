import board
import neopixel
import random
import time

num_pixels = 300
my_strip = neopixel.NeoPixel(board.D18, num_pixels, auto_write=False)
loop_iteration_period = 20 # msec
dark_threshold = 0.99
max_brightness = 128

# Random brightness assigned to every pixel, updated periodically

# With this approach the stars never seem to go out at all.
# The simple solution may be to clip the low end of the 
# brightness value.


def twinkleFrame(my_strip):
    for pixel_idx in range(0, num_pixels):
        red = 0 if random.uniform(0., 1.) < dark_threshold else random.randint(0, max_brightness)
        my_strip[pixel_idx] = (red, red, red) # to get white


def iteration(my_strip):
    twinkleFrame(my_strip)
    my_strip.show()
    time.sleep(loop_iteration_period/1000.0)


duration = 10.0
start_time = time.time()
while time.time() - start_time < duration:
    iteration(my_strip)
my_strip.fill((0,0,0))
my_strip.show()



