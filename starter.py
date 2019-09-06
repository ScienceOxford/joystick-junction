from microbit import *
from joystick import button_press, joystick_push
from game import road, get_road_pos

# Please tag us if used!
# We'd love to see what you make:
# @ScienceOxford

x = 0
y = 0
b = 9

while True:
    sleep(200)
    road()
    display.set_pixel(x, y, b)
    button = button_press()
