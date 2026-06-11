# -*- coding: utf-8 -*-
"""
Created on Thu Jan  4 12:02:43 2024

@author: jgsch
"""

import numpy as np
Re = 6371000.0
days2sec = 86400
G = 6.67430*(10**(-11)) #SI
Msun = 2*(10**30) #SI
au2m = 1.496e+11
Me = 5.972*(10**24)


def lc_model(Rp = 1.0, Rs = 109.0, inc = np.pi/2.0, e = 0.0, a = 1.0, f0 = 1.0, omega = 0.0, npts = 100):
    
    Rp = Rp*Re
    Rs = Rs*Re
    a = a*au2m
    
    P = np.sqrt((4.0*np.pi*np.pi*(a**3))/(G*Msun))
    
    tc = P/2.0
    
    b = (a*np.cos(inc)/Rs)*((1.0 - e**2)/(1.0 + e*np.sin(omega)))
    n = 2.0*np.pi/P
    
    tau0 = (Rs/(a*n))*(np.sqrt(1.0 - e**2)/(1.0 + e*np.sin(omega)))          
    d = f0*((Rp/Rs)**2)
    T = 2.0*tau0*np.sqrt(1.0 - b**2)
    r = Rp/Rs
    
    tau = 2.0*tau0*r/np.sqrt(1.0 - b**2)
    
    time = np.linspace(-(T/2.0 + 5.0*tau), T/2.0 + 5.0*tau, npts) + tc
    #a2 = a*((1.0 - e**2)/(1.0 + e*np.sin(omega)))
    #n2 = n*((1.0 + e*np.sin(omega))**2)/((1.0 - (e**2))**(3.0/2.0))
    
    z = (a/Rs)*np.sqrt(((np.sin(n*(time-tc)))**2) + ((np.cos(inc)*np.cos(n*(time-tc)))**2))
    
    y = np.zeros(len(time))
    i = 0
    
    for t in time:
        if abs(t-tc) <= (T/2.0) - tau/2.0:
            y[i] = f0-d
        if (T/2.0 - tau/2.0 < abs(t-tc)) and (abs(t-tc) < T/2.0 + tau/2.0):
            y[i] = f0 - d + (d/tau)*(abs(t-tc) - T/2.0 + tau/2.0)
        if abs(t-tc) >= T/2.0 + tau/2.0:
            y[i] = f0
        i += 1
    return y, time/days2sec, tc/days2sec, b, z