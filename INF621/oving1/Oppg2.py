# -*- coding: utf-8 -*-
"""
Created on Wed Oct 27 11:25:44 2021

@author: Lars Holen

INF621 - Høstsemesteret 2021
Øvingsoppgave 2

"""
#%% Imports
from random import randint


#%% Oppgave 2. a)
def les_ny_vare():
    vare = ""
    pris = ""
    kategori = ""
    vare = str(input("Navn på vare: "))
    pris = int(input("Pris på vare: "))
    kategori = str(input("Kategori: "))
    result = {"navn" : vare, "pris" : pris, "kategori" : kategori}
    return result


#%% Oppgave 2. b)
def les_utvalg():
    result = []
    while True:
        velg = str(input("Vil du legge til en ny vare (j/n)? "))
        if velg.lower() == "n":
            break
        # I og met jeg antar alltid gyldig input, ingen else setning nødvendig
        result.append(les_ny_vare())
    return result

#%% Oppgave 2. c)
def tell_varer(vareliste):
    for dik in vareliste:
        dik["antall"] = randint(0, 3) 

#%% Oppgave 2. d)
def sett_ned_pris(vareliste, kategori, prosent):
    for dik in vareliste:
        if dik["kategori"] == kategori:
            nypris = dik["pris"] - dik["pris"]*prosent/100
            dik["pris"] = nypris
            

#%% Oppgave 2. e)
def selg_vare(varenavn, vareliste):
    for dik in vareliste:
        if dik["navn"] == varenavn:
            if dik["antall"] > 0:
                dik["antall"] -= 1
                return dik["pris"]
            else:
                return -1
            
#%% Oppgave 2. f)
def selg_varer(handleliste, vareliste):
    sumPriser = 0
    for handleObjekt in handleliste:
        for dik in vareliste:
            if dik["navn"] == handleObjekt:
                if dik["antall"] > 0:
                    dik["antall"] -= 1
                    sumPriser += dik["pris"]
                    break
    return sumPriser

                    

            
#%% Main
            

    
if __name__ == "__main__":
    vareliste = les_utvalg()
    tell_varer(vareliste)
    sett_ned_pris(vareliste, 'frukt', 10)
    selg_vare('eple',vareliste)
    selg_vare('kål',vareliste)
    selg_varer(['eple', 'kål', 'drue', 'eple'], vareliste)
    print(vareliste)