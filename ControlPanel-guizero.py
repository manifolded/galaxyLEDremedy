# Code initiated by ChatGPT when prompted to use guizero
from guizero import App, PushButton, Box, Text
import board
import neopixel
import Rainbow
import Galaxy
import StarField
import time
import sys

touch_width = 800
touch_height = 480
button_width = 30
button_height = 6

num_pixels = 300
my_strip = neopixel.NeoPixel(board.D18, num_pixels, auto_write=False)
loop_iteration_period = 20 # msec

rainbow = Rainbow.Rainbow()
galaxy = Galaxy.Galaxy()
stars = StarField.Stars()
# displays = ["none", "rainbow", "galaxy", "starfield"]
# implementations = [None, None, galaxy.iteration(), stars.iteration]
current_display = 0

# Display codes can't be blocking so they have to be some sort of thread. We have to be able 
# to click the terminate button. One main loop isn't very appealing since the codes are so 
# different. Separate loops which terminate on command is more appealing.
def loop_body_iteration():
    global current_display
    global my_strip
    if current_display == 1:
        rainbow.iteration(my_strip)
    elif current_display == 2:
        galaxy.iteration(my_strip)
    elif current_display == 3:
        stars.iteration(my_strip)
    else:
        my_strip.fill((0,0,0))
        # freezes, but does not clear, despite what this implies
    my_strip.show()

def execute_rainbow():
    global current_display
    current_display = 1

def execute_galaxy():
    global current_display
    current_display = 2

def execute_starfield():
    global current_display
    current_display = 3

def terminate_display():
    global current_display
    current_display = 0

def quit_panel():
    terminate_display()
    my_strip.fill((0,0,0))
    my_strip.show()
    app.destroy()
    sys.exit()

app = App("Galaxy LED Control Panel", width=touch_width, height=touch_height)

title_box = Box(app, width=400, height=50, align="top", border=True)
Text(title_box, text="Theme Selection (Galaxy)")

button_box = Box(app, layout="grid")
op_box = Box(app, layout="grid")
button1 = PushButton(button_box, text="View the Sweeping Rainbow", command=execute_rainbow,
                     width=button_width, height=button_height, grid=[0, 0])
button2 = PushButton(button_box, text="View the Sea of Galatic Colors", command=execute_galaxy, 
                     width=button_width, height=button_height, grid=[1, 0])
button3 = PushButton(button_box, text="View a Field of Stars", command=execute_starfield,
                     width=button_width, height=button_height, grid=[2, 0])
button4 = PushButton(op_box, text="Terminate Diplays", command=terminate_display,
                     width=button_width, height=button_height, grid=[0, 0])
button5 = PushButton(op_box, text="Quit this Control Panel", command=quit_panel,
                     width=button_width, height=button_height, grid=[1, 0])

# execute main body loop iteration periodically
null_text = Text(app, text="1")
null_text.repeat(loop_iteration_period, lambda: loop_body_iteration())
app.display()


