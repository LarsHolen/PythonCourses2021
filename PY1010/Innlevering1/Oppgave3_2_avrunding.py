# -*- coding: utf-8 -*-
"""
Created on Thu Feb 11 12:29:54 2021

@author: larsh
"""

# %% Import

import numpy as py

# %% Setter variabler

var1 = 1.5000
var2 = 1.2222
var3 = 1.7555

# %% Skriver ut variablene med forskjellig bruk av funksjonene ceil() og floor() 

print("Celi() funksjon på ", var1, " blir ", py.ceil(var1))
print("Floor() funksjon på ", var1, " blir ", py.floor(var1))
print("Round() funksjon på ", var1, " blir ", py.round(var1, 0))

print("\nCeli() funksjon på ", var2, " blir ", py.ceil(var2))
print("Floor() funksjon på ", var2, " blir ", py.floor(var2))
print("Round() funksjon på ", var2, " blir ", py.round(var2, 0))

print("\nCeli() funksjon på ", var3, " blir ", py.ceil(var3))
print("Floor() funksjon på ", var3, " blir ", py.floor(var3))
print("Round() funksjon på ", var3, " blir ", py.round(var3, 0))

# %% Kommentar
"""
Ceil funksjonen runder opp til nærmeste heltall
Floor funksjonen runder ned til nærmeste heltall
Round funksjonen runder opp fra .5 og ned under .5, samt en får 
angi antall desimaler en ønsker. Angir en null, får man heltall.
"""