# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 10:11:48 2021

@author: Lars Holen

INF620 - Høstsemesteret 2021
Øvingsoppgave 5

"""

#%% Imports

import random
from matplotlib import pyplot  

#%% Oppgave info
"""
Vi skal skrive kode som skal hjelpe en kryssordleverandør å lage rutemønster. Et
kryssord betraktes som et rektangel delt opp i åpne og lukkede ruter. I koden som
skal utvikles i denne oppgaven representeres rutemønsteret med en todimensjonal
liste bestående av karakterer. Hvilke ruter som skal være hhv. åpne og lukkede
bestemmes delvis av enkle regler, og delvis av tilfeldigheter.
3
Som symbol på hhv. en åpen og en lukket rute brukes karakterene ’O’ (stor ’o’) og
’X’ (stor ’x’). Derfor kan starten av filen oppg2.py gjerne inneholde kodelinjene:
ÅPEN = 'O'
LUKKET = 'X'

"""

#%% Globale variabler

ÅPEN = "O"
LUKKET = "X"

#%% Oppgave 2 a)
"""
Skriv en funksjon skriv(kryssord) som får en todimensjonal liste svarende
til et kryssordmønster som parameter, og som skriver mønsteret ryddig ut i
konsollen.
"""
def skriv(kryssord):
    """
    Parameters
    ----------
    kryssord : List
        En 2d liste med X eller O

    Returns
    -------
    None. Skriver ut 2d listen som ett rutenett
    """
    # Bruker to looper
    for y in kryssord:
        for x in y:
            # Printer med ekstra parameteren "end="""
            print(x, end="")
        print()

#%% Oppgave 2 b)
"""
Rutene i kryssordet identifiseres av to indekser. Første indeks gir 
radnummeret (0 er øverste rad, antall rader minus en er nederste rad). Andre indeks
gir kolonnenummeret (0 er kolonnen lengst til venstre, antall kolonner minus 
en er kolonnen lengst til høyre). Skriv en funksjon har_nabo(kryssord,
rad, kol) som tar et rutemønster som første parameter, og indeksene til en
rute i kryssordet som de to siste parametrene. Funksjonen skal returnere True
dersom ruten i rad rad og kolonne kol har en åpen naborute (over, under, til
venstre eller til høyre). I motsatt tilfelle skal False returneres.
"""
def har_nabo(rutenett, rad, kol):
    """
    Parameters
    ----------
    rutenett : List
        2d list
    rad : int
        rad posisjon for elementet som skal sjekkes om har ÅPEN'e naboer over/under/h/v
    kol : int
        kolonne posisjon for elementet som skal sjekkes om har ÅPEN'e naboer over/under/h/v

    Returns
    -------
    bool
        True om elementet har naboer, false om elementet ikke har naboer
        over/under/sidene(altså ligger på ytterkant av rutenettet)

    """
    
    
    # Sjekk om venstre, høyre, over eller under, er ÅPEN(O)
    # (NB ÅPEN/LUKKET er en globale variabeler, og burde nok heller vært inne
    # i denne funksjonen)
    # returner True, så fort en finner en ÅPEN.  Finnes ingen ÅPEN,
    # returner False
    if rad - 1 >= 0:
        if rutenett[rad - 1][ kol] == ÅPEN:
            return True;
    if rad + 1 < len(rutenett):
        if rutenett[rad + 1][kol] == ÅPEN:
            return True;
    if kol - 1 >= 0:
        if rutenett[rad][kol - 1] == ÅPEN:
            return True;
    if kol + 1 < len(rutenett[0]):
        if rutenett[rad][kol + 1] == ÅPEN:
            return True;
    return False
    

#%% Oppgave 2 c)
"""
Skriv en funksjon lag_kryssord(m, n) som returnerer en todimensjonal liste
svarende til et kryssordmønster med m rader og n kolonner. Om en rute er
åpen eller lukket skal være tilfeldig, og sannsynligheten for at den er åpen
skal være like stor som at den er lukket. Funksjonen skal returnere det genererte kryssordmønsteret.
"""
def lag_kryssord(m,n):
    """
    Parameters
    ----------
    n : int
        rutenettets lengde i x rettning
    m : int
        rutenettets lengde i y rettning

    Returns
    -------
    resultatListe : List
        en 2d liste med tilfeldig X og O 

    """
    resultatListe = []
    # loop i en loop som genererer en 2d liste
    # ÅPEN/LUKKET bestemmes av randint 0 eller 1
    for j in range(m):
        resultatListe.append([])
        for i in range(n):
            r = random.randint(0, 1)
            if r == 0:
                resultatListe[j].append(ÅPEN)
            else:
                resultatListe[j].append(LUKKET)
                
    
    return resultatListe

#%% Oppgave 2 d)
"""
Kryssordleverandøren vil ikke ha løsningsord på bare en bokstav. Derfor ber
hun om at vi ikke lager kryssordmønster der det finnes åpne ruter uten åpne
naboruter (over, under, til venstre eller til høyre). For et eksempel på en slik
forbudt rute, se ruten i rad 0 og kolonne 0 (dvs. øverst i venstre hjørne) i
kryssordet på slutten av oppgave 1c. Skriv en funksjon fyll(kryssord) som
tar et rutemønster som parameter, og som lukker alle åpne ruter som ikke
har åpne naboruter. Antall ruter som får ny verdi skal returneres.
"""
def fyll(kryssord):
    resultat = 0
    # Looper gjennom 2d listen og kjører "har_nabo" funksjonen
    # på parameter listen der elementet er ÅPEN.  Returnerer den 
    # False, har vi ikke naboer som er åpne, og vi setter elementet
    # til LUKKET.  Og vi teller hvor mange ganger vi gjør dette i resultat
    for j in range(len(kryssord)):
        for i in range(len(kryssord[0])):
            if kryssord[j][i] == ÅPEN:
                if(har_nabo(kryssord, j, i) != True):
                    resultat +=1
                    kryssord[j][i] = LUKKET
    return resultat

#%% 

def main():
    print("Main running")
    


#%% Kaller main funksjonen om denne filen blir kjørt
    
if __name__ == "__main__":
    main()