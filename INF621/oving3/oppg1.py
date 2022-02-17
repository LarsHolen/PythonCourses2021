# -*- coding: utf-8 -*-
"""
Created on Fri Nov 19 12:15:46 2021

@author: Lars Holen

INF621 - Høstsemesteret 2021

Oppgave 1

Terninger (50%)
Svar leveres på fil med navn oppg1.py
Vi ser for oss m ‘terninger’ med n sider, der n ikke nødvendigvis er lik 6. Sidene på
terningene er merket med tallene 1, 2, . . . , n. Vi vil undersøke hvor mange kast med
terningene vi trenger for at minst en av terningene viser verdien n (største verdi på
terningen).


"""

#%% Imports

from random import randint

#%% Oppgave 1. a)
"""
Skriv en funksjon tell_kast(m,n) som kaster alle de m terningene like til minst
en av dem viser verdien n. Funksjonen skal returnere antall ganger terningene ble
kastet.
"""

def tell_kast(m,n):
    """
    Parameters
    ----------
    m : int
        Antall terninger.
    n : int
        Terningens antall sider.

    Returns
    -------
    None.
    Prints result to screen
    """
    # Definerer variabler og setter enklere navn på parameter verdiene
    antallKast = 0
    antallTerninger = m
    antallSider = n
    suksess = False
    # Lager en dictionary som skal
    while(suksess != True):
        antallKast += 1
        for x in range(0, antallTerninger):
            verdi = randint(1, antallSider)
            if verdi == antallSider:
                suksess = True
                break;
    return antallKast
    
#%% Oppgave 1. b)
"""
Skriv pythonkode som kaller opp tell_kast(m,n) for ulike verdier av m og n, og
som skriver resultatene til en CSV-fil (kast.csv). Et eksempel på en slik fil er gitt
i mappen Filer/Oppgaver/Oving3 på MittUiB. La m variere fra 1 til 18, og n fra
1 til 20. Radene i filen skal svare til m, og kolonnene til n. Det er ikke noe krav til
hvilken mappe filen skal plasseres i.
"""
def test_tell_kast():
    """
    Dette tester metoden tell_kast for verdier m = 1-18 og n= 1-20
    Resultatet blir skrevet til filen kast.csv i csv format.

    Returns
    -------
    None.

    """
    colonne = 20
    rad = 18
    with open("kast.csv", mode="w") as fil:
        for m in range(0, rad + 1):
            for n in range(0, colonne + 1):
                # Tester om vi er i øverste venstre hjørne
                if m == 0 and n == 0:
                    fil.write(";")
                # Tester om vi er på øverste linje, men ikke i første posisjon
                if m == 0 and n > 0:
                    fil.write(str("n=" + str(n) + ";")) 
                # Tester om vi er i første posisjon på linjen, men ikke øverst    
                if m > 0 and n == 0:
                    fil.write(str("m=" + str(m)))
                    print("m=", m)
                # Tester om vi ikke er i første posisjon på linjen og ikke øverst
                # om så, begynner vi med ; og fyller inn data fra tell_kast
                if m > 0 and n > 0:
                    fil.write(str(";" + str(tell_kast(m, n))))
                
                # Tester om vi er på slutten av linjen, så vi setter inn ett linjeskift
                if n == colonne:
                    fil.write("\n")
                    
                
                


#%% Main
def main():
    tell_kast(1, 10)
    #test_tell_kast();
    
if __name__ == "__main__":
    main()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    