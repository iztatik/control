import numpy as np
import control as ct


# System
num = list(map(float,input('Plant numerator: ').split()))
den = list(map(float,input('Plant denominator: ').split()))
G = ct.tf(num, den)
print('Plant:', G)

# Error constant
b0 = num[0]
a1 = den[1]
a0 = den[2]

Kp = b0/a0
print('Position error constant: ', Kp)

# Error
e = 1/(1+Kp)
print('Steady-state error: ', e)