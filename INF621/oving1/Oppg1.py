# -*- coding: utf-8 -*-
"""
Created on Tue Oct 26 17:48:11 2021

@author: Lars Holen


INF621 - Høstsemesteret 2021
Øvingsoppgave 1

"""


#%% Oppgave 1. a)
def erstatt(tekst, ordbok):
    
    ordListe = tekst.split()
    for index, ord in enumerate(ordListe):
        if ordbok.get(ord) != None:
            ordListe[index] = ordbok[ord]
    result = " ".join(ordListe)
    return result


#%% Oppgave 1. b)
def les_ordbok():
    lhs = ""
    rhs = ""
    result = {}
    while True:
        lhs = input("Gi meg det neste ordet(avslutt med tom streng): ")
        if lhs == "":
            break
        if result.get(lhs) != None:
            print("Tidligere ville du erstatte", lhs, "med", result[lhs])
        inputTekst = "Hva skal " + lhs + " erstattes med: "
        rhs = input(inputTekst)
        print("Vi erstatter", lhs, "med", rhs)
        result[lhs] = rhs
    return result

#%% Oppgave 1. c)
def oversett():
    ordliste = les_ordbok()
    while True:
        lhs = input("Skriv en tekst vi skal oversette(avslutt med tom streng): ")
        if lhs == "":
            break
        print("Den nye teksten er:", erstatt(lhs, ordliste))
        
    

    
    
if __name__ == "__main__":
    oversett()
    