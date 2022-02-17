# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 20:11:00 2021

@author: Lars Holen

"""

# %% Importerer pakker jeg trenger:
    
import random 


#%% Hovedfunksjon main()

def main():
    # Kaster 3, sekskantede terninger og lagrer verdiene
    verdi1 = random.randint(1, 6)
    verdi2 = random.randint(1, 6)
    verdi3 = random.randint(1, 6)
    
    
    # Finner max, min og medium av verdiene 
    minVerdi = min(verdi1, verdi2, verdi3)
    medVerdi = verdi1 + verdi2 + verdi3 - min(verdi1, verdi2, verdi3) - max(verdi1, verdi2, verdi3)
    maxVerdi = max(verdi1, verdi2, verdi3)
    
    # Skriver ut til skjerm
    print("%-20s %15d" %("Minste verdi: ", minVerdi))
    print("%-20s %15d" %("Median: ", medVerdi))
    print("%-20s %15d" %("Største verdi: ", maxVerdi))
    
    # Sjekker om median er like langt fra max som min
    if(medVerdi - minVerdi == maxVerdi - medVerdi):
        print("Medianen ligger midt mellom minste og største verdi.\n")
    else:
        print("Medianen ligger ikke midt mellom minste og største verdi.\n")

    
    # En annen måte er å sette verdiene inn i en liste, bruke sort()
    # funksjonen for å få minste først, median og høyeste til slutt i
    # lista
    verdiListe = [verdi1, verdi2, verdi3]
    verdiListe.sort()
    
    # Skriver ut til skjerm
    print("%-20s %15d" %("Minste verdi: ", verdiListe[0]))
    print("%-20s %15d" %("Median: ", verdiListe[1]))
    print("%-20s %15d" %("Største verdi: ", verdiListe[2]))
    
    # Sjekker om median er like langt fra max som min
    if(verdiListe[1] - verdiListe[0] == verdiListe[2] - verdiListe[1]):
        print("Medianen ligger midt mellom minste og største verdi.")
    else:
        print("Medianen ligger ikke midt mellom minste og største verdi.\n")
        
    
    # %% Sjekker om dette programmet heter "__main__", altså ikke importert som en pakke
    # Og kjører funksjonen main() om så
if __name__ == "__main__":
    main()