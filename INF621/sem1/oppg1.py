# -*- coding: utf-8 -*-
"""
Created on Tue Nov  9 16:14:42 2021

@author: Lars Holen

INF621 - Høstsemesteret 2021

Oppgave 1
Svar leveres på fil med navn oppg1.py. Denne oppgaven er en øvelse i å lese
fra/skrive til en tekstfil.

"""

#%% Imports:
from datetime import datetime
import string

import locale

# Setter culture til norsk, for å få norske dager/månder i datetime
locale.setlocale(locale.LC_ALL, "no_NO")
    

#%% Oppgave 1. a)
"""
Lag en funksjon fil_info(filnavn) som printer hvor mange tegn, ord
og linjer filen med navn filnavn inneholder. Linjeskift telles ikke som tegn.
In [1]: fil_info('test.txt')
Det er 56 tegn, 12 ord og 7 linjer i filen test.txt.

"""
def fil_info(filnavn):
    antallTegn = 0
    antallLinjer = 0
    antallOrd = 0
    # Åpner filen
    with open(filnavn) as fil:
        # Looper gjennom alle linjene
        for linje in fil:
            # Fjerner newline(\n)
            linje = linje.strip("\n")
            # Deler linjen opp i ord
            word = linje.split()
            # teller en linje for hver gang loopen går
            antallLinjer += 1
            # Legger til antall ord 
            antallOrd += len(word)
            # Legger til antall tegn
            antallTegn += len(linje)
    # Printer ut resultatet til skjerm
    print("Det er", antallTegn, " tegn,", antallOrd, "ord og", antallLinjer, "linjer i filen", filnavn + ".") 

#%% Oppgave 1. b)
"""
Lag en funksjon tidspunkt() som oppretter en fil med navnet nå.txt.
Denne filen skal inneholde informasjon om tidspunktet filen ble opprettet på. Bruk
formatet 'Fil opprettet ukedag (d)d. månedsnavn yyyy klokken TT:MM:SS.'.
Hvis tidspunkt() kjøres den 18.11.21 kl. 15:59:55 skal filen nå.txt inneholde:
Fil opprettet torsdag 18. november 2021 klokken 15:59:55.

"""
def tidspunkt():
    # Åpner filen eller lager en ny i "write" mode for å skrive over eventuell
    # eldre tekst
    with open("nå.txt", mode="w") as fil:
        # Lager et datotid objekt for dette tidspunktet
        datotid = datetime.now()
        # Skriver formatert tekts med dato og tid til filen
        fil.write(datotid.strftime("Fil opprettet %A %w. %B %Y klokken %X")) 

#%% Oppgave 1. c)
"""
Lag en funksjon antall(filnavn) som returnerer en ordbok med bokstaver fra 'a' til 'å' 
som nøkler og antallet forekomster av de ulike bokstavene i
filnavn som verdi.
In [2]: antall('test.txt')
Out[2]: {'a': 1, 'b': 0, 'c': 0, 'd': 4, 'e': 10, 'f': 1,
'g': 0, 'h': 2, 'i': 4, 'j': 0, 'k': 3, 'l': 2, 'm': 0, 'n': 5,
'o': 2, 'p': 0, 'q': 0, 'r': 2, 's': 2, 't': 7, 'u': 1, 'v': 1,
'w': 0, 'x': 0, 'y': 0, 'z': 0, 'æ': 0, 'ø': 0, 'å': 0}
"""
def antall(filnavn):
    # Oppretter en dictionary med det internasjonale alfabetet
    resultDic = dict.fromkeys(string.ascii_lowercase,0)
    # Legger til norske spesial bokstaver
    resultDic.update({'æ': 0, 'ø': 0, 'å': 0}) 
    bokstavliste = list()
    # Åpner filen
    with open(filnavn) as fil:
        for linje in fil:
            # Lager en liste med alle bokstaver og tegn
            bokstavliste += list(linje)
    # Looper gjennom dictionary
    for key in resultDic:
        # Teller antall ganger "key" dukker opp i bokstavlisten.  Og setter
        # antall som verdi i dictionary
        resultDic[key] = bokstavliste.count(key)
    # Returnerer dictionary med rette verdier.
    return resultDic



#%% 
def main():
    fil_info('test.txt')
    tidspunkt()
    forekomst = antall('test.txt')
    print('Bokstaver som forekommer i fila test.txt sortert etter avtakende forekomst:')
    for bokstav in sorted(forekomst, key=forekomst.get, reverse=True):
        f = forekomst[bokstav]
        if f>0:
            print('%s: %4d' % (bokstav, f))

    
if __name__ == "__main__":
    main()