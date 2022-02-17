# -*- coding: utf-8 -*-
"""
Created on Fri Feb 12 13:43:29 2021

@author: larsh
"""

# %% importerer pakker

import numpy as np
import matplotlib.pyplot as plt


# %% Definerer Variabler

x1 = 0  #start punkt i origo 0,0
y1 = 0

strekning = 0


# %% Funksjon definisjoner

def reiselengde(x1,y1,x2,y2):
    return np.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


# %% Program

x2 = float(input("Skriv inn x-koordinaten for andre destinasjon her:"))
y2 = float(input("Skriv inn y-koordinaten for andre destinasjon her:"))

strekningArray = [0]    # Setter første destinasjon til Origo, så plot starter i 0
strekningStartSluttArray = [0]


strekning1 = reiselengde(x1,y1,x2,y2)
strekning += strekning1
strekningArray.append(strekning)
strekningStartSluttArray.append(strekning1)
print("Avstand fra x1,y1 til x2,y2 er lik: ", strekning1)
print("Totalt reiste strekning er lik: ", strekning)
print("Avstand fra startpunkte1(x1,y1) er lik:", strekning1) 
print("Disse tre skal alltid være like ved andre punkt.")

x3 = float(input("Skriv inn x-koordinaten for tredje destinasjon her:"))
y3 = float(input("Skriv inn y-koordinaten for tredje destinasjon her:"))

strekning2 = reiselengde(x2,y2,x3,y3)
strekning += strekning2
strekningStartSlutt = reiselengde(x1,y1,x3,y3)
strekningArray.append(strekning)
strekningStartSluttArray.append(strekningStartSlutt)
print("Avstand fra x2,y2 til x3,y3 er lik: ", strekning2)
print("Totalt reiste strekning er lik: ", strekning)
print("Avstand fra startpunkte1(x1,y1) er lik:", strekningStartSlutt)

x4 = float(input("Skriv inn x-koordinaten for fjerde destinasjon her:"))
y4 = float(input("Skriv inn y-koordinaten for fjerde destinasjon her:"))

strekning3 = reiselengde(x3,y3,x4,y4)
strekning += strekning3
strekningStartSlutt = reiselengde(x1,y1,x4,y4)
strekningArray.append(strekning)
strekningStartSluttArray.append(strekningStartSlutt)
print("Avstand fra x2,y2 til x3,y3 er lik: ", strekning3)
print("Totalt reiste strekning er lik: ", strekning)
print("Avstand fra startpunkte1(x1,y1) er lik:", strekningStartSlutt)


dStopp = len(strekningArray)
destinasjoner = np.linspace(0, dStopp-1, dStopp) # lager en array med "destinasjon ID" 0,1,2,3 etter lengden på strekningarray

# %% Plotting


plt.close("all") #lukker eventuelle åpne figurer
plt.figure(1) # Setter figur 1 som aktiv
plt.plot(destinasjoner, strekningArray, "bo-") # plotter destinasjoner/strekningarray med blå farge, O'er i punktene og strek mellom
plt.plot(destinasjoner, strekningStartSluttArray, "ro-") # plotter destinasjoner/strekningStartArray med rød farge, O'er i punktene og strek mellom

plt.xlim(0, len(destinasjoner)) # Setter grenser på x aksen 0 til lengden av arrayen(en mer enn nødvending, så enden på plottene blir tydeligere)
plt.ylim(0,strekningArray[np.argmax(strekningArray)] + strekningArray[np.argmax(strekningArray)]/len(strekningArray)) # Setter grenser på y aksen fra null til maximalverdien i arrayen(pluss maxverdi/lengde av array)
plt.grid() # viser rutenett
plt.xticks(destinasjoner) # setter x verdiene på x aksen til verdiene i destinasjoner arrayen
plt.ylabel("Strekning") 
plt.xlabel("Destinasjon")
plt.title("Plot av avstander mellom destinasjoner og \n avstand fra start destinasjon ")
plt.legend(labels=("Total Strekning", "Strekning til startpunkt"))
plt.show() # forsikrer at figuren blir vist 

