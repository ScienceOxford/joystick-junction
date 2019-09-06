from microbit import *
from joystick import button_press
from game import road

# Please tag us if used!
# We'd love to see what you make:
# @ScienceOxford

x = 0
y = 0
b = 9
pause = False

while True:
    if pause is False:
        sleep(150)
        road()
        display.set_pixel(x, y, b)
        button = button_press()
        if button == 'C' and y < 4:
            y += 1
        if button == 'A' and y > 0:
            y -= 1
        if button == 'B' and x < 4:
            x += 1
        if button == 'D' and x > 0:
            x -= 1
        if button == 'F':
            pause = True
    else:
        display.show(Image.TARGET)
        button = button_press()
        if button == 'E':
            pause = False
