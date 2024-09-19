import RPi.GPIO as gp
import time 

gp.setmode(gp.BCM)
leds=[2,3,4,17,27,22,10,9]
gp.setup(leds,gp.OUT)
for i in range(3):
    for z in leds:
        gp.output(z,1)
        time.sleep(0.2)
        gp.output(z,0)
gp.cleanup()