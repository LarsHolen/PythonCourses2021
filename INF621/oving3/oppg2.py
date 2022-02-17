# -*- coding: utf-8 -*-
"""
Created on Fri Nov 19 13:37:00 2021

@author: Lars Holen

INF621 - Høstsemesteret 2021

Oppgave 2

Værdata for Bergen
Filen florida.csv (tilgjengelig i mappen Filer/Oppgaver på MittUiB) inneholder
værdata (gjennomsnittlig vindstyrke, nedbørsmengde, minimumstemperatur, mak1
simumstemperatur) på Florida værstasjon i Bergen i perioden for hvert døgn fra 1.
januar til 31. oktober 2021.
"""

#%% Import

import csv
from datetime import datetime
import locale

# Setting culture to norwegian
locale.setlocale(locale.LC_ALL, "no_NO")

#%% Oppgave 2. a)
"""
Last ned og gjør deg kjent med innholdet i denne filen, f.eks. ved å åpne den i Excel.
Sjekk i konsollen at du klarer å lese inn filen, enten v.h.a. csv.reader, eller ved å
lese den som en vanlig tekstfil.
"""
def LesFloridaSomTekst():
    """
    Reads a csv file named florida.csv as a text file
    Parse it and add the data into a list of the VaerData class
    Returns
    -------
    List<VaerData>

    """
    # Definerer en liste å lagre dataene som returneres
    vaerData = []
    # Åpner filen florida.csv
    with open("florida.csv") as fil:
        # Looper gjennom linjen, med index og item med "enumerate()
        for index,linje in enumerate(fil):
            # Hopper over første linje, siden det er en "header" 
            if index == 0:
                continue
            # Deler opp linjen i hvert komma
            l = linje.split(",")
            # Lager ett VaerData objekt og lagrer dataene fra l listen
            vaerData.append(VaerData(l[0],l[1], l[2], l[3], l[4]))
    # Skriver ut liten til skjerm for testing
    #for v in vaerData:
        #print("Dato: ", v.dato, "Vind: ", v.vind, "\tNedbør: ", v.regn, "\tMinTemp:", v.minTemp, "\tMaksTemp:", v.maksTemp)
    
    # returnerer listen
    return vaerData

def LesFloridaSomCSV():
    """
    Reads a csv file named florida.csv with the csv reader
    Parse it and add the data into a list of the VaerData class
    Returns
    -------
    List<VaerData>

    """
    # Definerer en liste å lagre dataene som returneres
    vaerData = []
    # Åpner filen
    with open("florida.csv", newline="") as csvFil:
        # Leser data fra filen med csv reader
        data = csv.reader(csvFil,dialect='excel')
        # Looper gjennom resultetet
        for index, doegn in enumerate(data):
            # Hopper over headeren
            if index == 0: 
                continue
            # Lagrer datane i ett object og lagrer objektet i en liste
            datoen = datetime.strptime(doegn[0], "%d.%m.%Y").date()
            vaerData.append(VaerData(datoen,doegn[1], doegn[2], doegn[3],doegn[4]))
    # skriver ut listen til skjem for testing
    #for v in vaerData:
    #    print("Dato: ", v.dato,"\tVind:", v.vind, "\tNedbør: ", v.regn, "\tMinTemp:", v.minTemp, "\tMaksTemp:", v.maksTemp)
    
    # returnerer listen
    return vaerData

class VaerData:
    def __init__(self, dato,vind , regn, minTemp, maksTemp):
        """
        Parameters
        ----------
        dato : string
            DateTime i stringformat.
        vind : string
            Vind i m/s
        regn : string
            Nummer i stringformat som beskriver nedbør i mm dette døgn
        minTemp : string
            Nummer som beskriver minimums temperatur dette døgn
        maksTemp : string
            Nummer som beskriver maksimums temperatur dette døgn
        """
        self.dato = dato
        self.vind = vind        
        self.regn = regn
        self.minTemp = minTemp
        self.maxTemp = maksTemp
    
#%% Oppgave 2. b)
"""
Skriv deretter pythonkode som leser filen, og som genererer en ny csv-fil som har
en rad for hver av månedene januar–oktober. Kolonnene i den nye filen skal være
minste og største gjennomsnittlige vindstyrke, total nedbørmengde, samt minimum
og maksimum temperatur. Det er ikke noe krav til hvilken mappe filen skal plasseres
i.
"""
def VaerDataMaanedsStatestikk():
    # Laser inn værdata fra florida.txt i en liste
    VaerDataListe = LesFloridaSomCSV()
    # Listen er allerede sortert etter dato
    # Definerer en måneds variabel for å holde styr på nest siste 
    #månedsdato i loopen
    mnd = 0
    # Liste som lagrer dags data pr måned
    mndData = []
    # åpner en fil til å skrive resultatet i
    with open("MaanedsvisVaerData.csv","w", newline="") as fil:
        csvwriter = csv.writer(fil,dialect='excel')
        csvwriter.writerow(["Måned", "Min Vind", "Max Vind", "Total nedbød", "Min Temp", "Max temp"])
        # Looper gjennom data listen
        for index, dag in enumerate(VaerDataListe):
            # Sjekker om det er første iterasjon og om så, setter mnd til dagens mnd
            if index == 0: mnd = dag.dato.month 
            # Når måneden i forrige iterasjon er en annen enn i dag, bytter vi måned
            if dag.dato.month > mnd: 
                # Gjør klar data for å bli skrevet til fil
                m =  datetime.strftime(mndData[0].dato, format="%B")
                maxVind = max(v.vind for v in mndData)
                minVind = min(v.vind for v in mndData)
                # sum virker ikke på string, så gjør den om til float
                # Må da runde av, så jeg får ett max antall desimaler
                sumRegn = round(sum(float(r.regn) for r in mndData),2)
                maxTemp = max(t.maxTemp for t in mndData)
                minTemp = min(t.minTemp for t in mndData)
                csvwriter = csv.writer(fil,dialect='excel')
                csvwriter.writerow([m, minVind, maxVind, sumRegn, minTemp, maxTemp])
                # Tømmer mndData for å begynne fylle den med en ny mnd
                mndData.clear()
            
            # Legger in dagsdata i mndData
            mndData.append(dag)       
            # Setter mnd til dagens mnd på slutten av loopen
            mnd = dag.dato.month
        
#%% Main
def main():
    print("Main running")
    #LesFloridaSomTekst()
    #LesFloridaSomCSV()
    VaerDataMaanedsStatestikk()
    
if __name__ == "__main__":
    main()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    