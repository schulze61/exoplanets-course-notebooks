# -*- coding: utf-8 -*-
"""
Created on Thu Jan  4 10:49:44 2024

@author: jgsch
"""
import numpy as np
from scipy.optimize import fsolve as fs


#some constants
G = 6.67430*(10**(-11)) #SI
Msun = 2*(10**30) #SI
au2m = 1.496e+11
Me = 5.972*(10**24)
c = 2.998e+8 #speed of light in m/s
halpha_rest = 6562.8 #angstrom


def transcendental_equ(E, M, e):
    return M - (E - e*np.sin(E))

def build_rv_curve(Mp = 1.0, a = 1.0, i = np.pi/2.0, e = 0.0, V0 = 0.0, w = 0.0,  T = 0.5, numpts = 100):
    a = a*au2m
    P = 2.0*np.pi*np.sqrt((a**3)/(G*Msun))
    t = P*np.linspace(0, 1.0, numpts)
    T = T*P
    Mp = Mp*Me
    K = (Mp/Msun)*np.sqrt(G*Msun/a)*np.sin(i)
    
    
    M = 2.0*np.pi*(t-T)/P
    E = np.array([fs(transcendental_equ, np.pi, args = (m, e)) for m in M])
    v = np.arccos((np.cos(E) - e) / (1 - e*np.cos(E)))
    V = V0 - K*(np.cos(w + v) + e*np.cos(w))
    
    dlambda = np.sqrt((1.0 + V/c) / (1.0 - V/c)) - 1.0
    halpha_obs = dlambda*halpha_rest + halpha_rest
    
    return t/P, V, E, halpha_obs, K