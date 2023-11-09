import random

# Random brightness assigned to every pixel, updated periodically
class Flare:
    def __init__(self) -> None:
        self.num_pixels = 300
        # With this approach the stars never seem to go out at all.
        # The simple solution may be to clip the low end of the 
        # brightness value.
        self.dark_threshold = 0.99
        self.max_brightness = 128

    def genFrame(self, my_strip):
        for pixel_idx in range(0, self.num_pixels):
            red = 0 if random.uniform(0., 1.) < self.dark_threshold else random.randint(0, self.max_brightness)
            my_strip[pixel_idx] = (red, red, red) # 3x repeat to get white

    def iteration(self, my_strip):
        self.genFrame(my_strip)
        my_strip.show()


