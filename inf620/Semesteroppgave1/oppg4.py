# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 21:19:07 2021

@author: Lars Holen

"""


#%% Hovedfunksjon main()

def main():
    # Henter data fra bruker
    dag = str(input("Hvilken dag er det i dag? "))
    dagVerdi = 0
    storDag = "ukjent"
    
    # sjekker at en har skrevet inn en korrekt dag.  Bruker upper() for
    # å godta alle mulige variasjoner med stor/liten bokstav.  Feks
    # LørDaG blir med upper gjort om til LØRDAG
    if(dag.upper() == "MANDAG"):
        dagVerdi = 0
    elif(dag.upper() == "TIRSDAG"):
        dagVerdi = 1
    elif(dag.upper() == "ONSDAG"):
        dagVerdi = 2
    elif(dag.upper() == "TORSDAG"):
        dagVerdi = 3
    elif(dag.upper() == "FREDAG"):
        dagVerdi = 4    
    elif(dag.upper() == "LØRSDAG"):
        dagVerdi = 5
    elif(dag.upper() == "SØNDAG"):
        dagVerdi = 6
    else:
            # input var ikke en gyldig dag.  Printer ut kommentar og avslutter
            print("Ugyldig dag.")
            return
        
    # Henter data fra bruker
    while True:
         try:
            
             antallDager = int(input("Hvor mange dager er det til den store dagen? "))
            
             
             break
           
         except:
                # Bruker har ikke skrevet inn ett heltall.  Printer ut kommentar
                # og prøver igjen pga while løkken
                print("Det er ikke ett heltall!")
        
    # Legger sammen dagsVerdi og antallDager.  Finner så rest, etter å ha
    # delt på 7(dager i uken).  Resten vil da gi en verdi fra 0-6, som
    # stemmer med dagVerdiene over.
    totalDager = antallDager + dagVerdi
    restDager = totalDager % 7
    
    
    # Bruker resten for å finne dagen
    if(restDager == 0):
        storDag = "mandag"
    elif(restDager == 1):
        storDag = "tirsdag"
    elif(restDager == 2):
        storDag = "onsdag"
    elif(restDager == 3):
        storDag = "torsdag"
    elif(restDager == 4):
        storDag = "fredag"
    elif(restDager == 5):
        storDag = "lørdag"
    elif(restDager == 6):
        storDag = "søndag"
    else:
        # I tilfelle feil i koden
        print("Noe gikk galt!")
    
    # Skriver ut svaret
    print("Den store dagen faller på en " + storDag)
    
   
    
    
# %% Sjekker om dette programmet heter "__main__", altså ikke importert som en pakke
# Og kjører funksjonen main() om så
    
if __name__ == "__main__":
    main()