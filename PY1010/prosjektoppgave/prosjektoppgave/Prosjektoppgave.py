# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 13:05:20 2021

@author: Lars Holen

Prosjektoppgave

Support dashboard.
Du skal her utføre diverse analyser av data som er loggført for supportavdelingen ved telefonselskapet MORSE. 
Enhver kundehenvendelse til MORSE blir loggført i en xlsx-fil og du skal i dette prosjektetjobbe med 
dataloggen for uke 24.Filen ‘support_uke_24.xlsx’ finner dusammen med prosjektoppgaveni Canvas under 
menyenOppgaver-> Prosjektoppgaven, og filen er organisert på følgende måte:Kolonne 1: Ukedag henvendelsen 
fant stedKolonne 2: Klokkeslett kunden tok kontakt med supportavdelingenKolonne 3: Samtalens varighetKolonne
4: Kundens tilfredshet (skala fra 1-10 hvor 1indikerer svært misfornøyd og 10 indikerer svært fornøyd). 
Merk: kolonne 4 er ikke komplett da mange kunderunnlater å gi tilbakemelding på sin tilfredshet.


"""

# %% Importerer pakker jeg trenger:
    
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# %% Oppgave Del a)
"""
Skrivet program som leser inn filen‘support_uke_24.xlsx’ og lagrer data frakolonne 1 i en array med variablenavn
‘u_dag’, dataen i kolonne 2 lagres iarrayen ‘kl_slett’, data i kolonne 3 lagres i arrayen ‘varighet’ og dataen 
i kolonne 4 lagres i arrayen ‘score’. Merk: filen ‘support_uke_24.xlsx’ må ligge i samme mappe som 
Python-programmet ditt.
"""
# Definerer variabler/laster inn excelfilen og fordeler kolonnene i rette variabel


fil = pd.read_excel("support_uke_24.xlsx") # laster inn filen med pandas
fil.fillna(0, inplace = True) # Setter tomme celler til 0(der kundene ikke har gitt tilbakemelding), for å unngå feil

u_dag = fil[fil.columns[0]].to_numpy() #trekker ut kolonne 0 pandas serien og gjor den om til numpy array
kl_slett = fil[fil.columns[1]].to_numpy() #trekker ut kolonne 1 pandas serien og gjor den om til numpy array
varighet = fil[fil.columns[2]].to_numpy() #trekker ut kolonne 2 pandas serien og gjor den om til numpy array
score = fil[fil.columns[3]].to_numpy() #trekker ut kolonne 3 pandas serien og gjor den om til numpy array


# %% Oppgave Del b)
"""
Skrivet program som finner antall henvendelser for hver de 5 ukedagene. 
Resultatet visualiseres ved bruk av et histogram(‘søylediagram’).
"""

numHenvendelserMandag = (u_dag == "Mandag").sum() # Finner antall ganger dagene er i u_dag arrayen
numHenvendelserTirsdag = (u_dag == "Tirsdag").sum() # Og lagrer verdiene i numHenvendelser[DAG] variablen
numHenvendelserOnsdag = (u_dag == "Onsdag").sum()
numHenvendelserTorsdag = (u_dag == "Torsdag").sum()
numHenvendelserFredag = (u_dag == "Fredag").sum()

labelsHistogram = ["Mandag", "Tirsdag", "Onsdag", "Torsdag", "Fredag"]
numHenvendelser = [numHenvendelserMandag, numHenvendelserTirsdag, numHenvendelserOnsdag, numHenvendelserTorsdag, numHenvendelserFredag]
plt.close("all")
plt.figure(1, figsize=(12,9)) # setter opp plottvindu
plt.title("Oppgave del b) Antall henvendelser fordelt på dagene: ")
plt.bar(labelsHistogram, numHenvendelser, color ="green")
plt.show()


# %% Oppgave Del c)
"""
Skrivet program som finnerminste og lengste samtaletid som er loggført for uke24. 
Svaret skrives til skjermmed informativ tekst. 
"""

minVarighet = 0
minVarighetIndex = 0
maxVarighet = 0
maxVarighetIndex = 0



for i in range(len(varighet)):
    if i == 0:
        minVarighet = varighet[i] # Naar i==0, er det den første verdien vi ser på
        maxVarighet = varighet[i] # Da er min og max den samme verdien
        minVarighetIndex = i # Lagrer indexen for minVarighet
        maxVarighetIndex = i # Lagrer index for maxVarighet
    else:
        if minVarighet > varighet[i]: # Variablene er type string, men > og < ser ut til å fungerer alikevel i python
            minVarighet = varighet[i]
            minVarighetIndex = i
            
        if maxVarighet < varighet[i]:
            maxVarighet = varighet[i]
            maxVarighetIndex = i
           
print("\nOppgave del c):")              
print("Minste samtaletid var på", minVarighet, "og har index", minVarighetIndex)   
print("Lengste samtaletid var på", maxVarighet, "og har index", maxVarighetIndex)


# %% Oppgave Del d)
"""
KREVENDE:Skriv et program som regner ut gjennomsnittlig samtaletid basert på alle henvendelser i uke 24. 
"""

sekunder = np.zeros(len(varighet)); # Definerer en array som skal holde varigheten i sekunder 

for j in range(len(varighet)):              # Looper gjennom arrayen med varighet, hvor tiden er lagret som str i "tt:mm:ss" format
    tid = np.array(varighet[j].split(":"))  # Deler opp tids string'en i tre deler, delt på ":".  Så timer, minutter og sekunder blir delt i en ny array
    ts = int(tid[0])*60**2                  # Tar time verdien, gjør den om til int, og ganger med 3600(60 min * 60 sek) for å få antall sekunder 
    ms = int(tid[1])*60                     # Tar minuttene, gjør om til int, og ganger med 60 for å få sekunder
    s = int(tid[2])                         # Tar sekundene og lagrer de
    sekunder[j] = ts + ms + s               # Legger sammen timer i sekunder, minutter i sekunder og sekunder for å få totalen i sekunder.  Og lagrer det i en sekunder arrayen
     
gjennomsnittsVarighetSekunder = int(np.round(np.average(sekunder))) # Bruker, np.average for å finne gjennomsnittet i arrayen. round for å runde av.  Og int for å ikke lagre noen desimaler(ikke få ".0")

timer = np.floor(gjennomsnittsVarighetSekunder/3600)                # Regner så ut antall hele timer
minu = np.floor((gjennomsnittsVarighetSekunder - timer*3600)/60)    # Regner ut antall hele minutter(trekker fra timene i sekunder først)
seku = gjennomsnittsVarighetSekunder - (timer * 3600) - (minu * 60) # Trekker fra timer i sekunder og minutter i sekunder, så sitter en igjen med resterende sekunder 

# Lager xx:yy:zz format på tiden, lagret i en string
timerStr = str(int(timer))      # Gjør om timer int(for å få ett heltall uten desimaler), så til en string
if len(timerStr) == 1:          # Sjekker om string har bare ett tall
    timerStr = "0" + timerStr   # Legger til en "0" om det var bare ett tall

minutterStr = str(int(minu))    # Utfører samme operasjon på minutter og sekunder som ble gjort på timer
if len(minutterStr) == 1:
    minutterStr = "0" + minutterStr
    
sekunderStr = str(int(seku))
if len(sekunderStr) == 1:
    sekunderStr = "0" + sekunderStr

gjennomsnittsVarighetStr = timerStr + ":" + minutterStr + ":" + sekunderStr # Legger sammen timer, minutter og sekunder.  Og plasserer ":" mellom
  
print("\nOppgave del d):")
print("Gjennomsnittstid pr henvendelse:", gjennomsnittsVarighetStr)
    

# %% Oppgave Del e)
"""
Supportvaktene i MORSE er delt inn i 2-timers bolker: kl 08-10, kl 10-12, kl 12-14 og kl 14-16. 
Skriv et programsom finner det totale antall henvendelser supportavdelingenmottokfor hver avtidsrommene
 08-10, 10-12, 12-14 og 14-16for uke 24. Resultatet visualiseres ved bruk av et sektordiagram (kakediagram).
"""

# Dele opp henvendelser i vaktene 8-10, 10-12,12-14,14-16 og visualisere i ett sektordiagram(kakediagram)
vakt_labels = ["Vakt 8-10", "Vakt 10-12", "Vakt 12-14", "Vakt 14-16"]
vakt_8_10 = 0
vakt_10_12 = 0
vakt_12_14 = 0
vakt_14_16 = 0

for k in range(len(kl_slett)):
    if kl_slett[k][0]== "0" and (kl_slett[k][1]== "8" or kl_slett[k][1]== "9"):
        vakt_8_10 += 1
    elif kl_slett[k][0]== "1" and (kl_slett[k][1]== "0" or kl_slett[k][1]== "1"):
        vakt_10_12 += 1
    elif kl_slett[k][0]== "1" and (kl_slett[k][1]== "2" or kl_slett[k][1]== "3"):
        vakt_12_14 += 1
    elif kl_slett[k][0]== "1" and (kl_slett[k][1]== "4" or kl_slett[k][1]== "5" or kl_slett[k][1]== "6"):
        vakt_14_16 += 1
    
vaktData = [vakt_8_10, vakt_10_12, vakt_12_14, vakt_14_16]
#print("\n", vakt_8_10, "\n", vakt_10_12, "\n", vakt_12_14, "\n", vakt_14_16, "\n", len(kl_slett), "\n" )
plt.figure(2, figsize=(12,9)) # setter opp plottvindu
plt.title("Oppgave del e): Antall henvendelser fordelt på vaktene: ")
plt.pie(vaktData, labels=vakt_labels, autopct="%.1f%%")
plt.show()  


# %% Oppgave Del f)
"""
Kundens tilfredshet loggføres som tall fra 1-10 hvor 1indikerer svært misfornøyd og 10 indikerer svært 
fornøyd. Disse tilbakemeldingene skal så overføres til NPS-systemet (Net Promoter Score). 
NPS-systemet er konstruert på følgende måte:Score 1-6 oppfattes som at kundenernegativ 
(vil trolig ikkeanbefale MORSE til andre).Score 7-8 oppfattes som et nøytralt svar.Score 9-10 
oppfattes som at kunden er positiv (vil trolig anbefale MORSE til andre).  Supportavdelingens NPS 
beregnes som et tall, prosentandelen positive kunder minus prosentandelen negative kunder. 
Ved en formel kan dette gis slik:NPS = % positive kunder -% negative kunder
"""
# Definerer variabler for de forskjellige score inndelingene
ikkesvart = 0
negativ = 0
noeytral = 0
positiv = 0

# Looper gjennom alle stemmene i score arrayen
# Og sjekker i hvilken kategori de skal i, og legger til 1 i rett kategori
for stemme in score:
    if stemme == 0:
        # Kunden har ikkesvart.  Unødvendig variabel, men lager den om en skulle få bruk for den
        # senere eller vel testing av resultatene
        ikkesvart += 1
    elif stemme > 0 and stemme <= 6:
        # Kunden er negativ
        negativ += 1
    elif stemme > 6 and stemme <= 8:
        # Kunden er nøytral
        noeytral += 1
    elif stemme > 8 and stemme <= 10:
        # Kunden er fornøyd
        positiv += 1

# Legger sammen alle stemmer vi skal bruke for å finne NPS(ekskluderer altså "ikkesvart")
totaltStemmer = negativ + noeytral + positiv

# Regner ut prosentvis score mot totalStemmer
negativProsent = negativ/totaltStemmer * 100
noeytralProsent = noeytral/totaltStemmer * 100
positivProsent = positiv/totaltStemmer * 100

# Beregner NPS
nps = positivProsent - negativProsent
  
print("\nOppgave del f):")        
print("NPS(avrundet):\t", int(np.round(nps)))       # Bruker int, for å ikke ha med desimaler

print("\nEkstra informasjon:")
print("detractors: \t", str(negativ).rjust(5),"  \t", str(np.round(negativProsent))+"%" ) # Gjør om tallene til string, for å kunne 
print("passives:   \t", str(noeytral).rjust(5),"  \t", str(np.round(noeytralProsent))+"%" ) # bruke rjust for å høyre justere de
print("promoters:  \t", str(positiv).rjust(5),"  \t", str(np.round(positivProsent))+"%" )   # så det ser penere ut.
print("total:      \t", str(negativ + noeytral + positiv).rjust(5), "   \t100.0%")
print("\nIkke stemt:  \t", str(ikkesvart).rjust(5))

en = (score == 1).sum()
print("\nValgt 1:\t", str((score == 1).sum()).rjust(2), "\t-")
print("Valgt 2:  \t", str((score == 2).sum()).rjust(2), "\t-")
print("Valgt 3:  \t", str((score == 3).sum()).rjust(2), "\t- =Detractors")
print("Valgt 4:  \t", str((score == 4).sum()).rjust(2), "\t-")
print("Valgt 5:  \t", str((score == 5).sum()).rjust(2), "\t-")
print("Valgt 6:  \t", str((score == 6).sum()).rjust(2), "\t-")
print("Valgt 7:  \t", str((score == 7).sum()).rjust(2), "\t* =Passives")
print("Valgt 8:  \t", str((score == 8).sum()).rjust(2), "\t*")
print("Valgt 9:  \t", str((score == 9).sum()).rjust(2), "\t+ =Promoters")
print("Valgt 10: \t", str((score == 10).sum()).rjust(2), "\t+")
































