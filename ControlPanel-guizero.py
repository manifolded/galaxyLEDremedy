# Code initiated by ChatGPT when prompted to use guizero
from guizero import App, PushButton, Box, Text
import subprocess

touch_width = 800
touch_height = 480
button_width = 30
button_height = 6

def execute_rainbow():
    subprocess.run(["python", "./RainbowAndDerivs.py"])

def execute_starfield():
    subprocess.run(["python", "./StarField.py"])

app = App("Galaxy LED Control Panel", width=touch_width, height=touch_height)

title_box = Box(app, width=400, height=100, align="top", border=True)
Text(title_box, text="Theme Selection (Galaxy)")

button_box = Box(app, layout="grid")

button1 = PushButton(button_box, text="View the Sea of Galatic Colors", command=execute_rainbow, 
                     width=button_width, height=button_height, grid=[0, 0])
button2 = PushButton(button_box, text="View a Field of Stars", command=execute_starfield,
                     width=button_width, height=button_height, grid=[1, 0])

app.display()
