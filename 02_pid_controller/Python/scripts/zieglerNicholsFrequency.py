import numpy as np
import control as ct


# System
num1 = list(map(float,input('Plant numerator: ').split()))
den1 = list(map(float,input('Plant denominator: ').split()))

G = ct.tf(num1, den1)
print('Plant', G)

# System critical period and frequency
Kcr, _, Wcr, _ = ct.margin(G)
Pcr = 2*np.pi/Wcr
print(Kcr, Wcr, Pcr)

# PID computation
Kp = 0.6*Kcr
Ti = 0.5*Pcr
Td = 0.125*Pcr

Gc = ct.tf([Kp*Ti*Td, Kp*Ti, Kp], [Ti, 0])
print('Kp: {a:1.6f}, Ti: {b:1.6f}, Td: {c:1.6f}'.format(a=Kp, b=Ti, c=Td))
