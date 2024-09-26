import RPi.GPIO as gp
import time 

def binary(x):
    return [int(i) for i in bin(x)[2:]]
print(binary(10))
