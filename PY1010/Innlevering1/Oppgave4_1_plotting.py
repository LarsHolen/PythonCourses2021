# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 10:47:46 2021

@author: Lars Holen

"""

# %% Import

import numpy as np
import matplotlib.pyplot as plt


# %% Variabler

x = np.array([0,1,2,3,4,5])
y = x
z = np.sqrt(x)


# %% Plotting

plt.close("all")
plt.figure(1, figsize = (12/2.52, 9/2.52))
plt.plot(x,y, "r-*")
plt.plot(x,z, "b--o")

plt.xlim(0, 6)
plt.ylim(0,6)
plt.title("Oppgave 4.1")
plt.xlabel("X [s]")
plt.ylabel("[m]")
plt.grid()


plt.legend(labels=("y = x", "z = Sqrt(x)"))

plt.savefig("plotOppgave4_1.pdf")
plt.show()
