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
zStart = 0

x1 = 0
y1 = 0
z1 = 0

strekning = 0
strekningFraStart = 0

A = np.array([6,7,8,1,2,3,4,5])
x = 2.6354

print(np.abs(x))

# %% Funksjon definisjoner

def reiselengde(x1,y1,z1,x2,y2,z2):
    return np.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2 + (z1 -z2) ** 2)


# %% Program loekke

while True:
    try:
        x2 = float(input("Skriv inn x-koordinaten for neste destinasjon her:"))
        y2 = float(input("Skriv inn y-koordinaten for neste destinasjon her:"))
        z2 = float(input("Skriv inn z-koordinaten for neste destinasjon her:"))
        
    except ValueError:
        continue
    else:
        strekning += reiselengde(x1, y1, z1, x2, y2, z2) 
        strekningFraStart = reiselengde(x2, y2, z2, xStart, yStart, zStart) 
        x1 = x2
        y1 = y2
        z1 = z2
        
        print("\nSammenlagt reiselengde gjennom alle punkter max 2 desimaler =", np.round(strekning,2))
        print("Reiselengde fra startpunkt til siste punkt max 2 desimaler =", np.round(strekningFraStart,2))
        continue
    