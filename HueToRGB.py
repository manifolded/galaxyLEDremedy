# Computes a single curve (plateau) that describes the unit green contribution
# for any given unit hue. Does, of course, compute other colors too, suitably 
# massaged.
def softPlateau(hue_value_dec_unit, lower, upper, shoulder_width):
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

# Magic numbers extracted from the features of the following image which relates
# the unit hue with the unit rgb's.
# https://en.wikipedia.org/wiki/Color_gradient#/media/File:Gnuplot_HSV_gradient.png
def rgbFromHue(hue_value_int_rep):
    green = int(255*softPlateau(hue_value_int_rep/256, 0.1666, 0.5, 0.1666))
    red = int(255*((softPlateau(hue_value_int_rep/256, 0.3333, 0.6666, 0.1666)-1.0)*-1.0))
    blue = int(255*softPlateau(hue_value_int_rep/256, 0.5, 0.8333, 0.1666))
    return (red, green, blue)
