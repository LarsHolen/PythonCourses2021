# -*- coding: utf-8 -*-
"""
Created on Wed Sep 22 18:56:06 2021

@author: Lars Holen

"""

from random import randint

def main():
    print("Main running")
    
    # tre terninger skal kastes. 6'ere skal beholdes.  Man skal fortsette
    # å kaste til alle ternigenen er 6'ere
    # Hver omgang skal skrives til skjerm (1. kast: 2 4 6)
    # Når alle terninger er 6'ere, skriv ut " Etter x kast med tre terninger
    # viste alle terningene 6.
    
    # lager en liste med tre heltall, som representerer 3 terninger
    diceList = [0,0,0]
    # antall kast
    throws = 0
    # bool for om alle terningene er like
    isEqual = False
    
    while not isEqual:
        throws += 1
        if(diceList[0] != 6):
            diceList[0] = randint(1, 6)
        if(diceList[1] != 6):
            diceList[1] = randint(1, 6)
        if(diceList[2] != 6):
            diceList[2] = randint(1, 6)
        print(str(throws) + ". kast: ", diceList[0], diceList[1], diceList[2])
        if(diceList.count(6) == 3):
            isEqual = True
    
    print("Etter ", throws, "kast med tre terninger viste alle terningene verdien ", diceList[2]) 
    
    
if __name__ == "__main__":
    main()