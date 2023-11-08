import time

class Galaxy:

    def __init__(self) -> None:
        self.num_hues = 30
        self.num_pixels = 300
        self.offset_idx = 0
        self.offset_speed = 3

    # Does, of course, compute other colors too, suitably massaged
    def softPlateau(self, hue_value_dec_unit, lower, upper, shoulder_width):
        if hue_value_dec_unit < lower - shoulder_width:
            green = 0.0
        elif hue_value_dec_unit < lower:  # left shoulder
            green = (hue_value_dec_unit - (lower - shoulder_width))/shoulder_width
        elif hue_value_dec_unit < upper:    
            green = 1.0
        elif hue_value_dec_unit < upper + shoulder_width:  # right shoulder
            green = (upper + shoulder_width - hue_value_dec_unit)/shoulder_width
        else:
            green = 0.0
        return green

    def rgbFromHue(self, hue_value_int_rep):
        green = int(255*self.softPlateau(hue_value_int_rep/256, 0.1666, 0.5, 0.1666))
        red = int(255*((self.softPlateau(hue_value_int_rep/256, 0.3333, 0.6666, 0.1666)-1.0)*-1.0))
        blue = int(255*self.softPlateau(hue_value_int_rep/256, 0.5, 0.8333, 0.1666))
        return (red, green, blue)

    def rainbowFrame(self, my_strip):
        global offset_idx
        for pixel_idx in range(self.num_pixels):
            hue_idx = (pixel_idx+offset_idx)%self.num_hues 
            hue_value_int_rep = (hue_idx/self.num_hues)*255
            my_strip[pixel_idx] = self.rgbFromHue(hue_value_int_rep)

    def galaxyHue(self, hue_value_dec_unit):
        return 0.5*hue_value_dec_unit + 0.5

    # Ultimately, galaxy frames should have scattered white pixels?
    #   Mark is as a future task
    def galaxyFrame(self, my_strip):
        global offset_idx
        for pixel_idx in range(self.num_pixels):
            hue_idx = (pixel_idx+offset_idx)%self.num_hues
            hue_value_dec_unit = hue_idx/self.num_hues
            galaxy_hue = self.galaxyHue(hue_value_dec_unit)
            my_strip[pixel_idx] = self.rgbFromHue(galaxy_hue*255)

    # This is the atom that is repeated endlessly to form the display
    # It is to be called from the parent code as the iterations of the loop,
    # thus the absence of a loop here.
    def iteration(self, my_strip):
        global offset_idx
        self.galaxyFrame(my_strip)
        my_strip.show()

        offset_idx += self.offset_speed
        offset_idx = offset_idx%self.num_pixels


