import control as ct

# Inputs
Kp = float(input('Kp: '))
Ti = float(input('Ti: '))
Td = float(input('Td: '))
ts = float(input('Ts: '))

pid = ct.tf([Kp*Ti*Td, Kp*Ti, Kp],[Ti, 0])

print('Transfer function: ')
print(pid)

# Equations
b0 = Kp*(1 + (ts/(2*Ti)) + (Td/ts))
b1 = -Kp*(1 - (ts/(2*Ti)) + (2*Td/ts))
b2 = Kp*Td/ts

print('Coefficients:')
print('b0: {a:1.4f}, b1: {b:1.4f},b2: {c:1.4f} '.format(a=b0, b=b1, c=b2))
