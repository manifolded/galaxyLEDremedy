from HueToRGB import rgbFromHue
class Rainbow:
    def __init__(self) -> None:
        self.num_hues = 30
        self.num_pixels = 300
        self.offset_idx = 0
        self.offset_speed = 3

    def rainbowFrame(self, my_strip):
        global offset_idx
        for pixel_idx in range(self.num_pixels):
            hue_idx = (pixel_idx+offset_idx)%self.num_hues 
            hue_value_int_rep = (hue_idx/self.num_hues)*255
            my_strip[pixel_idx] = rgbFromHue(hue_value_int_rep)

    # This is the atom that is repeated endlessly to form the display
    # It is to be called from the parent code as the iterations of the loop,
    # thus the absence of a loop here.
    def iteration(self, my_strip):
        self.rainbowFrame(my_strip)
        my_strip.show()

        self.offset_idx += self.offset_speed
        self.offset_idx = self.offset_idx%self.num_pixels


