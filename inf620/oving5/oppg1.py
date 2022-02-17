# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 08:38:47 2021

@author: Lars Holen

INF620 - Høstsemesteret 2021
Øvingsoppgave 5

"""

#%% Imports

import random
from matplotlib import pyplot  

#%% Oppgave 1 a)

"""
Skriv en funksjon lag_liste(n, sanns, maks) som returnerer en liste med
nedbørsverdier for n dager. Sannsynligheten for at en dag er en nedbørsdag er
gitt med parameteren sanns. På nedbørsdager er nedbøren et tilfeldig flyttall
på intervallet fra og med 0.0 til verdien på parameteren maks. På andre dager
er nedbøren lik 0.0.

"""

def lag_liste(n, sanns, maks):
    # Definerer resultatListe som liste
    resultatListe = []
    
    # Looper n ganger
    for i in range(n):
        # Finner ett tillfeldig flytetall fra 0 til 1
        regnerDet = random.random()
        # Sjekker om det tillfeldige tallet er mindre eller lik sanns
        if regnerDet <= sanns:
            # Finner en tillfeldig regnmengde fra 0 til maks, ved å gange
            # en verdi fra 0 til 1 med maks
            regnMengde = random.random() * maks
            # Legger til regnmengden i listen
            resultatListe.append(regnMengde)
        else:
            # Det regnet ikke, så legger til 0.0 i listen
            resultatListe.append(0.0)
    # Printer ut listen ved brukt av *, og sep comandoen som her separerer
    # hvert element med \n (new line)
    print(*resultatListe, sep="\n")


#%% Oppgave 1 b)

"""
Skriv en funksjon gjennomsnitt(nedbør) som returnerer en liste med 
gjennomsnittsnedbør fra og med første dag dekket av listen nedbør. For hver dag
i skal den returnerte listen inneholde gjennomsnittet av nedbør f.o.m. dag 0
t.o.m. dag i
"""
def gjennomsnitt(nedbor):
    """
    Parameters
    ----------
    nedbør : List
        En liste med mm nedbør på en dag.

    Returns
    -------
    result : Liste
        En liste med gjennomsnitts nedbør fra første dag, til første dag + i

    """
    
    # definerer resultatListe som liste
    resultatListe = []
    # definerer og setter sumNedbor til 0
    sumNedbor = 0.0
    # Looper gjennom nedbor
    for index, i in enumerate(nedbor):
        # Legger til i, dagens nedbor, til sumNedbor
        sumNedbor += i
        # Legger til nytt element i listen, som består av
        # sumNedbør/ index + 1
        # pluss en pga index starter på null
        resultatListe.append(sumNedbor/(index + 1))
    return resultatListe

#%% Oppgave 1 c)

"""
Skriv en funksjon økning(nedbør) som tar en nedbørsliste som parameter,
og som returnerer en liste med nedbørsøkninger fra dagen før. Vi antar at det
ikke var nedbør siste dag før observasjonene startet.
"""

def okning(nedbor):
    """
    Parameters
    ----------
    nedbor : List
        Liste over nedbor i mm pr dag.

    Returns
    -------
    result : List
        En liste med økningen fra i går til i dag i mm nedbør

    """
    resultatListe = []
    for index, i in enumerate(nedbor):
        if index == 0:
            resultatListe.append(i)
        else:
            resultatListe.append(i - nedbor[index-1])
    return resultatListe

#%% Oppgave 1 d)
"""
Denne oppgaven er kun for de som er interesserte i å gå utenfor pensum. Skriv
en funksjon plott(nedbør) som gjør bruk av funksjonene gjennomsnitt og
økning. Deretter skal funksjonen plotte nedbørsverdiene i listen nedbør sammen
med tilhørende gjennomsnittsverdier (se oppg. 1b) og økninger (se oppg. 1c).
"""

def plott(nedbor):
    """
    Parameters
    ----------
    nedbor : List
        Liste med nedbør i mm pr dag.

    Returns
    -------
    None.
        Plotter nedbør, gjennomsnittsnedbør og økninger til skjerm

    """
    # Lager data for snitt og økninger og lagrer i nye lister
    liste1_gjennomsnitt = gjennomsnitt(nedbor)
    liste2_okning = okning(nedbor)
    
    # Bruker pyplot til å plotte nedbor, økning og snitt listene
    pyplot.close("all")
    pyplot.title("Nedbør")
    
    pyplot.plot(liste1_gjennomsnitt)
    pyplot.plot(liste2_okning)
    pyplot.plot(nedbor)
    pyplot.grid()
    pyplot.xlabel("Dager")
    pyplot.ylabel("mm")
    pyplot.legend(('Gjennomsnitt','Økning', 'Nedbør'))
    pyplot.show()
            

#%%

def main():
    print("Main running")
    


#%% Kaller main funksjonen om denne filen blir kjørt
    
if __name__ == "__main__":
    main()