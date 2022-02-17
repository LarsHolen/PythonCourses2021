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
vinkel_k1_k2_grader = 90 # trekanten er rettvinklet, ergo vinkel mellom katetene er 90 grader

k2 = 0
vinkel_k1_h_grader = 0
vinkel_k2_h_grader = 0


# %% Beregener

k1 = float(input("Skriv lengde på korteste katet: "))
h = float(input("Skriv lengde på hypotenus: "))
k2 = np.sqrt(h**2 - k1**2)

vinkel_k1_h_grader = np.degrees(np.arccos(k1/h))
vinkel_k2_h_grader = np.degrees(np.arccos (k2/h))

print("Det andre katetet med to desimaler er: ", np.round(k2,2))
print("Overflateareal på den rettvinklede trekanten med 2 desimaler er: ", np.round(k1*k2/2, 2))
print("Omkretsen på den rettvinklede trekanten med to desimaler er: ",  np.round(k1 + k2 + h,2))
print("Summen av alle vinkler i grader er: ", np.round(vinkel_k1_h_grader,2) + np.round(vinkel_k1_k2_grader,2) + np.round(vinkel_k2_h_grader,2))
print("Vinkler i grader er: ", np.round(vinkel_k1_h_grader,2), "---" , np.round(vinkel_k1_k2_grader,2), "---", np.round(vinkel_k2_h_grader,2))
print("Vinklene i radianer er: ", np.round(np.radians(vinkel_k1_h_grader),2), "---" , np.round(np.radians(vinkel_k1_k2_grader),2), "---", np.round(np.radians(vinkel_k2_h_grader),2))




