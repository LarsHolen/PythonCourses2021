# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 19:35:36 2021

@author: Lars Holen

"""


# %% Importerer pakker jeg trenger:
    
import random 

#%% Hovedfunksjon main()

def main():
    # Velger en tilfeldig serie 1,2,3 eller 4, som skal tilsvare
    # spar, kløver,hjerter, ruter
    serie = random.randint(1, 4)
    
    # Velger en tilfeldig verdi fra 1 til 13 i samsvar på verdiene på
    # kort seriene
    verdi = random.randint(1, 13)
    
    # starter med en tom streng, for oversiktens skyld.
    serieVerdiText = ""
    
    # Gir strengen en verdi, spar, kløver, hjerter eller ruter
    # utifra hvilket tall som er i serie variablen.  Legger også til 
    # ett mellomrom til slutt.
    if(serie == 1):
        serieVerdiText = "Spar "
    elif(serie == 2):
        serieVerdiText = "Kløver "
    elif(serie == 3):
        serieVerdiText = "Hjerter "
    elif(serie == 4):
        serieVerdiText = "Ruter "
    
    
    # Plusser på teksten Ess for 1 verdi, Konge for 13, Dame for 12 og 
    # Knekt for 11.  Mens de andre verdiene er heltall som blir gjort om
    # til streng med str()
    if(verdi == 13):
        serieVerdiText += "Konge"
    elif(verdi == 12):
        serieVerdiText += "Dame"
    elif(verdi == 11):
        serieVerdiText += "Knekt"
    elif(verdi == 1):
        serieVerdiText += "Ess"
        
    else:
        serieVerdiText += str(verdi)
    
    # Skriver ut svar
    print(serieVerdiText)

    

    
    # %% Sjekker om dette programmet heter "__main__", altså ikke importert som en pakke
    # Og kjører funksjonen main() om så
if __name__ == "__main__":
    main()