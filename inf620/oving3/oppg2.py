# -*- coding: utf-8 -*-
"""
Created on Wed Sep 22 18:06:58 2021

@author: Lars Holen

"""
import random

def main():
    print("Main running")
    isEqual = False
    diceThrows = 0
    
    
    while not isEqual:
        diceThrows += 1
        global diceOne 
        diceOne = random.randint(1, 6)
        diceTwo = random.randint(1, 6)
        diceThree = random.randint(1, 6)
        print(str(diceThrows) + ". kast: ", diceOne, diceTwo, diceThree)
        if(diceOne == diceTwo == diceThree):
            isEqual = True
    
    print("Etter ", diceThrows, "kast med tre terninger viste alle terningene verdien ", diceOne)
    
    
if __name__ == "__main__":
    main()