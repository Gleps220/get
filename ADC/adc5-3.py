import RPi.GPIO as gp
import time 

def binary(x):
    return [int(i) for i in bin(x)[2:].zfill(8)]

def adc():
    for i in range(255):
        gp.output(dac,binary(i))
        time.sleep(0.002)
        if gp.input(comp)==1:
            break
    return i
            
gp.setmode(gp.BCM)
dac=[8,11,7,1,0,5,12,6]
leds=[2,3,4,17,27,22,10,9]
comp=14
troyka=13
gp.setup(dac,gp.OUT)
gp.setup(leds,gp.OUT)
gp.setup(comp,gp.IN)
gp.setup(troyka,gp.OUT,initial=gp.HIGH)

try:
    pred=-1
    while True:
        i=adc()
        print(i,'Nапряжение: ', i/255*3.3,' В')
        time.sleep(0.1)
        if pred==i:
            continue
        else:
            gp.output(leds,binary(i))


finally:
    gp.output(dac,0)
    gp.output(troyka,0)
    gp.cleanup()