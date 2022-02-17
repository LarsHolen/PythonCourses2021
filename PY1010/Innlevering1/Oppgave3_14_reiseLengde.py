# -*- coding: utf-8 -*-
"""
Created on Fri Feb 12 13:43:29 2021

@author: larsh
"""

# %% importerer pakker

import numpy as np


# %% Definerer Variabler

xStart = 0
yStart = 0

x1 = 0
y1 = 0

strekning = 0

# %% Funksjon definisjoner

def reiselengde(x1,y1,x2,y2):
    return np.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


# %% Program loekke

while True:
    try:
        x2 = float(input("Skriv inn x-koordinaten for neste destinasjon her:"))
        y2 = float(input("Skriv inn y-koordinaten for neste destinasjon her:"))
        
    except ValueError:
        continue
    else:
        strekning += reiselengde(x1, y1, x2, y2) 
        x1 = x2
        y1 = y2
        print("Sammenlagt reiselengde max 2 desimaler =", np.round(strekning,2))
        continue
    