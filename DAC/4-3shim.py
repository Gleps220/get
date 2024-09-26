
import RPi.GPIO as gp
gp.setmode(gp.BCM)
gp.setup(9, gp.OUT)

p = gp.PWM(9, 1000)

try:
    while True:
        K=float(input('Введите коэффициент заполнения: '))
        p.start(K)
        print('Предпологаемое напряжение = ',3.3*K*0.01)

finally:
    p.stop()
    gp.cleanup()