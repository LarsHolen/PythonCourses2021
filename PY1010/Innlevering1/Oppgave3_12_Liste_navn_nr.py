# -*- coding: utf-8 -*-
"""
Created on Fri Feb 12 13:43:29 2021

@author: larsh
"""

# %% Definerer Variabler

navn = ["Eli", "Ola", "Ali", "Ela"]
tlf = [9423234,9223001,4756001,9592676]


# %% Tar imot input, og set om en finner det i listen

while True:
    
    try:
         inputNavn = input("Skriv inn fornavn på personen du vil ha nummeret til:")
         index = navn.index(inputNavn)
    except ValueError: # Om input ikke er tall, skaff ny input
         print("Navn ikke funnet i listen/Husk stor forbokstav")
         continue
    else:
        break;
        
     



# %% Skriver til skjerm


print(inputNavn, "sitt nummer er:", tlf[navn.index(inputNavn)])