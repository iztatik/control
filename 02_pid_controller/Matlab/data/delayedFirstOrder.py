#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import identification as idt
import numpy as np
import control as ct
import pandas as pd
import matplotlib.pyplot as plt

# Import and sort the data as a numpy array
data = np.array(pd.read_csv('delayedFirstOrder1.csv', header=None))
t = data[:, 0]
u = data[:, 1]
c = data[:, 2]

# Identification of the system by curve fitting
k, tau, theta =  idt.fopdt(t, u, c)
G = ct.tf([k], [tau, 1])*ct.tf(*ct.pade(theta, 10))

# Step response of the identified system
_, ce = ct.step_response(u[-1]*G, t)

#Plot both responses
plt.plot(t, c, label = 'Raw')
plt.plot(t, ce, label = "Identified")


plt.legend()
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.grid()

plt.show()
