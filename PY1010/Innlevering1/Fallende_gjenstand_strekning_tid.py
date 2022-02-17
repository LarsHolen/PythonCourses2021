# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 11:54:37 2021

@author: larsh
"""

# %% Imports

import numpy as np

# %% Fallende gjennstand tid 0-5 sec, s=strekning

t_start = 0
t_stopp = 5

Ts = 1 # Tidssteg pr beregning

n = int((t_stopp - t_start)/Ts+1) # Beregner antall hopp mulig fra start til stop met Ts mellomrom

g = 9.81 # jordens gjennomsnittlige aksellerasjon m/s/S

t = np.linspace(t_start, t_stopp, n) # Beregner tidene fra start til stop med n hopp
 
s = (1/2)*g*t*t

print(s)
print(t)
