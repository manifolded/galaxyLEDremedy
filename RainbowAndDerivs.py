import time

num_hues = 30
num_pixels = 300
offset_idx = 0
offset_speed = 3

def softPlateau(unitHue, lower, upper, shoulder_width):
    if unitHue < lower - shoulder_width:
        green = 0.0
    elif unitHue < lower:  # left shoulder
        green = (unitHue - (lower - shoulder_width))/shoulder_width
    elif unitHue < upper:    
        green = 1.0
    elif unitHue < upper + shoulder_width:  # right shoulder
        green = (upper + shoulder_width - unitHue)/shoulder_width
    else:
        green = 0.0
    return green

def rgbFromHue(octalHue):
    green = int(255*softPlateau(octalHue/256, 0.1666, 0.5, 0.1666))
    red = int(255*((softPlateau(octalHue/256, 0.3333, 0.6666, 0.1666)-1.0)*-1.0))
    blue = int(255*softPlateau(octalHue/256, 0.5, 0.8333, 0.1666))
    return (red, green, blue)

def rainbowFrame(offset_idx, num_pixels, num_hues, my_strip):
    for pixel_idx in range(num_pixels):
        hue_idx = (pixel_idx+offset_idx)%num_hues 
        octalHue = (hue_idx/num_hues)*255
        my_strip[pixel_idx] = rgbFromHue(octalHue)

def galaxyHue(unitHue):
    return 0.5*unitHue + 0.5

# Ultimately galaxy frames should have scattered white pixels?
def galaxyFrame(offset_idx, num_pixels, num_hues, my_strip):
    for pixel_idx in range(num_pixels):
        hue_idx = (pixel_idx+offset_idx)%num_hues
        unitHue = hue_idx/num_hues
        galaxy_hue = galaxyHue(unitHue)
        my_strip[pixel_idx] = rgbFromHue(galaxy_hue*255)


def iteration(my_strip):
    galaxyFrame(offset_idx, num_pixels, num_hues, my_strip)
    my_strip.show()

    offset_idx += offset_speed
    offset_idx = offset_idx%num_pixels


