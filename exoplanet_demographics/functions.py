# -*- coding: utf-8 -*-
"""
Created on Sun Jan 21 14:23:36 2024

@author: jgsch
"""

import numpy as np


h = 6.62607015e-27
c = 2.998e10
kb =  1.380649e-16
rsun_cm = 6.96e10
au2cm = 1.496e13
re = 637100000.0
nm = 1e-7


def chen_kipping(mass_array):
    rad = np.zeros(len(mass_array))
    for i in range(0, len(mass_array)):
        M = np.log10(mass_array[i])
        C1 = 0
        C2 = C1 + ((0.2790-0.589)*np.log10(2.04))
        C3 = C2 + ((0.589+0.044)*np.log10(318.0*0.414))
        if mass_array[i] <= 2.04:
            rad[i] = C1 + M*0.2790
        elif mass_array[i] > 2.04 and mass_array[i] <= 318.0*0.414:
            rad[i] = C2 + M*0.589
        else:
            rad[i] = C3 + M*(-0.044)
            
    return rad
    
    
    
    
    
