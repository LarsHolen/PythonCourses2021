# -*- coding: utf-8 -*-
"""
Created on Thu Feb 11 12:41:59 2021

@author: larsh
"""

# %% import 

import numpy as np


# %% Definerer variabler

h = 0
k1 = 0

# %% Beregener

k1 = float(input("Skriv lengde på korteste katet: "))
h = float(input("Skriv lengde på hypotenus: "))

k2 = np.sqrt(h**2 - k1**2)

print("Det andre katetet er: ", k2)
print("Overflateareal på den rettvinklede trekanten med 2 desimaler er: ", np.round(k1*k2/2, 2))
print("Omkretsen på den rettvinklede trekanten med to desimaler er: ",  np.round(k1 + k2 + h,2))