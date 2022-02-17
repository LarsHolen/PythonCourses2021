# -*- coding: utf-8 -*-
"""
Created on Fri Nov 12 16:06:40 2021

@author: Lars Holen

INF621 - Høstsemesteret 2021

Oppgave 4

I denne oppgaven må du arbeide mer selvstendig enn i de tidligere oppgavene.
Om du har lyst til å utfordre deg selv litt ekstra kan du gjøre et forsøk på å
knekke en kode. Du skal ikke levere noen egen fil for denne bonusoppgaven. Dersom
du klarer å finne krypteringsordboken som ble brukt til å kryptere teksten i filen
kryptert_melding.txt så kan du legge til en funksjon bonus() til slutt i pythonfilen oppgave3.py som returnerer denne ordboken.
I denne siste (frivillige) bonusoppgaven skal vi se hvor utrygt det er å kryptere
meldinger med ‘monoalfabetisk substitusjonchiffer”. Dette skal vi vise ved å bryte
krypteringen på innholdet i filen med navn kryptert_melding.txt. Metoden vi
bruker for å bryte krypteringen heter frekvensanalyse. Du kan lese mer om denne teknikken på wikipedia: https://no.wikipedia.org/wiki/Frekvensanalyse_
(kryptografi)


"""

#%% Imports
import string

#%% Oppgave 4. a)
"""
(0 poeng) Første steg er å finne frekvensen til hver av bokstavene i tekstfilen
en_kryptert_melding.txt. Det er lurt å skrive ut bokstavene og frekvensene i sortert rekkefølge.
Hint: Her kan du bygge videre på funksjonen fra oppgave 1.c

"""
def frekvensPåTegn(filnavn):
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
    for tegn in bokstavliste:
        if tegn not in resultDic:
            resultDic[tegn] = 1
        else:
            resultDic[tegn] += 1
    # Returnerer dictionary med rette verdier.
    return resultDic

#%% Oppgave 4. b)
"""
Den krypterte meldingen er en engelsk setning + en kjent engelsk bok.
I en typisk engelsk tekst er bokstaven e mest vanlig og z minst vanlig. Alfabetet
sortert etter sjeldenhet ser slik ut: e, t, a, o, i, n, s, h, r, d, l ,c, u, m, w, f, g, y, p,
b, v, k, j, x, q, z. Om du er interessert i de eksakte frekvensene til hver bokstav kan
du finne dem her: https://en.wikipedia.org/wiki/Letter_frequency.
Samenlign frekvensene i den krypterte teksten med frekvensen av de ulike bokstaver
i en typisk engelsk tekst. Bruk denne informasjonen til å gjøre en kvalifisert gjettning
på hvilken ordbok som er brukt til å kryptere meldingen.

"""
def les_krypteringsordbok2():
    # Oppretter dictionary som skal returneres
    kryptoDic = {}
    
    # Åpner fil for lesing
    with open("hemmelig_oppg4.txt") as fil:
        # looper gjennom hver linje
        for linje in fil:
            # Fjerner linjeskift/"\n"
            linje = linje.strip("\n")
            # Legger til key/value i dictionary
            kryptoDic[linje[0]] = linje[-1]
    # Returnerer ferdig dictionary
    return kryptoDic

def dekrypter(filnavn, krypteringsordbok):
    # Snur om på key og value i krypteringsordboken
    # Gjør det siden ingen values er like, og kan behandles som unike keys
    dekrypteringsordbok = krypteringsordbok
     # Åpner fil for lesing
    with open(filnavn) as innFil:
        # Åpner fil for skriving
        with open(str("dekryptert_kryptert_" + filnavn), mode="w") as utFil:
            # Looper linjer
            for linje in innFil:
                # Looper gjennom tegnene
                for bokstav in linje:
                    # Ser om tegn/bokstav ikke finnes i ordboken
                    if bokstav not in dekrypteringsordbok:
                        # tegnet er ikke i ordboken, og da skrives den samme
                        utFil.write(bokstav)
                    else:
                        # Vi finner tegnet i ordboken, og bytter den ut med til
                        # hørende tegn i ordboken
                        utFil.write(dekrypteringsordbok[bokstav])
    



#%% main

def main():
    print("Main running")
    print(frekvensPåTegn("en_kryptert_melding.txt"))
    sort_orders = sorted(frekvensPåTegn("en_kryptert_melding.txt").items(), key=lambda x: x[1], reverse=True)
    
    for i in sort_orders:
        print(i[0], i[1])
    krypteringsordbok = les_krypteringsordbok2()
    
    dekrypter('en_kryptert_melding.txt', krypteringsordbok)
    
if __name__ == "__main__":
    main()