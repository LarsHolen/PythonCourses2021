# -*- coding: utf-8 -*-
"""
Created on Thu Dec  2 13:12:14 2021

@author: Lars Holen

SEMESTER OPPGAVE 2

Oppgave 1 Grafiske temperaturrapporter

Svar leveres på fil med navn oppg1.py
Den vedlagte filen april.csv inneholder maksimumstemperatur for fem norske byer
nedlastet fra Norsk Klimaservicesenter. Hver linje inneholder feltene bynavn, dato
og maksimumstemperatur den datoen.

"""

#%% Imports
# datetime, for å kunne ha tidsdata som ett datetime objekt
from datetime import datetime
# pyplot for plotting av data 
import matplotlib.pyplot as plt


#%% Oppgave 1. a)
"""
Skriv en funksjon les_temp(filnavn, skille=',') med navnet på en CSVfil som første parameter, 
og som leser filen. Andre parameter sier hvilket skilletegn
som skal brukes. Funksjonen skal returnere en oppslagstabell der nøklene er bynavn,
og verdiene er oppslagstabeller. I disse oppslagstabellene skal nøklene være dato, og
verdiene makstemperatur.
"""

def les_temp(filnavn, skille=','):
    """
    Parameters
    ----------
    filnavn : string
        nanv på csv fil.
    skille : string, optional
        Tegnet som separerer datane i csv filen. Default er ','.

    Returns
    -------
    dataDictionary : Dcitionary
        En dictionary, med "by" key(string), og dictionaries som values(hvor dato(datetime)
        er key og måling(float) er values.
    """
    # Åpner filen for lesing og med encoding for å få korrekt ÆØÅ
    with open(filnavn, "r", encoding="utf-8") as fil:
        # Definerer resultat dictionary/oppslagsverk
        dataDictionary = {}
        # Looper gjennom filen men både index og linje
        for i, linje in enumerate(fil):
            # Ignorerer første linje, siden den ikke inneholder data jeg ønsker
            if i == 0:
                continue
            # Deler opp linjen etter skille tegnet
            dataLinje = linje.rstrip().split(skille)
            
            # Om byen ikke eksisterer i oppslaget, Legger vi det til med ett
            # nytt oppslag som value
            if dataLinje[0] not in dataDictionary:
                dataDictionary[dataLinje[0]] = {}
            # DatoTid vil aldri bli den samme for den samme byen, så jeg tester ikke
            # for duplikater i målingene.  Gjør om tekst datoen til datetime objekt
            # som blir key, og målingen gjøres om til float fra tekst
            dataDictionary[dataLinje[0]][datetime.strptime(dataLinje[1],'%d.%m.%Y')] = float(dataLinje[2])
            
        """
        #Test for å lese oppslagstabellene
        #Lar denne stå, om sensor ønsker teste selv
        
        for by in dataDictionary:
            print(by)
            for målingsDato in dataDictionary[by]:
                print(målingsDato , " " , dataDictionary[by][målingsDato] )
        """
    # returnerer oppslagsverket
    return dataDictionary


#%% Oppgave 1. b)
"""
Skriv en funksjon plott(makstemp) som tar en oppslagstabell av typen forklart
i forrige deloppgave som parameter. Funksjonen skal plotte kurver av 
maksimumstemperatur for hver by som funksjon av tid. Alle kurvene skal framstilles i
samme plott.
Kjøreeksemplet
In [1]: makstemp = les_temp('april.csv', skille=',')
In [2]: plott(makstemp)
skal gi et plott av typen som vist i oppgaven
"""
def plott(makstemp):
    """
    Parameters
    ----------
    makstemp : Dictionary
        Type som returnert av les_temp(filnavn, skille=',') funksjonen

    Returns
    -------
    None. Skriver plottet til skjerm

    """
    # Lukker eventuelle gamle plot
    plt.close('all')
    # Setter figur id/navn 1 og størrelse i tommer og dpi 300 på plottet
    # figsize justert for å få plottet til å ligne det i oppgaven
    plt.figure(1,figsize=(6,5), dpi=300)
    # Setter tittel
    plt.title("Maksimumstemperaturer i Norge i peroiden 1.-30. april 2021")
    # looper gjennom oppslagstabellen
    for by in makstemp:
            # Definerer lister for datane for målingene i hver by.
            # Lager nye for hver by/fjerner gammel data
            x= []
            y=[]
            # Looper gjennom målingene i gitte by
            for målingsDato in makstemp[by]:
                # Legger til målingens dags dato i x listen
                x.append((målingsDato.date().day))
                # Legger til selve målingen i y listen
                y.append(makstemp[by][målingsDato])  
            # Plotter x,y listene og legger til by i label
            plt.plot(x,y, label=by)     
            
    # Viser label/by navn i upper left
    plt.legend(loc = "upper left")
    """
    # Lagre plot som pdf om ønskelig
    plt.savefig("PlottOppgave1b.pdf")
    """
    # "Lukker" plottet", kan ikke bli kalt eller lagret etter show()
    # Dette gjør også at man kan lage nye plot, uten at det blir "skrevet over"
    plt.show()
    
    
#%% Oppgave 1. c)
"""
Skriv en funksjon stolper_snitt(makstemp) som lager et stolpediagram
over gjennomsnittlig maksimumstemperatur i april for de fem byene. Funksjonen
skal ta en oppslagstabell av typen nevnt i første deloppgave som parameter.
Kjøreeksemplet
In [3]: stolper_snitt(makstemp)
skal gi diagram av typen som vist i oppgaven
"""
def stolper_snitt(makstemp):
    """
    Parameters
    ----------
    makstemp : Dictionary
        Type som returnert av les_temp(filnavn, skille=',') funksjonen

    Returns
    -------
    None. Skriver plottet til skjerm

    """
    # Lukker eventuelle gamle plot
    plt.close('all')
    # Setter figur id/navn 1 og størrelse i tommer og dpi 300 på plottet
    # figsize justert for å få plottet til å ligne det i oppgaven
    plt.figure(1,figsize=(6,4), dpi=300)
    # Setter tittel
    plt.title("Gjennomsnittelig makstemperaturer i Norge i april 2021")
    # looper gjennom oppslagstabellen
    # Definerer lister for plottene
    byer = []
    snittTemp = []
    for by in makstemp:
            # Definerer lister for datane for målingene i hver by.
            # Lager nye for hver by/fjerner gammel data
            temp=[]
            # Looper gjennom målingene i gitte by
            for målingsDato in makstemp[by]:
                # Legger til selve målingen i temp listen
                temp.append(makstemp[by][målingsDato])
            # Legger til by navn i byer listen
            byer.append(by)
            # Legger til snittet av alle temperaturene for denne byen
            snittTemp.append(sum(temp)/len(temp))
    
    # Plotter x,y listene i bar/stolpediagram
    plt.bar(byer, snittTemp, width=0.9)           
    """
    # Lagre plot som pdf om ønskelig
    plt.savefig("PlottOppgave1b.pdf")
    """
    # "Lukker" plottet", kan ikke bli kalt eller lagret etter show()
    # Dette gjør også at man kan lage nye plot, uten at det blir "skrevet over"
    plt.show()
    

#%% Oppgave 1. d)
"""
Skriv en funksjon kake(makstemp) som lager et sektordiagram over hvor ofte
(hvor mange dager) hver by er den med høyest temperatur.
Kjøreeksemplet
In [4]: kake(makstemp)
skal gi diagram av typen som vist i oppgaven
"""
def kake(makstemp):
    """
    Parameters
    ----------
    makstemp : Dictionary
        Type som returnert av les_temp(filnavn, skille=',') funksjonen

    Returns
    -------
    None. Skriver plottet til skjerm

    """
     # Lukker eventuelle gamle plot
    plt.close('all')
    # Setter figur id/navn 1 og størrelse i tommer og dpi 300 på plottet
    # figsize justert for å få plottet til å ligne det i oppgaven
    plt.figure(1,figsize=(8,4), dpi=300)
    # Setter tittel
    plt.title("Hvor ofte har byene høyest temperatur i april 2021")
    # looper gjennom oppslagstabellen
    # Definerer lister for plottene
    # Navnene på byene
    byer = []
    # liste med antall ganger tilhørende by/index har høyeste temp
    harMaksTemp = [0,0,0,0,0]
    # Looper gjennom byene og lagrer by navn i listen
    for by in makstemp:
          byer.append(by)
    # Looper gjennom målingene
    
    for index, måling in enumerate(makstemp[byer[0]].items()):
        # Lager en test liste for å sjekke høyeste temp
        # Burde sjekke andre måter å gjøre det på om
        # antall målinger eller byer kunne bli stort med tanke på
        # hastighet
        testListe = []
        # Finner datoen for målingen
        målingsDato = måling[0]
        # Legger til målingene fra hver by
        for i in range(len(byer)):
            # Finner temperatur i de forskjellige byene på denne målingsDato
            testListe.append(makstemp[byer[i]][målingsDato])
        # Finner max temp
        maxT = max(testListe)
        # maxT kan være lik i flere byer, altså flere byer som harMaksTemp
        # så jeg looper gjennom antall ganger jeg finner maxT
        for i in range(testListe.count(maxT)):
            # Finner indexen på den høyeste temperaturen
            index = testListe.index(maxT)
            # Legger til 1 i harMaksTemp listen, i korrekt index
            harMaksTemp[index] += 1
            # denne index/temp har blitt registrert, så jeg setter den til noe
            # veldig lavt
            testListe[index] = -270
    # Tegner plot
    plt.pie(harMaksTemp, labels=byer, autopct="%.1f%%")           
    plt.legend(loc = "upper right")
    """
    # Lagre plot som pdf om ønskelig
    plt.savefig("PlottOppgave1b.pdf")
    """
    # "Lukker" plottet", kan ikke bli kalt eller lagret etter show()
    # Dette gjør også at man kan lage nye plot, uten at det blir "skrevet over"
    plt.show()


#%% Main
def main():
    plott(les_temp("april.csv", skille=","))
    stolper_snitt(les_temp("april.csv"))
    kake(les_temp("april.csv"))
if __name__ == "__main__":
    main()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    