# -*- coding: utf-8 -*-
"""
Created on Tue May  4 11:27:53 2021

@author: Lars Holen

"""


# %% importerer pakker

import numpy as np
import matplotlib.pyplot as plt


# %% Def variabler

g = 9.81

# %% Def funksjoiner

# Funksjon som gir y komponent/høyde på det fallende onbjektet
def y_komponent(v0y, t):
    g = 9.81
    return v0y * t - 0.5 * g * t ** 2

# Funksjon som gir x komponent/streking på det fallende objektet
def x_komponent(v0x, t):
    return v0x * t



# %% Bergenger data

# Lager en array med verdier fra 0 til 22, i 100 steg
tid = np.linspace(0,22,100)

# start hastighet på "fallet"
v0 = 150

# vinkel på "fallet"
vinkel =  44.5 * (2 * np.pi/360)
# np.pi/4

# Start x og y koordinater
vx_init = v0 * np.sin(vinkel)
vy_init = v0 * np.sin(vinkel)

Xkomponent = x_komponent(vx_init, tid)
Ykomponent = y_komponent(vy_init, tid)

plt.close("all")
plt.plot(Xkomponent, Ykomponent, "ko-")
plt.bar(Xkomponent, Ykomponent)
plt.xlabel("x [m]")
plt.ylabel("y [m]")
plt.gray()
plt.show()
