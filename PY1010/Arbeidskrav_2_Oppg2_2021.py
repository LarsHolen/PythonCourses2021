# -*- coding: utf-8 -*-
"""
Created on Fri Feb 12 11:23:03 2021

@author: larsh
"""

# %% Importerer pakker

import numpy as np


# %% Definerer variabler

grader_input = 0
radianer = 0

# %% Definerer funksjoner

def grad2rad(grader):
    return grader*np.pi/180

# %% Motta input

while True:
    try:
        grader_input = float(input("Skriv inn gradtallet: "))
    except ValueError: # om input ikke kan gjøres om til float
        continue
    else:
        break
            
# %% Skriv til skjerm

print("Beregninger rundes til 2 desimaler eller mindre")
print(np.round(grader_input,2),"grader er lik", np.round(grad2rad(grader_input),2), "radianer.")
print("Regner vi om til max <360 grader eller <6.28 radianer:")
print(np.round(grader_input % 360,2) ,"grader er lik", np.round(grad2rad(grader_input % 360),2), "radianer.")

