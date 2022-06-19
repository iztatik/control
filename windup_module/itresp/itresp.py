#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import control as ct
import matplotlib.pyplot as plt


def continuous_response(sys, t, r, Kp = 1, Ti = float('inf'), Td = 0,  lim= float('inf'), antiwindup=None):
    """
    Performs a step-by-step response for a continuous-time system considering or not the Windup effect, a PID controller and an Anti-windup action.

    Parameters
    ----------
    sys : control.TransferFunction
        System's transfer function.
    t : Numpy array
        Time.
    r : Numpy array
        Input signal.
    Kp : Float, optional
        Proportional gain. The default is 1.
    Ti : Float, optional
        Integral time. The default is float('inf').
    Td : Float, optional
        Derivative time. The default is 0.
    lim : Float, optional
        Windup limit (Simetric). The default is float('inf').
    antiwindup : String, optional
        'conditional', 'discharge'. The default is None.

    Returns
    -------
    c : Numpy array
        System's response.
    u : Numpy array
        Control signal.
    e : Numpy array
        Error signal.
    it : Numpy array
        Integral action signal.

    """
    
    # Conver to space states to allow initial conditions
    Gss = ct.tf2ss(sys)

    # Get the time step
    dt = t[1]-t[0]

    # Initial conditions
    x0 = np.zeros(len(sys.pole()))

    # Accumulated system response
    c = np.zeros(len(t))

    # Accumulated limited control signal
    u = np.zeros(len(t))
    
    # Accumulated unlimited control signal
    v = np.zeros(len(t))

    # Accumulated error
    e = np.zeros(len(t))
    
    # Accumulated integral 
    it = np.zeros(len(t))
        
    # Initial value of I
    I = 0
    
    # Conditional discharge constant
    Tt = np.sqrt(Ti*Td)

    for i, ti in enumerate(t):
        # Instantaneous error
        e_i = r[i] - c[i-1]

        # Controller considering windup effect
        P = Kp*e_i
        D = Kp*Td*(e_i - e[i-1])/dt
        
        # Integral action considering anti-windup
        if antiwindup == None or (antiwindup == 'conditional' and -lim < v[i-1] < lim):
            I = I + dt*Kp*e_i/Ti
        elif antiwindup == 'discharge':
            es_i = u[i-1] - v[i-1]
            I = I + dt*(Kp*e_i/Ti + es_i/Tt)
        
        v_i = P + I + D
        u_i = max(min(v_i, lim), -lim)

        # System response
        _, Ci, Xi = ct.forced_response(Gss, [ti-dt, ti], [u_i, u_i], X0=x0, return_x=True)

        # Save results
        c[i] = np.squeeze(Ci[-1])
        x0 = np.squeeze(Xi[:, -1])
        e[i] = e_i
        u[i] = u_i
        v[i] = v_i
        it[i] = I

    return c, u, e, it



def discrete_response(sys, t, r, Kp = 1, Ti = float('inf'), Td = 0,  lim= float('inf'), antiwindup=None):
    """
    Performs a step-by-step response for a discrete-time system considering or not the Windup effect, a PID controller and an Anti-windup action.

    Parameters
    ----------
    sys : control.TransferFunction
        System's transfer function.
    t : Numpy array
        Time.
    r : Numpy array
        Input signal.
    Kp : Float, optional
        Proportional gain. The default is 1.
    Ti : Float, optional
        Integral time. The default is float('inf').
    Td : Float, optional
        Derivative time. The default is 0.
    lim : Float, optional
        Windup limit (Simetric). The default is float('inf').
    antiwindup : String, optional
        'conditional'. The default is None.

    Returns
    -------
    c : Numpy array
        System's response.
    u : Numpy array
        Control signal.
    e : Numpy array
        Error signal.
    it : Numpy array
        Integral action signal.

    """
    
    
    # Conver to space states to allow initial conditions
    Gss = ct.tf2ss(sys)

    # Get the time step
    dt = t[1]-t[0]
    
    # Sample time
    ts = dt

    # Initial conditions
    x0 = np.zeros(len(sys.pole()))

    # Accumulated system response
    c = np.zeros(len(t))

    # Accumulated limited control signal
    u = np.zeros(len(t))
    
    # Accumulated unlimited control signal
    v = np.zeros(len(t))

    # Accumulated error
    e = np.zeros(len(t))
    
    # Accumulated integral 
    it = np.zeros(len(t))
        
    # Initial value of I
    I = 0
    
    # Discrete coeficients
    b0 = Kp*(1 + (ts/(2*Ti)) + (Td/ts))
    b1 = -Kp*(1 - (ts/(2*Ti)) + (2*Td/ts))
    b2 = Kp*Td/ts
    
    print('Digital PID coefficients: ')
    print('b0:{a:1.4f}, b1:{b:1.4f}, b2:{c:1.4f} '.format(a=b0, b=b1, c=b2))

    for i, ti in enumerate(t):
        # Instantaneous error
        e_i = r[i] - c[i-1]

        # Controller considering windup effect
        v_i = b0*e_i + b1*e[i-1] + b2*e[i-2] + v[i-1]
        
        # Control action considering anti-windup
        if antiwindup == 'conditional':
            v_i = max(min(v_i, lim), -lim)
        
        u_i = max(min(v_i, lim), -lim)

        # System response
        _, Ci, Xi = ct.forced_response(Gss, [ti-dt, ti], [u_i, u_i], X0=x0, return_x=True)

        # Save results
        c[i] = np.squeeze(Ci[-1])
        x0 = np.squeeze(Xi[:, -1])
        e[i] = e_i
        u[i] = u_i
        v[i] = v_i
        it[i] = I

    return c, u, e, it

