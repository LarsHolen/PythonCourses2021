# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 14:00:15 2021

@author: larsh

Arbeidskrav 2 Levert som PDF

"""

# OPPGAVE 1

# %% importere pakker

import numpy as np

# %% Definere variabler

antall_elever = 0
antall_pizza = 0

# %% Definere funksjon

def faaOgsjekkAntall():
    while True:
        try:
            tall = int(input("Skriv inn antall elever: "))
        except ValueError: # Om input ikke er tall, skaff ny input
            continue
        else:
            if tall < 1: # Om tallet er under 1, må det være feil.Skaff ny input
                continue
            else:
                return (tall)
            

# %% Få antall elever fra bruker:
    
antall_elever = faaOgsjekkAntall()


# %% Beregninger

antall_pizza = np.ceil(antall_elever/4) # np.ceil runder tallet opp til nermeste heltall.  
                                        # Men blir ikke lagret som heltall variabel, 
                                        # er fortsatt float


# %% Skriver til skjerm

print("Det må handles", int(antall_pizza), "pizzaer til klassefesten!") # antall_pizza gjøres om 
                                                                        # til heltall for syns skyld










# OPPGAVE 2


# %% Importerer pakker

import numpy as np


# %% Definerer variabler

grader_input = 0
radianer = 0

# %% Definerer funksjoner

def grad2rad(grader):
    return grader*np.pi/180

# %% Motta input

while True:
    try:
        grader_input = float(input("Skriv inn gradtallet: "))
    except ValueError: # om input ikke kan gjøres om til float
        continue
    else:
        break
            
# %% Skriv til skjerm

print("Beregninger rundes til 2 desimaler eller mindre")
print(np.round(grader_input,2),"grader er lik", np.round(grad2rad(grader_input),2), "radianer.")
print("Regner vi om til max <360 grader eller <6.28 radianer:")
print(np.round(grader_input % 360,2) ,"grader er lik", np.round(grad2rad(grader_input % 360),2), "radianer.")





# OPPGAVE 3


# %% importerer pakker

import numpy as np


# %% Definerer Variabler

x1 = 0  #start punkt i origo 0,0
y1 = 0

strekning = 0

# %% Program

x2 = float(input("Skriv inn x-koordinaten for andre destinasjon her:"))
y2 = float(input("Skriv inn y-koordinaten for andre destinasjon her:"))

strekning1 = np.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
strekning += strekning1
print("Avstand fra x1,y1 til x2,y2 er lik: ", strekning1)
print("Totalt reiste strekning er lik: ", strekning)
print("Avstand fra startpunkte1(x1,y1) er lik:", strekning1) 
print("Disse tre skal alltid være like ved andre punkt.")

x3 = float(input("Skriv inn x-koordinaten for tredje destinasjon her:"))
y3 = float(input("Skriv inn y-koordinaten for tredje destinasjon her:"))

strekning2 = np.sqrt((x2 - x3) ** 2 + (y2 - y3) ** 2)
strekning += strekning2
strekningStartSlutt = np.sqrt((x1 - x3) ** 2 + (y1 - y3) ** 2)
print("Avstand fra x2,y2 til x3,y3 er lik: ", strekning2)
print("Totalt reiste strekning er lik: ", strekning)
print("Avstand fra startpunkte1(x1,y1) er lik:", strekningStartSlutt)

x4 = float(input("Skriv inn x-koordinaten for fjerde destinasjon her:"))
y4 = float(input("Skriv inn y-koordinaten for fjerde destinasjon her:"))

strekning3 = np.sqrt((x3 - x4) ** 2 + (y3 - y4) ** 2)
strekning += strekning3
strekningStartSlutt = np.sqrt((x1 - x4) ** 2 + (y1 - y4) ** 2)
print("Avstand fra x2,y2 til x3,y3 er lik: ", strekning3)
print("Totalt reiste strekning er lik: ", strekning)
print("Avstand fra startpunkte1(x1,y1) er lik:", strekningStartSlutt)




# OPPGAVE 4


# %% importerer pakker

import numpy as np


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

strekning1 = reiselengde(x1,y1,x2,y2)
strekning += strekning1
print("Avstand fra x1,y1 til x2,y2 er lik: ", strekning1)
print("Totalt reiste strekning er lik: ", strekning)
print("Avstand fra startpunkte1(x1,y1) er lik:", strekning1) 
print("Disse tre skal alltid være like ved andre punkt.")

x3 = float(input("Skriv inn x-koordinaten for tredje destinasjon her:"))
y3 = float(input("Skriv inn y-koordinaten for tredje destinasjon her:"))

strekning2 = reiselengde(x2,y2,x3,y3)
strekning += strekning2
strekningStartSlutt = reiselengde(x1,y1,x3,y3)
print("Avstand fra x2,y2 til x3,y3 er lik: ", strekning2)
print("Totalt reiste strekning er lik: ", strekning)
print("Avstand fra startpunkte1(x1,y1) er lik:", strekningStartSlutt)

x4 = float(input("Skriv inn x-koordinaten for fjerde destinasjon her:"))
y4 = float(input("Skriv inn y-koordinaten for fjerde destinasjon her:"))

strekning3 = reiselengde(x3,y3,x4,y4)
strekning += strekning3
strekningStartSlutt = reiselengde(x1,y1,x4,y4)
print("Avstand fra x2,y2 til x3,y3 er lik: ", strekning3)
print("Totalt reiste strekning er lik: ", strekning)
print("Avstand fra startpunkte1(x1,y1) er lik:", strekningStartSlutt)



# OPPGAVE 5


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
destinasjoner = np.linspace(0, dStopp-1, dStopp)    # lager en array med "destinasjon ID" 
                                                    # 0,1,2,3 etter lengden på strekningarray

# %% Plotting


plt.close("all") #lukker eventuelle åpne figurer
plt.figure(1) # Setter figur 1 som aktiv
plt.plot(destinasjoner, strekningArray, "bo-")  # plotter destinasjoner/strekningarray med blå farge, 
                                                # O'er i punktene og strek mellom
plt.plot(destinasjoner, strekningStartSluttArray, "ro-")    # plotter destinasjoner/strekningStartArray 
                                                            # med rød farge, O'er i punktene og strek mellom

plt.xlim(0, len(destinasjoner)) 
# Setter grenser på x aksen 0 til lengden av arrayen(en mer enn nødvending, 
# så enden på plottene blir tydeligere)

plt.ylim(0,strekningArray[np.argmax(strekningArray)] + strekningArray[np.argmax(strekningArray)]/len(strekningArray)) 
# Setter grenser på y aksen fra null til maximalverdien i arrayen(pluss maxverdi/lengde av array)

plt.grid() # viser rutenett
plt.xticks(destinasjoner) # setter x verdiene på x aksen til verdiene i destinasjoner arrayen
plt.ylabel("Strekning") 
plt.xlabel("Destinasjon")
plt.title("Plot av avstander mellom destinasjoner og \n avstand fra start destinasjon ")
plt.legend(labels=("Total Strekning", "Strekning til startpunkt"))
plt.show() # forsikrer at figuren blir vist 


