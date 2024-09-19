import RPi.GPIO as gp
import time 

gp.setmode(gp.BCM)

dac=[8, 11,7,1,0,5,12,6]
number=[1,0,0,0,0,0,0,0]
gp.setup(dac,gp.OUT)
gp.output(dac,number)
time.sleep(15)
gp.cleanup()
