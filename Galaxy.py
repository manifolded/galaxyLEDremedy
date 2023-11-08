import HueToRGB

class Galaxy:
    def __init__(self) -> None:
        self.num_hues = 30
        self.num_pixels = 300
        self.offset_idx = 0
        self.offset_speed = 3

    def galaxyHue(self, hue_value_dec_unit):
        return 0.5*hue_value_dec_unit + 0.5

    # Ultimately, galaxy frames should have scattered white pixels?
    #   Mark is as a future task
    def galaxyFrame(self, my_strip):
        for pixel_idx in range(self.num_pixels):
            hue_idx = (pixel_idx+self.offset_idx)%self.num_hues
            hue_value_dec_unit = hue_idx/self.num_hues
            galaxy_hue = self.galaxyHue(hue_value_dec_unit)
            my_strip[pixel_idx] = HueToRGB.rgbFromHue(galaxy_hue*255)

    # This is the atom that is repeated endlessly to form the display
    # It is to be called from the parent code as the iterations of the loop,
    # thus the absence of an explicit loop here.
    def iteration(self, my_strip):
        self.galaxyFrame(my_strip)
        my_strip.show()

        self.offset_idx += self.offset_speed
        self.offset_idx = self.offset_idx%self.num_pixels


