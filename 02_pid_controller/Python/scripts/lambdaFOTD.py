import numpy as np
import control as ct
import matplotlib.pyplot as plt

# Get the data from the user
K = float(input('System gain (K): '))
T = float(input('System time constant (T): '))
td = float(input('System time delay (td): '))

# Type of sintonization
print('Select a tuning type: ')
print('1 -  Robust')
print('2 -  Agressive')
print('3 -  Custom')
L = input('Type: ')

if L == '1':
    L = 3*T
elif L =='2':
    L = T
elif L == '3':
    L = float(input('Lambda: '))
else:
    print('Error: Incorrect value...')        
    
# PD controller tuning
Kp = T/(K*(td + L))
Ti = T

# Results
print(f'Kp: {Kp}, Ti:{Ti}')

# Plot systems
G = ct.tf([K], [T, 1])*ct.tf(*ct.pade(td, 10))
Gc = ct.tf([Kp*Ti, Kp], [Ti, 0])

sys = ct.feedback(Gc*G)

t1, C1 = ct.step_response(G)
t2, C2 = ct.step_response(sys)

plt.plot(t1, C1, label = 'FOTD')
plt.plot(t2, C2, label = 'Controlled')
plt.legend()
plt.grid()
