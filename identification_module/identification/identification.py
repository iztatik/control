import numpy as np
import control as ct
from scipy import signal as sig
from scipy import optimize as opt
import warnings

warnings.filterwarnings('ignore', message='invalid value encountered in true_divide')


def firstOrder(time, din, dout, p0 = [1.0, 1.0]):
    """
    
    Identification of a first order system.
    
    Parameters
    ----------
    time : numpy array
        Time array.
    din : TYPE
        Input signal data.
    dout : numpy array
        System response data.
    p0 : float list, optional
        Initial guess . The default is [k, T] = [1.0, 1.0].

    Returns
    -------
    k : float
        System's gain.    
    Wn : float
        System's time constant.

    """
    
    def first_order_mdl(t, k, T):
        my_tf = sig.TransferFunction(k, [T, 1])
        to, yo, xo = sig.lsim2(my_tf, U=din, T=time)
        return yo
    
    params, params_cov = opt.curve_fit(first_order_mdl, time, dout, method='lm', maxfev=1000, p0=p0)

    # Step response
    k = params[0]
    T = params[1]
    G = ct.tf([k], [T, 1])
    _, c = ct.step_response(din[-1]*G, time)
    
    # Mean Absolute Percent Error (MAPE)
    mape = np.mean(np.abs(np.nan_to_num((dout-c)/dout, False, 0)))*100;
    
    # Show results
    print()
    print('First order identification:')
    print('    Mean Absolute Percent Error: {:.4f}%'.format(mape))
    print('    k: {:.6f}, T: {:.6f} '.format(k, T))
    print()    

    # k, T
    return  params[0], params[1]


def fopdt(time, din, dout, method = 'smith'):
    """
    Identification of a first order plus delayed time system.

    Parameters
    ----------
    time : numpy array
        Time array.
    din : TYPE
        Input signal data.
    dout : numpy array
        System response data.
    mtd : Algorithm, optional
        smith - Smithś method, sk - Sundaresan&Krishnaswamy method. The default is 'smith'.

    Returns
    -------
    k : float
        Systems gain.
    tau : float
        System's time constant.
    theta : float
        Time delay.

    """
    
    # Gain
    k = dout[-1]/din[-1]
          
    # Method: Smith
    if method == 'smith':
        o28 = 0.283*(max(dout)-min(dout))
        o63 = 0.632*(max(dout)-min(dout))

        i28 =  np.absolute(o28 - dout).argmin()
        i63 =  np.absolute(o63 - dout).argmin()

        t28 = time[i28]
        t63 = time[i63]

        tau = 3*(t63 - t28)/2
        theta = t63 - tau
        
    # Method: Sundaresan - Krishnaswamy
    elif method == 'sk':
        
        o35 = 0.353*(max(dout)-min(dout))
        o85 = 0.853*(max(dout)-min(dout))

        i35 =  np.absolute(o35 - dout).argmin()
        i85 =  np.absolute(o85 - dout).argmin()

        t35 = time[i35]
        t85 = time[i85]

        tau = 0.674803*(t85 - t35)
        theta = 1.29382*t35 - 0.293815*t85
        
    else:
        print('Error: Bad Argument')
        return 0, 0, 0
                
    # Compare and graph
    G = ct.tf([k], [tau, 1])*ct.tf(*ct.pade(theta, 10))
    _, c = ct.step_response(din[-1]*G, time)
    
    # Mean Absolute Percent Error (MAPE)
    mape = np.mean(np.abs((dout-c)/dout))*100
        
    # Show results
    print()
    print('FOPDT identification:')
    print('    Method: ', method)
    print('    Mean Absolute Percent Error: {:.4f}%'.format(mape))
    print('    k: {:.6f}, tau: {:.6f}, theta: {:.6f} '.format(k, tau, theta))
    print()
        
    return k, tau, theta

def secondOrder(time, din, dout, p0 = [1.0, 1.0, 0.1]):
    """
    Identification of a second order system.
    
    Parameters
    ----------
    time : numpy array
        Time array.
    din : TYPE
        Input signal data.
    dout : numpy array
        System response data.
    p0 : float list, optional
        Initial guess . The default is [k, Wn, z] = [1.0, 1.0, 0.1].

    Returns
    -------
    k : float
        System's gain.    
    Wn : float
        Natural frequency.
    z : float
        Relative damping coefficient

    """
    
    def second_order_mdl(t, k, wn, zeta):
        my_tf = sig.TransferFunction(k*(wn**2), [1, 2*zeta*wn, wn**2])
        to, yo, xo = sig.lsim2(my_tf, U=din, T=time)
        return yo
    
    params, params_cov = opt.curve_fit(second_order_mdl, time, dout, method='lm', maxfev=1000, p0=p0)
    
    # Step response
    k = params[0]
    Wn = params[1]
    z = params[2]
    G = ct.tf([k*Wn**2], [1, 2*z*Wn, Wn**2])
    _, c = ct.step_response(din[-1]*G, time)
    
    # Mean Absolute Percent Error (MAPE)
    mape = np.mean(np.abs(np.nan_to_num((dout-c)/dout, False, 0)))*100;
    
    # Show results
    print()
    print('Second order identification:')
    print('    Mean Absolute Percent Error: {:.4f}%'.format(mape))
    print('    k: {:.6f}, Wn: {:.6f}, z: {:.6f} '.format(k, Wn, z))
    print()
    
    # k, Wn, z
    return  k, Wn, z


