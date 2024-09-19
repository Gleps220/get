import RPi.GPIO as gp
import time 

gp.setmode(gp.BCM)
gp.setup(14,gp.OUT)
gp.setup(4,gp.IN)
k=0
while k<20:
    if gp.input(4)==True:
        gp.output(14,1)
    else:
        gp.output(14,0)
    time.sleep(1)
    k+=1