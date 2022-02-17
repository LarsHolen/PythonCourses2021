# -*- coding: utf-8 -*-
"""
Created on Fri Nov 12 15:13:35 2021

@author: Lars Holen

INF621 - Høstsemesteret 2021

Oppgave 3

I denne oppgaven skal vi øve enda litt mer på å lese fra og å skrive til filer, denne
gangen ved å se på kryptering. Å kryptere betyr å forsøke å gjøre en melding uleselig
for alle andre enn de som er ment å motta den.
I denne oppgaven skal vi se på en type kryptering som kalles “monoalfabetisk 
substitusjon”. Til tross for det lange navnet så er dette en ganske enkel (men “utrygg”)
måte å kryptere tekst på, hvor man erstatter bokstavene i en tekst med andre
bokstaver. Vi antar at både den som krypterer og den som dekrypterer meldingen
kjenner til hvordan bokstavene byttes ut med hverandre.

"""

#%% Imports

#%% Oppgave 3. a)
"""
Filen hemmelig.txt gir en oppskrift på hvordan du skal kryptere meldinger. 
Gjør deg derfor først kjent med innholdet i filen hemmelig.txt.
Linjene i hemmelig.txt er på formen `"bokstav1" erstattes med "bokstav2"'.
I denne oppgaven skal du lage en funksjon lag_krypteringsordbok() som leser
innholdet i filen hemmelig.txt og som returnerer en ordbok som vi senere skal
bruke til krypteringen. Nøklene i denne ordboken skal være bokstaver og verdien
skal være bokstaven som nøkkelen skal erstattes med i den krypterte meldingen.
In [10]: les_krypteringsordbok()
Out[10]: {'a': 'x', 'b': 'q', 'c': 'w', 'd': 'z', 'e': 'd',
'f': 'b', 'g': 'g', 'h': 'y', 'i': 'u', 'j': 'n', 'k': 'k',
'l': 'i', 'm': 't', 'n': 'e', 'o': 'r', 'p': 'f', 'q': 'l',
'r': 'v', 's': 'm', 't': 'o', 'u': 'c', 'v': 'j', 'w': 'p',
'x': 'h', 'y': 'a', 'z': 's'}
"""
def les_krypteringsordbok():
    # Oppretter dictionary som skal returneres
    kryptoDic = {}
    
    # Åpner fil for lesing
    with open("hemmelig.txt") as fil:
        # looper gjennom hver linje
        for linje in fil:
            # Fjerner linjeskift/"\n"
            linje = linje.strip("\n")
            # Legger til key/value i dictionary
            kryptoDic[linje[0]] = linje[-1]
    # Returnerer ferdig dictionary
    return kryptoDic

#%% Oppgave 3. b)
"""
Lag en funksjon krypter(filnavn, krypteringsordbok) som leser inn
en fil med navn filnavn og oppretter en ny fil med navnet 'kryptert_' + filnavn.
Denne filen skal inneholde den krypterte teksten fra filen filnavn, hvor teksten har
blitt kryptert ved hjelp av ordboken krypteringsordbok av samme type som den
du leste inn i oppgave 3.a. Dersom du kjører koden:

In [11]: krypteringsordbok = lag_krypteringsordbok()
In [12]: krypter('test.txt', krypteringsordbok)

skal det opprettes en fil med navn kryptert_test.txt hvor det står:
ydu
zdood dv de
iuode odkmobui yjrv
zc
kxe odmod krzde
zue



"""
def krypter(filnavn, krypteringsordbok):
    # Åpner fil for lesing
    with open(filnavn) as innFil:
        # Åpner fil for skriving
        with open(str("kryptert_" + filnavn), mode="w") as utFil:
            # Looper linjer
            for linje in innFil:
                # Looper gjennom tegnene
                for bokstav in linje:
                    # Ser om tegn/bokstav ikke finnes i ordboken
                    if bokstav not in krypteringsordbok:
                        # tegnet er ikke i ordboken, og da skrives den samme
                        utFil.write(bokstav)
                    else:
                        # Vi finner tegnet i ordboken, og bytter den ut med til
                        # hørende tegn i ordboken
                        utFil.write(krypteringsordbok[bokstav])

#%% Oppdave 3. c)
"""
Lag en funksjon dekrypter(filnavn, krypteringsordbok) som leser
inn en fil med navn filnavn som inneholder tekst som har blitt kryptert med ordboken krypteringsordbok. Funksjonen dekrypter(filnavn, krypteringsordbok)
skal opprette en ny fil med navn'dekryptert_' + filnavn. Dersom du kjører:
    
In [13]: krypteringsordbok = les_krypteringsordbok()
In [14]: dekrypter('kryptert_test.txt', krypteringsordbok)

skal det opprettes en fil med navn dekryptert_kryptert_test.txt hvor det står:
hei
dette er en
liten tekstfil hvor
du
kan teste koden
din
"""
def dekrypter(filnavn, krypteringsordbok):
    # Snur om på key og value i krypteringsordboken
    # Gjør det siden ingen values er like, og kan behandles som unike keys
    dekrypteringsordbok = {value:key for key, value in krypteringsordbok.items()}
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
    


#%% Oppgave 4/Bonus The quick brown fox jumps over the lazy dog
def bonus():
     # Oppretter dictionary som skal returneres
    kryptoDic = {"c":"e",
                 "m":"t",
                 "t":"a",
                 "y":"o",
                 "i":"n",
                 "l":"i",
                 "a":"h",
                 "v":"s",
                 "d":"r",
                 "j":"d",
                 "p":"l",
                 "n":"u",
                 "b":"m",
                 "h":"w",
                 "s":"c",
                 "f":"f",
                 "q":"g",
                 "x":"y",
                 "k":"p",
                 "g":"b",
                 "z":"v",
                 "w":"k",
                 "u":"x",
                 "o":"q",
                 "e":"j",
                 "r":"z"                              
                 }
    
    return kryptoDic


#%% Main

def main():
    krypteringsordbok = les_krypteringsordbok()
    krypter('test.txt', krypteringsordbok)
    dekrypter('kryptert_test.txt', krypteringsordbok)
    
if __name__ == "__main__":
    main()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    