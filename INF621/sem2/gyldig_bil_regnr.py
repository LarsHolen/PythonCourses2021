# -*- coding: utf-8 -*-
"""
Created on Wed Dec 15 11:09:27 2021

@author: Lars Holen


Som kjennemerke (registreringsnummer) på bilskilt godtar vi alle strengar som består av to store
bokstavar etterfølgd av fem siffer, der første siffer er ulik 0.
Skriv python-kode som les inn ein streng frå brukaren, og som skriv ut om strengen er eit gyldig
kjennemerke eller ikkje.
Eksempelkjøringer:
Registreringsnummer: XY54321
XY54321 er gyldig kjennemerke
Registreringsnummer: AB01234
AB01234 er ikkje gyldig kjennemerke
Registreringsnummer: xyz1234
xyz1234 er ikkje gyldig kjennemerke
Registreringsnummer: R10
R10 er ikkje gyldig kjennemerke
NB: Krava for gyldige kjennemerke er forenkla i denne oppgåva.


"""
def sjekkKjennemerke():
    registreringsnummer = input("Registreringsnummer: ")
    gyldig = True
    # Sjekk om de to første er store bokstaver
    if registreringsnummer[:1].isalpha() == False or registreringsnummer[:2].isalpha() == False:
        gyldig = False
    if registreringsnummer[:1].isupper() == False or registreringsnummer[:2].isupper() == False:
        gyldig = False
    for i in range(4,1):
        if registreringsnummer[i+1:i+2].isdigit() == False:
            print("Numfalse" , registreringsnummer[i+1:i+2])
            gyldig = False
    if gyldig:
        print(registreringsnummer, "er gyldig kjennemerke")
    else:
        print(registreringsnummer, "er ikkje gyldig kjennemerke")
    

def main():
    sjekkKjennemerke()
    
if __name__ == "__main__":
    main()