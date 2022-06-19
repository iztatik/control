import control as ct
import cmath


# System
num = list(map(float,input('Plant numerator: ').split()))
den = list(map(float,input('Plant denominator: ').split()))
G = ct.tf(num, den)
print('System: ', G)

# Evaluation
s = complex(input('s = '))
Gev = ct.evalfr(G, s)
print('Evaluation: ',Gev)

# Magnitude and angle
print('Magnitude: ', abs(Gev))
print('Angle: ', cmath.phase(Gev))