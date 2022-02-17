# -*- coding: utf-8 -*-
"""
Created on Fri Feb 12 13:43:29 2021

@author: larsh
"""

# %% Definerer Variabler

s = "Nedre grense for karakter E er 40 poeng. 8 12 eller 3"

# %% Gjør greier
    
minList = s.split()

for item in minList:
    try:
        test = int(item)
    except ValueError:
        continue
    else:
        print("Tall funnet i teksten ", int(item))
        continue
        
        


# %% Skriver til skjerm


print(minList)