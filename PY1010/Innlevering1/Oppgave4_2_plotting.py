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
plt.figure(1, figsize = (12, 9))
plt.subplot(2,1,1)
plt.title("Oppgave 4.2")
plt.legend(labels=("y = x"))
plt.xlabel("X [s]")
plt.ylabel("[m]")
plt.xlim(0, 6)
plt.ylim(0,6)
plt.plot(x,y, "r-*")
plt.subplot(2,1,2)
plt.plot(x,z, "b--o")

plt.xlim(0, 6)
plt.ylim(0,6)
plt.title("Oppgave 4.2")
plt.xlabel("X [s]")
plt.ylabel("[m]")
plt.grid()


plt.legend(labels=("z = Sqrt(x)"))

plt.savefig("plotOppgave4_1.pdf")
plt.show()
