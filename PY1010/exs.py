# -*- coding: utf-8 -*-
"""
Created on Fri May  7 09:10:18 2021

@author: Lars Holen

"""
import time
import random
from typing import Callable, Any

def time_it(search: Callable[[list, Any], Any], L: list, v: Any) -> float:
    """ Time how long it takes to run function searcg to find value v in list L.
    """
    t1 = time.perf_counter()
    search(L, v)
    t2 = time.perf_counter()
    return (t2-t1) * 1000.0


def mySearch(L: list, v: Any) -> int:
    """ search
    """
    i = 0
    l = len(L)
    for a in L:
        
        i+=1
        l -= 1 
        if a == v:
           return i
       
        if a == L[l]:
           return l
        if i > l:
            return -1
        
    print(-1)
    return -1
        
        

v = 900000
myList = list(range(1000000))

#random.shuffle(myList)
iterations = 10
t = 0
tTotal = 0
for i in range(iterations):
    
    t =  time_it(mySearch, myList, v)
    tTotal += t
print("Avg: ", tTotal/iterations)

    