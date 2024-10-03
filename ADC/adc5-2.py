import RPi.GPIO as gp
import time 

def binary(x):
    return [int(i) for i in bin(x)[2:].zfill(8)]

def adc():
    summ=0
    for b in range(7,-1,-1):
        gp.output(dac,binary(2**b+summ))
        time.sleep(0.003)
        if gp.input(comp)!=1:
            summ+=2**b         
    return summ
            
gp.setmode(gp.BCM)
dac=[8,11,7,1,0,5,12,6]
comp=14
troyka=13
gp.setup(dac,gp.OUT)
gp.setup(comp,gp.IN)
gp.setup(troyka,gp.OUT,initial=gp.HIGH)
try:

    while True:      
        i=adc()
        print(i,'Nапряжение: ', i/255*3.3,' В')
        time.sleep(0.1)
finally:
    gp.output(dac,0)
    gp.output(troyka,0)
    gp.cleanup()