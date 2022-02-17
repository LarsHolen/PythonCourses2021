# -*- coding: utf-8 -*-
"""
Created on Sat Mar  6 10:27:20 2021

@author: Lars Holen

"""

# %% importerer pakker

import numpy as np
import matplotlib.pyplot as plt


# %% Def variabler



# %% Def funksjoiner

# funksjon som tar bredde, høyde og returnerer areal
def hemmelig(g, h):
    A = g * h
    return A


# funksjon som tar antall euro som input og returnerer nok og dollar verdien
def euroTilNokOgDollar(euro):
    euroNok = 10.42
    dollarNok = 1.19
    r1 = euro * euroNok
    r2 = euro * dollarNok
    return r1, r2

def storeKatet(x,y):
    h = np.sqrt(x**2 + y**2)
    return h

def kinEnergi(m, v):
    e = 1/2 * m * v ** 2
    return e

def potEnergi(m,h):
    g = 9.81
    e = m * g * h
    return e

def objHeightFromEnergyMass(e,m, g = 9.81):
    h = e/(m*g)
    return h

def func1(x):
    return x ** 2 + 3

def func2(x):
    """ Test"""

    return 3 * x -1



# %%  Test
print(func2(2))
help(func2)

xa = np.linspace(-2, 3, 100)
plt.close("all")
plt.figure(1, figsize = (12,9))

plt.plot(xa, func1(func2(xa)), xa , func2(func1(xa)))
plt.legend(labels=("lab1", "lab2"))
plt.show()
    



