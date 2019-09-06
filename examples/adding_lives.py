from microbit import *
from joystick import button_press, joystick_push
from game import road, get_road_pos

# Please tag us if used!
# We'd love to see what you make:
# @ScienceOxford

x = 0
y = 0
b = 9
lives = 9

while True:
    if lives > 0:
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
        road_location = get_road_pos()
        pixel_location = x, y
        if pixel_location == road_location:
            lives -= 1
    else:        
        display.show(Image.NO)
