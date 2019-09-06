from microbit import *
from joystick import joystick_push

# Please tag us if used!
# We'd love to see what you make:
# @ScienceOxford

while True:
    joystick = joystick_push()
    print(joystick)
    
    if joystick[0] > 519:   # replace 519 with x + 10
        display.show(Image.ARROW_E)
        
    if joystick[0] < 499:   # replace 499 with x - 10
        display.show(Image.ARROW_W)
        
    if joystick[1] > 536:   # replace 536 with y + 10
        display.show(Image.ARROW_N)
        
    if joystick[1] < 516:   # replace 516 with y - 10
        display.show(Image.ARROW_S)
        
    else:
        display.clear()
    sleep(500)
