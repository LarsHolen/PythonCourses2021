# -*- coding: utf-8 -*-
"""
Created on Tue Sep 28 20:25:42 2021

@author: Lars Holen

"""

#%% Imports
from random import randint


#%% main function
def main():
    turnering()
    



#%% Functions

def turnering():
    terninger = 0
    resultatDict = {} 
    # Krever ett heltall for antall terninger som skal brukes i turneringen
    while True:
        try:
             terninger = int(input("Skriv antall terninger: "))
             print("Takk!")
             break
        except:
            print("Det er ikke ett heltall!")
    spiller_navn = input("Første spillers navn: ")
    spiller_poeng = 0
    while True:
        # Tester om man vil avslutte med en tom streng som input
        if(spiller_navn == ""):
            break
        # Tester om navnet har blitt brukt.
        if spiller_navn in resultatDict:
            # Navnet finnes allerede, så vi legger til ett tilfeldig tall
            # og satser på at ingen får det samme tilfeldige tallet
            spiller_navn = spiller_navn +"_" + str(randint(0, 100000000))
        spiller_poeng = stigespill(spiller_navn, terninger)
        
        resultatDict[spiller_navn] = spiller_poeng
        print(resultatDict)
        spiller_poeng = 0
        spiller_navn = input("Neste spillers navn: ")
        
    sortertResultatDict = sorted(resultatDict.items() , key=lambda x: x[1], reverse=True)
    print("\nResultat liste: ")
    for i in sortertResultatDict:
        print(i[0],"fikk",  i[1], "poeng.")
    

def stigespill(navn, n):
    """
    

    Parameters
    ----------
    navn : String
        Navnet på spiller.
    n : int
        antall terninger.

    Returns
    -------
    poeng : int
        poengscore.

    """
    listeMedTerninger = [0] * n
    totalPoeng = 0
    poeng = 0
    sistePoeng = 0
    kast_igjen = True;
    print(navn, "kaster terningene!")
    while kast_igjen:
        # Kunne brukt terning funksjonen her, men gjør det på en annen måte for å vise hver ternings verdi
        for index, terning in enumerate(listeMedTerninger):
            terning = randint(1,6)
            print(index+1,"terning viser:", terning)
            poeng = poeng + terning
        print("Poeng denne runden:", poeng)
        if(poeng < sistePoeng):
            totalPoeng = 0
            print("Du kastet en lavere poengsum i dette kastet enn i forige! 0 poeng!")
            break
        else:
            totalPoeng = totalPoeng + poeng
            sistePoeng = poeng
            poeng = 0
            print("Totalscore så langt:", totalPoeng)
            
            while True:
                try:
                     prøve_igjen = str(input(navn + " kast igjen(j/n)?"))
                     if(prøve_igjen == "j"):
                         break
                     elif(prøve_igjen == "n"):
                         print("Spillet avsluttes med:", totalPoeng, "poeng")
                         kast_igjen = False
                         break
                except:
                    print("Kast igjen(j/n)?")
    
    
    
    
    return totalPoeng

def terninger(n):
    """
    Parameters
    ----------
    n : int
        n er antall terninger som skal bli kastet
    
    Returns
    -------
    total : int
        Summen av alle terningverdier

    """
    total = 0
    
    for i in range(n):
        total = total + randint(1, 6)
    
    return total
    
#%% Kode som kjører main() om filen ikke er importert som pakke.    
if __name__ == "__main__":
    main()