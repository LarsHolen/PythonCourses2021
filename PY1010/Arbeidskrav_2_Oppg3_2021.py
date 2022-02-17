# -*- coding: utf-8 -*-
"""
Created on Fri Feb 12 13:43:29 2021

@author: larsh
"""

# %% importerer pakker

import numpy as np


# %% Definerer Variabler

x1 = 0  #start punkt i origo 0,0
y1 = 0

strekning = 0

# %% Program

x2 = float(input("Skriv inn x-koordinaten for andre destinasjon her:"))
y2 = float(input("Skriv inn y-koordinaten for andre destinasjon her:"))

strekning1 = np.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
strekning += strekning1
print("Avstand fra x1,y1 til x2,y2 er lik: ", strekning1)
print("Totalt reiste strekning er lik: ", strekning)
print("Avstand fra startpunkte1(x1,y1) er lik:", strekning1) 
print("Disse tre skal alltid være like ved andre punkt.")

x3 = float(input("Skriv inn x-koordinaten for tredje destinasjon her:"))
y3 = float(input("Skriv inn y-koordinaten for tredje destinasjon her:"))

strekning2 = np.sqrt((x2 - x3) ** 2 + (y2 - y3) ** 2)
strekning += strekning2
strekningStartSlutt = np.sqrt((x1 - x3) ** 2 + (y1 - y3) ** 2)
print("Avstand fra x2,y2 til x3,y3 er lik: ", strekning2)
print("Totalt reiste strekning er lik: ", strekning)
print("Avstand fra startpunkte1(x1,y1) er lik:", strekningStartSlutt)

x4 = float(input("Skriv inn x-koordinaten for fjerde destinasjon her:"))
y4 = float(input("Skriv inn y-koordinaten for fjerde destinasjon her:"))

strekning3 = np.sqrt((x3 - x4) ** 2 + (y3 - y4) ** 2)
strekning += strekning3
strekningStartSlutt = np.sqrt((x1 - x4) ** 2 + (y1 - y4) ** 2)
print("Avstand fra x2,y2 til x3,y3 er lik: ", strekning3)
print("Totalt reiste strekning er lik: ", strekning)
print("Avstand fra startpunkte1(x1,y1) er lik:", strekningStartSlutt)


