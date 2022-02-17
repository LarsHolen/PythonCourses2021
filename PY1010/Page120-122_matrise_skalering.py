# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 10:52:14 2021

@author: larsh
"""

# %% Imports

import numpy as np

# %% Matriser/Vector/2d array tests

M = np.array([[1,1],[1,2]])
v = np.array([[3],[4]])
p = M @ v
pf = M * v
print("M: \n", M, "\n")
print("v: \n",v, "\n")
print("M * v =  \n", pf, "\n")
print("M @ v = \n", p, "\n")
