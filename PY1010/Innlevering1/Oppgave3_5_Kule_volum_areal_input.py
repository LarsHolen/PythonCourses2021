# -*- coding: utf-8 -*-
"""
Created on Thu Feb 11 12:41:59 2021

@author: larsh
"""

# %% import 

import numpy as py


# %% Definerer variabler

r = 0


# %% Beregener

r = float(input("Skriv radius på kulen: "))

print("Overflateareal på kulen med 2 desimaler er: ", py.round( 4 * py.pi * r**2, 2))
print("Volumet på kulen med to desimaler er: ",  py.round(4/3 * py.pi * r**3,2))