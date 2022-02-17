# -*- coding: utf-8 -*-
"""
Created on Thu Sep 23 17:43:18 2021

@author: Lars Holen


Given an array of integers, find the maximum possible sum yiou can 
get from one of its 



"""


inputList = [-2,2,5,-11,6]


def func1(l):
    maxSum = l[0]
    currentSum = maxSum
    for i in range(1,len(l)):
        currentSum = max(l[i] + currentSum , l[i])
        maxSum = max(currentSum, maxSum)
    return maxSum

        
    
print(func1(inputList))