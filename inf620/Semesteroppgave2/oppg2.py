# -*- coding: utf-8 -*-
"""
Created on Tue Oct  5 22:35:50 2021

@author: Lars Holen

Semesteroppgave 2
INF620 - Høstsemesteret 2021

"""
#%% Imports
from random import randint
from matplotlib import pyplot as plt

#%%
"""
Oppgave 2. a):

Skriv en funksjon kast som tar en heltallsparameter n, og som returnerer 
et kast med n terninger i form av en liste med n tilfeldige heltallsverdier
i intervallet 1–6

"""

def kast(n):
    """
    Parameters
    ----------
    n : int
        Antall 6 sidete terninger man ønsker resultatet av.

    Returns
    -------
    result : List
        Liste av terningkastene.

    """
    # lager result liste
    result = []
    # kjører en loop n ganger
    for i in range(n):
        # Legger til en tilfeldig verdi mellom 1-6
        result.append(randint(1, 6))
    # returnerer listen med n terningkast
    return result

#%% 
"""
Oppgave 2. b):

Skriv en funksjon finn_antall som tar som parameter en liste (terninger)
med terningkast av den typen funksjonen kast returnerer. Funksjonen skal
returnere en heltallsliste (antall) av lengde 6. Første element i antall, dvs.
antall[0], skal være lik antall enere i terninger. Neste element i antall,
dvs. antall[1], skal være lik antall toere i terninger, osv., og siste element
i antall, dvs. antall[5], skal være lik antall seksere i terninger.

"""
def finn_antall(terninger):
    """
    Parameters
    ----------
    terninger : List
        Liste med forskjellige terningkast, med verdier fra 1-6

    Returns
    -------
    result : List
        Liste med antall ganger terningverdiene gjentar seg
        [1,0,0,0,0,5] betyr 1 ener og 5 seksere
    """
    # Lager en resultat liste med 6 elementer med verdi 0
    result = [0,0,0,0,0,0]
    # Looper gjennom terningliste og legger til 1 i det element
    # som svarer til terningverdien
    for i in terninger:
        result[i-1] += 1
    return result

#%% 
"""
Oppgave 2. c):

Skriv en funksjon finn_flest som tar som parameter en heltallsliste
(antall) av den typen funksjonen finn_antall returnerer. Husk at den listen
inneholder antall enere, toere, . . ., seksere. Funksjonen skal returnere hvilken
terningverdi (1–6) som forekommer flest ganger.

"""
def finn_flest(antall):
    """
    Parameters
    ----------
    antall : List
        Liste med heltall som inneholder antall ener kast, toere, treere osv

    Returns
    -------
    indexavantallverdi : int
        Returnerer den terningverdien som ble kastet flest ganger.  Når
        to har samme antall, returneres den siste i listen.

    """
    # sorterer antall listen
    antallverdi = 0
    indexavantallverdi = -1
    # Looper gjennom listen og får både index og element med enumerate()
    for index, i  in enumerate(antall):
        # Tester om i/elementet er større eller lik lagrede antallverdi
        # Større eller lik, så returneres siste element med flest antall
        # Bare større enn, ville returnert den første
       if(i >= antallverdi):
           #  Lagrer høyeste antallverdi og indexen for denne
           antallverdi = i;
           indexavantallverdi = index
    # returnerer indexAvantallverdi + 1 siden 0'te element tilsvarer terningverdi 1 osv
    return indexavantallverdi + 1   
    
#%% 
"""
Oppgave 2. d):

Skriv en funksjon nytt_kast som tar som første parameter en liste
(terninger) med terningkast av den typen funksjonen kast returnerer. Som
andre parameter tar funksjonen en heltallsparameter (spar) med verdi i 
intervallet 1–6. Funksjonen gjør et nytt kast med alle terningene som ikke har
samme verdi som spar, og oppdaterer verdien i terninger til det nye kastet.

"""
def nytt_kast(terninger, spar):
    """
    Parameters
    ----------
    terninger : List
        En liste med terningkast fra e 6 sidet terning.
    spar : int
        Bestemmer hvilken terning som skal ikke kastes oppigjen.

    Returns
    -------
    None.  Men listen terninger blir oppdatert med eventuelle nye kast

    """
    
    # Looper gjennom listen med index
    for i in range(len(terninger)):
        # om terningverdien i listen ikke er lik "spar", setter vi listens
        # element til ett nytt kast, som vi får fra funksjonen kast.  Som 
        # returnerer en liste.  Derav (1) en terning, og [0] for vi vil ha verdien
        # i første(og eneste) element i resultatet til kast funksjonen
        if(terninger[i] != spar):
            terninger[i] = kast(1)[0]
            
#%%
"""
Oppgave 2. e):

Skriv en funksjon yatzy som tar et antall (n) terninger som parameter,
og som lar brukeren trille terningene like til hun får yatzy, dvs. alle n 
terningene viser samme verdi. I hver omgang skal funksjonen velge en verdi 1–6
som skal spares, slik at et maksimalt antall terninger som viser samme verdi
legges til side. Funksjonen skal returnere antall omganger som minst en 
terning måtte kastes før yatzy ble oppnådd. I hver omgang skal funksjonen skrive
ut hva terningene viser

"""
def yatzy(n):
    # Setter variabler og tar første kast
    terningListe = kast(n)
    print(terningListe)
    # Vi sparer på verdien vi får fra finn_flest-->finn_antall-->terningList
    spar = finn_flest(finn_antall(terningListe))
    antallKast = 1
    alleLike = False
    
    # Tester om vi fikk alle like på første kast
    if(finn_antall(terningListe)[spar - 1] == n):
        alleLike = True
        
    # Begynner loopen som kaster til alle har lik verdi
    while(not alleLike):
        # Tar ett nytt kast, men sparer på "spar" verdien
        # skriver terningene til skjerm og legger til 1 på antall kast
        nytt_kast(terningListe, spar)
        print(terningListe)
        antallKast += 1
        # Sjekker om vi har fått yatzy
      
        if(finn_antall(terningListe)[spar - 1] == n):
            alleLike = True
        else:
            # Sjekker om en annen verdi har fått flere tilfeller enn det 
            # som er lagret i "spar"
            spar = finn_flest(finn_antall(terningListe))
    return antallKast
        
#%%
"""
Oppgave 2. f):
    
Bruk funksjonen yatzy ved å kalle den i slutten av programfilen oppg2.py.
"""
#heltall1 = 0
while True:
    try:
        heltall1 = int(input("Antall terninger: "))
        print("Takk!")
        break
    except:
            print("Det er ikke ett heltall!")
antallKast = yatzy(heltall1)
print("Yatzy med", heltall1, "terninger på", antallKast, "kast.") 




"""

Utkommentert ekstraoppgave

 Oppgave 2. g):

# Lager en liste med elementer fra 1 til 100
interval = list(range(1,101))
omganger = []
for i in interval:
    fyller i resultatet fra yatzy(i) i omganger listen
    omganger.append(yatzy(i))                

# plotter
plt.close("all")
plt.figure(1, figsize=(12,9))
plt.plot(interval, omganger, "r*-")
plt.xlabel("Antall terninger brukt")
plt.ylabel("Antall kast for å få yatzy")
plt.grid()
plt.show()

"""
   
    
   
    
   
    
   
    
   
    
   
    
   
    
   
    
   
    
   
    
   
    
   
    
   
    
   
    
   
    
   
    
   
    
   