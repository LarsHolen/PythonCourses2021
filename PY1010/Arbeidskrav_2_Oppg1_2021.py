# -*- coding: utf-8 -*-
"""

Arbeidskrav 2

Created on Fri Feb 12 09:33:12 2021

@author: larsh
"""

# %% importere pakker

import numpy as np

# %% Definere variabler

antall_elever = 0
antall_pizza = 0

# %% Definere funksjon

def faaOgsjekkAntall():
    while True:
        try:
            tall = int(input("Skriv inn antall elever: "))
        except ValueError: # Om input ikke er tall, skaff ny input
            continue
        else:
            if tall < 1: # Om tallet er under 1, må det være feil. Skaff ny input
                continue
            else:
                return (tall)
            

# %% Få antall elever fra bruker:
    
antall_elever = faaOgsjekkAntall()


# %% Beregninger

antall_pizza = np.ceil(antall_elever/4) # np.ceil runder tallet opp til nermeste heltall.  Men blir ikke lagret som heltall variabel, er fortsatt float


# %% Skriver til skjerm

print("Det må handles", int(antall_pizza), "pizzaer til klassefesten!") #antall_pizza gjøres om til heltall for syns skyld






