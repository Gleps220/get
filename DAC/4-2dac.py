import RPi.GPIO as gp
import time 

def binary(x):
    if x<=255:
        return [int(i) for i in bin(x)[2:].zfill(8)]
    else : 
        return ValueError

gp.setmode(gp.BCM)
dac=[8,11,7,1,0,5,12,6]
gp.setup(dac,gp.OUT)

T=float(input('Введите период сигнала в секундах: '))
try:
    while True:
        for i in range(256):
            gp.output(dac,binary(i))
            time.sleep(T/510)
            print(i/255*3.3)
        for i in range(255,0,-1):
            gp.output(dac,binary(i))
            time.sleep(T/510)
            print(i/255*3.3)

finally:
    gp.output(dac,0)
    gp.cleanup()