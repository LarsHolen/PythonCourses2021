# -*- coding: utf-8 -*-
"""
Created on Tue Sep 28 22:04:40 2021

@author: Lars Holen

"""

def main():
    print("Main running")
    
#%% Oppgave C
def halveringstid(s, alpha, beta):
    if(beta <= alpha * s):
        return None
    uker = 0
    halveS = s / 2
    while(s > halveS):
        s = round( s + alpha * s - beta)
        uker = uker + 1
        
    return uker
 
#%% Oppgave B
def utvikling(s, alpha, beta, n):
    print("%-4s %6s" %("Uke", "Syke"))
    for i in range(n+1):
        print("%-4d %6d" %(i, s))
        s = neste(s, alpha, beta)
        
        
#%% Oppgave A
def neste(s, alpha, beta):
    antall = round( s + alpha * s - beta)
    if(antall < 0):
        antall = 0
    return antall
    
if __name__ == "__main__":
    main()