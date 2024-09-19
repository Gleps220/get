import RPi.GPIO as gp
import time 

gp.setmode(gp.BCM)

leds=[2,3,4,17,27,22,10,9]
aux=[21,20,26,16,19,25,23,24]
gp.setup(leds,gp.OUT)
gp.setup(aux,gp.IN)
while True:
    for i in range(len(aux)):
        if gp.input(aux[i])==1:
            gp.output(leds[i],1)
        else:
            gp.output(leds[i],0)
gp.cleanup()