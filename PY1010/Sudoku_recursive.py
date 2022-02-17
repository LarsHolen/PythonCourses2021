# -*- coding: utf-8 -*-
"""
Created on Fri Apr 16 14:42:35 2021

@author: Lars Holen

"""

""

# %% importerer pakker
import numpy as np



# %% Def variabler

grid2 = [[5,3,0,0,7,0,0,0,0],
        [6,0,0,1,9,5,0,0,0],
        [0,9,8,0,0,0,0,6,0],
        [8,0,0,0,6,0,0,0,3],
        [4,0,0,8,0,3,0,0,1],
        [7,0,0,0,2,0,0,0,6],
        [0,6,0,0,0,0,2,8,0],
        [0,0,0,4,1,9,0,0,5],
        [0,0,0,0,8,0,0,7,9]]

grid = [[0,0,1,0,6,0,0,5,9],
        [0,0,0,0,0,3,0,2,0],
        [0,6,0,0,8,0,0,0,0],
        [4,0,0,0,0,0,5,0,0],
        [0,2,0,0,0,0,0,0,0],
        [0,7,0,2,0,0,4,8,0],
        [8,0,0,0,0,0,9,0,5],
        [7,0,0,6,0,9,0,3,0],
        [0,0,5,0,0,0,0,4,0]]
         

counter = 0

# %% Def funksjoiner

def solve():
    global grid
    global counter
    for y in range(9):
        for x in range(9):
            if grid[y][x] == 0:
                for n in range(1,10):
                    if possible(y,x,n):
                        grid[y][x] = n
                        counter+=1
                        solve()
                        grid[y][x] = 0
                return
            
    print(np.matrix(grid), counter)
   

# funksjon tester om n i x,y har en lik på rekke, i kolonne eller i 3x3 sector
def possible(y,x,n):
    global grid
    for i in range(9):
        if grid[y][i] == n and i != x:
            return False
    for i in range(9):
        if grid[i][x] == n and i != y:
            return False
    x0 = (x//3)*3
    y0 = (y//3)*3
    for i in range(3):
        for j in range(3):
            if grid[y0+i][x0+j] == n:
                return False
            
    return True

        


solve()
