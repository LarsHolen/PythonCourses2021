# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 11:33:40 2021

@author: Lars Holen (244697@student.usn.no)

"""

# %% Imports

import time


# %% Definere variabler

t0 = time.time()
t1 = 0



# %% Oppgave testing

print("Epoch: ", time.gmtime(0))
print(time.time()) # skriver ut antall sekunder siden epoch 1970, 1.1. kl 00:00:00
print("Before the sleep statement")
time.sleep(5) # Pauser, stopper programmet i 5 sekunder
print("After the sleep statement")
t1 = time.time() - t0;
print("Time passed: ", t1)

