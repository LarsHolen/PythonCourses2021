# -*- coding: utf-8 -*-
"""
Created on Thu Feb 11 12:41:59 2021

@author: larsh
"""

# %% import 

import numpy as np


# %% Definerer variabler

xA = 2.3
yA = 8.1

xB = 7.4
yB = -13.5


# %% Beregener

print("Avstand fra punkt A til punkt B = ",  np.sqrt((xA - xB) ** 2 + (yA - yB) ** 2))