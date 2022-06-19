#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import control as ct
import itresp as ite
import matplotlib.pyplot as plt

# Parameters
tsim = 15
dt = 0.01
t = np.arange(0, tsim, dt)
r = np.ones(len(t))

# Plant
num1 = [1]
den1 = [1, 7, 12, 0]
G = ct.tf(num1, den1)

# Controller
Kp = 50.4
Ti = 0.9069
Td = 0.2267
Gc = ct.tf([Kp*Ti*Td, Kp*Ti, Kp], [Ti, 0])

# Closed-loop system
sys = ct.feedback(Gc*G)
_, c1 = ct.forced_response(sys, t, r)

# Step-by-step response
c2, u, e, i = ite.continuous_response(G, t, r, Kp, Ti, Td, 12, antiwindup='conditional')

# PLot
plt.plot(t, c1)
plt.plot(t, c2)
plt.show()
