import RPi.GPIO as gp
import time 

def binary(x):
    return [int(i) for i in bin(x)[2:].zfill(8)]

gp.setmode(gp.BCM)
dac=[8,11,7,1,0,5,12,6]
gp.setup(dac,gp.OUT)

try:

    while True:
        x=float(input('Введите число от 0 до 255: '))
        z=int(x)
        gp.output(dac,binary(z))
        print('Предпологаемое напряжение: ', x/255*3.3,' В')
except:
    print('Некорректное значение...')


finally:
    gp.output(dac,0)
    gp.cleanup()
