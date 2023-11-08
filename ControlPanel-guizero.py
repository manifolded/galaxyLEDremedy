# Code initiated by ChatGPT when prompted to use guizero
from guizero import App, PushButton, Box, Text
import board
import neopixel
import RainbowAndDerivs
import StarField

touch_width = 800
touch_height = 480
button_width = 30
button_height = 6

num_pixels = 300
my_strip = neopixel.NeoPixel(board.D18, num_pixels, auto_write=False)
loop_iteration_period = 20 # msec

displays = ["none", "rainbow", "galaxy", "starfield"]
galaxy = RainbowAndDerivs.Galaxy()
stars = StarField.Stars()
implementations = [None, None, galaxy.iteration, stars.iteration]
current_display = 0

# Display codes can't be blocking so they have to be some sort of thread. We have to be able 
# to click the terminate button. One main loop isn't very appealing since the codes are so 
# different. Separate loops which terminate on command is more appealing.

def loop_iteration():
    global current_display
    if current_display >= 2:
        implementations[current_display]
        # No drawing is allowed in the display code, so it must get invoked here.
        my_strip.show()
    else:
        my_strip.fill((0,0,0))
        my_strip.show()


def execute_galaxy():
    global current_display
    current_display = 2

def execute_starfield():
    global current_display
    current_display = 3

def terminate_display():
    global current_display
    current_display = 0

app = App("Galaxy LED Control Panel", width=touch_width, height=touch_height)

title_box = Box(app, width=400, height=100, align="top", border=True)
Text(title_box, text="Theme Selection (Galaxy)")

button_box = Box(app, layout="grid")

button1 = PushButton(button_box, text="View the Sea of Galatic Colors", command=execute_galaxy, 
                     width=button_width, height=button_height, grid=[0, 0])
button2 = PushButton(button_box, text="View a Field of Stars", command=execute_starfield,
                     width=button_width, height=button_height, grid=[1, 0])
button3 = PushButton(app, text="Terminate Diplays", command=terminate_display,
                     width=button_width, height=button_height)

# execute main body loop_iteration periodically
app.repeat(loop_iteration_period, loop_iteration())
app.display()


