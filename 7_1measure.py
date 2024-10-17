import RPi.GPIO as gp
import time 
from matplotlib import pyplot as pl

#Функция для перевода в двоичную СС
def binary(x):
    return [int(i) for i in bin(x)[2:].zfill(8)]

#Функция для АЦП
def adc():
    summ=0
    kvant=0.03
    for b in range(7,-1,-1):
        gp.output(dac,binary(2**b+summ))
        time.sleep(kvant)
        if gp.input(comp)!=1:
            summ+=2**b         
    return summ

#ОбЪявление пинов входа и выхода
gp.setmode(gp.BCM)
dac=[8,11,7,1,0,5,12,6]
leds=[2,3,4,17,27,22,10,9]
comp=14
troyka=13
gp.setup(dac,gp.OUT)
gp.setup(leds,gp.OUT)
gp.setup(comp,gp.IN)


results=[] #список для хранения результатов
one=time.time()
gp.setup(troyka,gp.OUT,initial=gp.HIGH)
try:
   
    #Подаем напряжение на тройка-модуль и проводим измерения пока он не зарядится до 80 процентов

    sleep_time=0.1
    while True:
        i=adc()
        U=i/255*3.3
        results.append(U)
        print('Зарядка конденсатора ',i,'Nапряжение: ', U,' В')
        if U>3.3*0.8:
            two=time.time()
            break
        gp.output(leds,binary(i))

    #Установливаем 0В на выход тройка-модуля и проводим измеренияБ пока конденсатор не разрядится до 2%

    gp.setup(troyka,gp.OUT,initial=gp.LOW)
    while True:
        i=adc()
        U=i/255*3.3
        results.append(U)
        print('Разрядка конденсатора ',i,'Nапряжение: ', i/255*3.3,' В')
        if U<3.3*0.02:
            three=time.time()
            break


        gp.output(leds,binary(i))
#   
    print('Общая продолжительность эксперемента: '+str(three-one))
    print('Время зарядки конденсатора: '+str(two-one))
    print('Время разрядки конденсатора: '+str(three-two))
    print('Период одного измерения: '+ str( (three-one)/len(results)))
    print('Шаг квантования АЦП: 0.03 sec')

    with open('/home/b03-401/Gleps/7/data.txt','w') as data:
        data.write('\n'.join([str(i) for i in results]))

#Запись параметров эксперимента

    with open('/home/b03-401/Gleps/7/settings.txt','w') as settings:
        settings.write('Общая продолжительность эксперемента: '+str(three-one)+'\n')
        settings.write('Период одного измерения: '+ str( (three-one)/len(results))+'\n')
        settings.write('Средняя частота дискретизации проведенных измерений: '+str(0.03*8)+'\n')
        settings.write('Шаг квантования АЦП: 0.03 sec')

#Построени графика по результатам эксперимента

    pl.plot(results)
    pl.show()

finally:
    gp.output(dac,0)
    gp.output(leds,0)
    gp.output(troyka,0)
    gp.cleanup()     




       

