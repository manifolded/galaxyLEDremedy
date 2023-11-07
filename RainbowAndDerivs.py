import time
import board
import neopixel
import sys

num_hues = 30
num_pixels = 300
offset_speed = 3
iteration_wait_ms = 50
terminal_wait_ms = 5000

my_strip = neopixel.NeoPixel(board.D18, num_pixels, auto_write=False, brightness=0.2)


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

try:
    for offset_idx in range(0, num_pixels, offset_speed):
        galaxyFrame(offset_idx, num_pixels, num_hues, my_strip)
        my_strip.show()
        time.sleep(iteration_wait_ms/1000.0)
    my_strip.fill((0,0,0))
    my_strip.show()
except KeyboardInterrupt:
    my_strip.fill((0,0,0))
    my_strip.show()
    sys.exit()