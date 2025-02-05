from gpiozero import LED
from time import sleep

red = LED(17)

try:
    while True:
        red.on()
        print("Red Light On")
        sleep(1)
        red.off()
        print("Red Light Off")
        sleep(1)
except KeyboardInterrupt:
    red.off()
    print("Program Ended")
