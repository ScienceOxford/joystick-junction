from microbit import *

# Please tag us if used!
# We'd love to see what you make:
# @ScienceOxford

x_road = 2
y_road = 2
b_road = 9
wait_road = 0

def road():
    global x_road, y_road, b_road, wait_road
    display.clear()
    display.set_pixel(x_road, y_road, b_road)
    if wait_road < 2:
        wait_road += 1
    else:
        wait_road = 0
        if y_road == 4:
            y_road = 0
        else:
            y_road += 1

def get_road_pos():
    return x_road, y_road

def get_road_wait():
    return wait_road
