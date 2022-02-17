# -*- coding: utf-8 -*-
"""
Created on Thu Feb 11 12:10:30 2021

@author: larsh
"""

# %% imortere

import numpy as py

# %% Definerer variabler

belop = 10000
bankRente = 1.85

antallAar = 5

svar = 0

desimaler = 2

# %% Beregner

svar = py.round(belop * ((1 + bankRente/100)**antallAar),desimaler)

# %% Skriver svar til skjerm

print("Innskuddet har økt fra ", belop, " kroner, til ", svar, " på ", antallAar, " år.\nSvaret er rundet med ", desimaler, " desimaler.")


