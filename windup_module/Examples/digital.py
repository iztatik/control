#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import control as ct
import itresp as ite
import matplotlib.pyplot as plt

# Parameters
tsim = 0.1
dt = 0.0005
t = np.arange(0, tsim, dt)
r = 4*np.ones(len(t))

# Plant
num1 = [29870]
den1 = [1, 414.7, 33610]
G = ct.tf(num1, den1)

# Controller
Kp = 3.84808815
Ti = 0.00711849
Td = 0
Gc = ct.tf([Kp*Ti*Td, Kp*Ti, Kp], [Ti, 0])

# Closed-loop system
sys = ct.feedback(Gc*G)
_, c1 = ct.forced_response(sys, t, r)

# Step-by-step response
c2, u, e, i = ite.discrete_response(G, t, r, Kp, Ti, Td, 12, antiwindup='conditional')

# PLot
plt.plot(t, c1)
plt.plot(t, c2)
plt.show()
