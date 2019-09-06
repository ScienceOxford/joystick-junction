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
    sleep(150)
    road()
    display.set_pixel(x, y, b)
    joystick = joystick_push()
    button = button_press()
    if joystick[1] < 516 and y < 4:
        y += 1
    if joystick[1] > 536 and y > 0:
        y -= 1
    if joystick[0] > 519 and x < 4:
        x += 1
    if joystick[0] < 499 and x > 0:
        x -= 1
