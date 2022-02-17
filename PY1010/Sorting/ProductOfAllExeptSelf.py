# -*- coding: utf-8 -*-
"""
Created on Thu Sep 23 08:23:43 2021

@author: Lars Holen

"""



# %% imports

import random

# %% Global variables

# Return a list of products of all numbers, except itself


#List to be sorted:
counter = 0
myList = [1,2,3,4]
listLength = len(myList)  


#for i in range(listLength):
#    a = random.randint(1, 500)
#    myList.append(a)




# Simplest with divination
def func1(theList):
    totalSum = 1
    sumArray = []
    for i in theList:
        totalSum = totalSum * i
    
    for j in theList:
        sumWithoutMe = int(totalSum / j)
        sumArray.append(sumWithoutMe)
    return sumArray


# without use of divination
# could use one separate loop for each of the sides.  And save first 
# side in the result list before doing other side, thus saving space of one list
def func2(theList):
    sumLeftList = []
    sumRightList = []
    resultList = []
    sumRight = 1
    
    # Looping once
    for i in range(len(theList)):
        # Calculate whats left of i and save it
        if(i == 0):
            sumLeft = 1
        elif(i == 1):
            sumLeft = theList[i-1]
        elif(i == len(theList)):
            sumLeftList
        else:
            sumLeft = sumLeft * theList[i-1]
        sumLeftList.append(sumLeft)
       
        
        # Calculate whats right of i and save it
        if(i < len(theList)):
            if(i == 0):
                sumRight = 1
            elif(i == 1):
                sumRight = theList[len(theList)-(i)]
            else:
                sumRight = sumRight * theList[len(theList)-i]
        sumRightList.insert(0,sumRight)
        in_a_dndMixin_drag
        
    # loop results and save the products of the two sides
    for j, k in zip(sumRightList, sumLeftList):
        resultList.append(j*k)
       
    return resultList

print("Func1", func1(myList))
print("Func2",func2(myList))
    
