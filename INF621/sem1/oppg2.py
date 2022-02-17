# -*- coding: utf-8 -*-
"""
Created on Thu Nov 11 13:33:41 2021

@author: Lars Holen

INF621 - Høstsemesteret 2021

Oppgave 2

I denne oppgaven skal vi behandle data fra en simulert fotoboks. Fotoboksen lagrer
data om biler som passerer en veistrekning med to felt. Dataen som fotoboksen har
samlet opp finner du i filen fotoboks.txt. Du bør gjøre deg kjent med innholdet i
filen før du begynner å løse oppgavene.
Hver linje i filen fotoboks.txt beskriver en bil som passerer fotoboksen. En 
passering er beskrevet med et tidspunkt, et skiltnummer og farten til bilen (målt til
nærmeste hele km/t). Den samme bilen kan passere fotoboksen flere ganger. To
passeringer kan være loggført til nøyaktig samme tidspunkt. Den samme bilen kan
ikke passere fotoboksen to ganger til samme tidspunkt.

"""

#%% Imports

from datetime import datetime
import locale
# Setter culture til norsk, for å få norske dager/månder i datetime
locale.setlocale(locale.LC_ALL, "no_NO")

#%% Oppgave 2. a)
"""
) Vi vil lese informasjon fra filen fotoboks.txt og lagre den i en ordbok.
Forklar kort (ca. 1 setning per svar) hvorfor hverken passeringstidspunkt 
eller registreringsnummer bør brukes som nøkkel alene i denne ordboken. 
Forklar også hvorfor det er trygt å bruke tupler (passeringstidpunkt, 
registreringsnummer) som nøkler i ordboken. Lag en funksjon svar_paa_2a() 
som printer svaret ditt:

In [4]: svar_paa_2a()
Tidspunkt bør ikke brukes som nøkkel alene fordi (ditt svar)
Bilnummer bør ikke brukes som nøkkel alene fordi (ditt svar)
Tuplen kan brukes som nøkkel fordi (ditt svar)
"""
def svar_paa_2a():
    print("Spørsmål 1:")
    print("Tidspunkt bør ikke brukes som nøkkel alene fordi to passeringer\nkan være loggført til nøyaktig samme tidspunkt\n")
    print("Spørsmål 2:")
    print("Bilnummer bør ikke brukes som nøkkel alene fordi den samme bilen\nkan passere flere ganger.\n")
    print("Spørsmål 3:")
    print("Tuplen (passeringstidpunkt,registreringsnummer) kan brukes som\nnøkkel fordi samme bil kan ikke passere flere ganger på samme tidspunkt.\n")

#%% Oppgave 2. b)
"""
Hver av linjene i filen fotoboks.txt er skrevet på det følgende formatet:
'dd.mm.yyyy-TT:MM:SS registreringsnummer fart'. Ingen av registreringsnumrene inneholder mellomrom.
Lag en funksjon hent_fotoboksdata() som leser fra filen fotoboks.txt og som
returnerer informasjonen lagret i denne filen i form av en ordbok. Nøklene i ordboken
skal være tupler bestående av passeringstidspunkt (i form av et datetime objekt)
og et registreringsnummer (i form av en streng). Verdien til nøklene skal være farten
bilen hadde under denne målingen, målt til nærmeste hele kilometer pr. time.

In [5]: målinger = hent_fotoboksdata()
In [6]: målinger[(datetime(2021, 11, 8, 12, 24, 28), 'ST181525')]
Out[6]: 80

NB!!!!!!!!!!!!!! 2021, 11, 8, 12, 24, 28), 'ST181525' eksisterer
ikke i listen og gir KeyError ikke 80!  Ikke så snilt i en oppgave.
2021, 11, 11, 12, 24, 28), 'ST181525' derimot gir 80.

"""
def hent_fotoboksdata():
    # Oppretter en dictionary
    resultatDic = {}
    
    # Åpner filen
    with open("fotoboks.txt") as fil:
         # Looper gjennom alle linjene
        for linje in fil:
            # Fjerner newline(\n)
            linje = linje.strip("\n")
            # Deler linjen opp i ord
            tidNummerFart = linje.split(" ")
            # Lager en tuple av datetime object fra første element i tidNummerFart og
            # registreringsnummeret og bruker den som key, legger til fart som value 
            resultatDic.update({(datetime.strptime(tidNummerFart[0],'%d.%m.%Y-%H:%M:%S'),tidNummerFart[1]): tidNummerFart[2] })
    return resultatDic

#%% Oppgave 2. c)
"""
La målinger være en ordbok lik den som skal bli returnert av funksjonen
hent_fotoboksdata() og la start_t og slutt_t være to datetime objekter. Lag
en funksjon antall_bøter(start_t, slutt_t, målinger) som returnerer antall
passeringer i målinger som ble loggført i tidsrommet fra (og med) start_t til (men
ikke med) slutt_t hvor farten til kjøretøyet var over 80 km/t.
In [7]: start_t = datetime(2021, 11, 8, 0, 0, 0)
In [8]: slutt_t = datetime(2021, 11, 15, 0, 0, 0)
In [9]: antall_bøter(start_t, slutt_t, målinger)
Out[9]: 267

"""
def antall_bøter(start_t, slutt_t, målinger):
    # Definerer return verdien
    antallBøter = 0
    for måling in målinger:
         tid = måling[0]
         fart = int(målinger[måling])
         if tid < slutt_t and tid > start_t and fart > 80:
             antallBøter += 1
        
         
    
    return antallBøter

#%% Oppgave 2. d)
"""
Lag en funksjon fartsbøter(målinger) som oppretter en fil som heter
bøter_per_dag.txt. Denne filen skal inneholde informasjon om antall ganger et
kjøretøy passerte fotoboksen med en hastighet over 80 km/t på de ulike dagene fra
og med 8. november 2021 til og med 14. november 2021. Om du skriver følgende i
konsollen:
In [10]: målinger = hent_fotoboksdata()
In [11]: fartsbøter(målinger)

Filinnhold:
Mandag 08. november: 19 bøter
Tirsdag 09. november: 17 bøter
Onsdag 10. november: 39 bøter
Torsdag 11. november: 36 bøter
Fredag 12. november: 45 bøter
Lørdag 13. november: 60 bøter
Søndag 14. november: 51 bøter
"""
def fartsbøter(målinger):
    # Definerer en liste for bøter med Bot objekter, klassen er definert under
    # for å forenkle sortering etter dato
    botListe = []
    # Looper gjennom målinger dictionary'en 
    for k, v in målinger.items():
        # Tester om farten var over 80, siden vi ikke trenger de som er under
        if int(v) > 80:
            # Legger til en bot i botListe'n
            botListe.append(Bot(k[1], k[0], v))
    # sorterer botListe etter dato
    botListe.sort(key=lambda r: r.dato)
    
    # Lager en dictionary for å lagre dags datoer og antall bøter på dagen
    bøterEtterDag = {}
    for bot in botListe:
        # sjekker om dato(uten timer/min/sek eksisterer i dictionary)
        if bot.dato.date() in bøterEtterDag:
            # Eksisterer den, legg til 1 i verdien
            bøterEtterDag[bot.dato.date()] += 1
        else:
            # Eksisterer ikke, opprett ny key etter date og gi verdien 1
            bøterEtterDag.update({bot.dato.date(): 1})
    # Åpner fil for skriving
    with open("bøter_per_dag.txt", mode="w") as fil:
        # Looper gjennom dictionary og skriver inn formatert tekst.
        # NB korriger tekstformat for å ta med årstall dersom funksjonen 
        # brukes på lister som går over flere kalenderår
        for k,v in bøterEtterDag.items():
            fil.write(str(k.strftime("%A %d. ")).title() + str(k.strftime("%B: ")) + str(v) + " bøter\n")
        
class Bot:
  def __init__(self, skiltnummer, dato, fart):
    self.skiltnummer = skiltnummer
    self.dato = dato        
    self.fart = fart
    
   

#%% Main  


def main():
    svar_paa_2a()
    målinger = hent_fotoboksdata()
    print("ST181525 kjørte i ", målinger[(datetime(2021, 11, 11, 12, 24, 28), 'ST181525')], "km/t ved passeringen klokken 12:24:28 den 11.11.2021")
    start_t = datetime(2021, 11, 8, 0, 0, 0)
    slutt_t = datetime(2021, 11, 15, 0, 0, 0)
    print("Antall bøter i perioden: ", antall_bøter(start_t, slutt_t, målinger))
    målinger = hent_fotoboksdata()
    fartsbøter(målinger)
    
  
    
if __name__ == "__main__":
    main()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    