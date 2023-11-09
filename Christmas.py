import board
import neopixel

class Christmas:
    def __init__(self) -> None:
        self.num_pixels = 300
        self.block_size = 80
        self.offset_idx = 0
        self.offset_speed = 6
        self.a_rgb = (255, 0, 0)
        self.b_rgb = (0, 255, 0)

    def genFrame(self, my_strip):
        for pixel_idx in range(0, self.num_pixels):
            # Mod 2 restricts us to two colors, red and white
            pixel_value = self.a_rgb if (pixel_idx + self.offset_idx)%self.block_size%2 == 0 else self.b_rgb
            my_strip[pixel_idx] = pixel_value
        

    # This is the atom that is repeated endlessly to form the display
    # It is to be called from the parent code as the iterations of the loop,
    # thus the absence of a loop here.
    def iteration(self, my_strip):
        self.genFrame(my_strip)
        my_strip.show()

        self.offset_idx += self.offset_speed
        self.offset_idx = self.offset_idx%self.num_pixels
