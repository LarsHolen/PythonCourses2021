# -*- coding: utf-8 -*-
"""
Created on Tue Dec  7 14:28:39 2021

@author: Lars Holen

Øving 4 

Oppgave 1
Terninger 
Skriv en funksjon for hver deloppgave. Svar leveres på fil med navn

"""

#%% Imports

# Importerer randint for å få tilfeldige tall
from random import randint

import numpy as np

# pyplot for plotting av data 
import matplotlib.pyplot as plt

#%% Oppgave 1. a)
"""
Kast ti terninger en etter en. Plott kurver som viser utviklingen av
• gjennomsnittsverdien oppnådd med terningene kastet så langt,
• minimumsverdien oppnådd med terningene kastet så langt, og
• maksimumsverdien oppnådd med terningene kastet så langt.
"""
def plotToKast():
    # Definerer en liste for terningkast
    terningKast = np.zeros([10], dtype=int)
    xLinje = []
    terningKastSnitt = []
    terningKastMinimum = []
    terningKastMaksimum = []
    
    # Looper 10 ganger
    for i in range(len(terningKast)):
        # Appender ett tillfeldig tall mellom 1 og 6 i treningKast
        terningKast[i] = randint(1,6)
        terningKastSnitt.append(np.average(terningKast[0:i+1]))
        terningKastMinimum.append(np.min(terningKast[0:i+1]))
        terningKastMaksimum.append(np.max(terningKast))
    

    plt.close('all')
    # figsize 
    plt.figure(1,figsize=(12,8), dpi=300)
    # Setter tittel
    plt.title("Oppgave 1. a)")
    
    plt.axis([1,11,0,7])
    
    plt.plot(terningKastSnitt, label="Snitt")
    plt.plot(terningKastMinimum, label = "Min")
    plt.plot(terningKastMaksimum, label="Max")
    plt.legend(loc = "upper left")
    plt.show()
    
#%% Oppgave 1. b)
"""
Gjør ti kast med to terninger. Lag et punktdiagram med ett punkt for hvert kast,
der x-koordinaten (y-koordinaten) tilsvarer verdien oppnådd med første (andre)
terning.
"""
def ToKastsPunktdiagram():
    # Definerer to kast
    terning1Kast = []
    terning2Kast = []
    for i in range(10):
        terning1Kast.append(randint(1,6))
        terning2Kast.append(randint(1,6))
    plt.close("all")
    plt.figure(1,figsize=(12,9), dpi=300)
    plt.title("Oppgave 1. b)")
    plt.plot(terning1Kast, terning2Kast, "*")
    plt.show()


#%% Oppgave 1. c)
"""
Gjør 100 kast med en terning. Lag et stolpediagram som viser hvor mange av kastene
som ga hver av verdiene 1, . . . , 6.
"""
def stolpeDiagramOver100Kast():
    terningKast = [0,0,0,0,0,0]
    for i in range(100):
        kast = randint(1, 6)
        terningKast[kast-1] += 1
    plt.close("all")
    plt.figure(1,figsize=(12,9), dpi=300)
    plt.title("Oppgave 1. c)")
    xList = [1,2,3,4,5,6]
    plt.bar(xList, terningKast )
    plt.show()

#%% Oppgave 1. d)
"""
Gjør 100 kast med en blå og en rød terning. Lag et diagram med seks par bestående
av en rød og en blå stolpe. Diagrammet skal for hver av terningene vise hvor mange
av kastene som ga hver av verdiene 1, . . . , 6.
"""
def stolperRødBlå100Kast():
    farger = ["r", "b"]
    fargeIndeks = 0
    xpos = 0

    blåKast = [0,0,0,0,0,0]
    rødeKast = [0,0,0,0,0,0]
    muligekast = [1,2,3,4,5,6]
    bredde = 1 / (len(muligekast)+1)
    ticks = []
    
    for i in range(100):
        kast = randint(1, 6)
        blåKast[kast-1] += 1
        kast = randint(1, 6)
        rødeKast[kast-1] += 1
    for i, mulige in enumerate(muligekast):
        # plotter data 
        ticks.append((xpos + xpos + len(farger)*bredde)/2)
        plt.bar(xpos, rødeKast[i], width = bredde, align="edge", color=farger[fargeIndeks])
        # bytter farge, men holder oss innen rangen til farger listen
        fargeIndeks = (fargeIndeks + 1) % len(farger)
        xpos += bredde
        plt.bar(xpos, blåKast[i], width = bredde, align="edge", color=farger[fargeIndeks])
        # Øker xpos
        xpos += bredde
        # bytter farge, men holder oss innen rangen til farger listen
        fargeIndeks = (fargeIndeks + 1) % len(farger)
        # Legger til en tom stolpe for å ha avstand mellom søkeordene
        xpos += bredde
    plt.xticks(ticks, labels=muligekast)
    plt.show()
        
    




#%% Main

def main():
    plotToKast()
    ToKastsPunktdiagram()
    stolpeDiagramOver100Kast()
    stolperRødBlå100Kast()
    
if __name__ == "__main__":
    main()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    