# -*- coding: utf-8 -*-
"""
Created on Fri Dec  3 13:26:35 2021

@author: Lars Holen

SEMESTER OPPGAVE 2

Oppgave 2 Sammenligning av nettaviser

Svar leveres på fil med navn oppg2.py
Vi vil analysere hvor ofte interessante ord forekommer på ulike avisers nettsider.
For å forenkle analysen, vil vi
• ikke skille mellom store og små bokstaver,
• ikke tolke html-koden, men heller lete etter ordene i html-filen, og
• telle forekomster v.h.a. strengmetoden count, slik at f.eks. teksten ‘... kjenner
lusa på gangen ...’ gir en forekomst av søkeordet USA.

"""

#%% Imports
# pyplot for plotting av data 
import matplotlib.pyplot as plt

# Import get to download url
from requests import get

# Kunne importert alt fra tkinter med *, men fikk så mange gule varseltrekanter
# i margen, at jeg gikk gjennom alt og importerte kun det python bad om.
# Psykisk helse er viktig!
from tkinter import Tk
from tkinter import Frame
from tkinter import Scrollbar
from tkinter import RIGHT
from tkinter import Y
from tkinter import Listbox
from tkinter import MULTIPLE
from tkinter import END
from tkinter import Button
from tkinter import Label


#%% Oppgave 2. a)
"""
Skriv en funksjon stolper(funn) som tar som parametre en oppslagstabell
(dict) over antall funn. Nøklene i funn er søkeord (strenger), og verdiene er 
oppslagstabeller med avisnavn som nøkler og antall forekomster av søkeordet i avisen
som verdier.
Funksjonen skal lage et stolpediagram over antall funn av de ulike søkeordene i hver
av avisene. Stolpene skal presenteres i grupper, med en gruppe for hvert søkeord.
I hver gruppe skal det være en stolpe for hver avis, med ulike farger. Mellom hver
gruppe skal det være et mellomrom like bredt som en stolpe.
Kjørekesempelet
In [1]: funn = {}
In [2]: funn['Norge'] = {'VG': 25, 'Dagbladet': 9, 'BT': 9}
In [3]: funn['Bergen'] = {'VG': 10, 'Dagbladet': 0, 'BT': 47}
In [4]: stolper(funn)
skal gi diagram av typen som vist i oppgaven
"""
def stolper(funn):
    # Lukker eventuelle gamle plot
    plt.close('all')
    # Setter figur id/navn 1 og størrelse i tommer og dpi 300 på plottet
    # figsize justert for å få plottet til å ligne det i oppgaven
    plt.figure(1,figsize=(12,5), dpi=300)
    
    # Setter x posisjon til null
    xpos = 0
    # Liste for å lagre posisjonene
    ticks = []
    
    # liste med fargene
    farger = ["b", "r", "g"]
    
    # Looper gjennom dictionary'en
    for søkeord in funn:
        # Lager en liste av alle mediene
        medier = list(funn[søkeord].keys())
        #Lager en variabel for å holde lengden på medier(siden den blir brukt flere ganger)
        antallMedier = len(medier)
        # Setter bredden
        bredde = 1 / (antallMedier+1)
        # Lagrer posisjon der funn ordene skal stå under stolpene
        ticks.append( (xpos + xpos + antallMedier*bredde)/2)
        # En variabel for å holde styr på fargene til stolpene i farger listen
        farge_i = 0
        # Looper gjennom medier
        for medie in medier:
            # plotter data 
            plt.bar(xpos, funn[søkeord][medie], width = bredde, align="edge", color=farger[farge_i])
            # Øker xpos
            xpos += bredde
            # bytter farge, men holder oss innen rangen til farger listen
            farge_i = (farge_i + 1) % len(farger)
        # Legger til en tom stolpe for å ha avstand mellom søkeordene
        xpos += bredde
    # Setter inn søkeordene som labels med avstander satt i ticks
    plt.xticks(ticks, labels=funn.keys())
    # Legger på boks med beskrivelse av medier og farge, og plasserer den opp til høyre
    plt.legend(medier, loc="upper right")
    """
    # Lagre plot som pdf om ønskelig
    plt.savefig("PlottOppgave1b.pdf")
    """
    # "Lukker" plottet", kan ikke bli kalt eller lagret etter show()
    # Dette gjør også at man kan lage nye plot, uten at det blir "skrevet over"
    plt.show()
    
#%% Oppgave 2. b)
"""
Skriv en funksjon søk(søkeord) som tar som parameter en liste med søkeord.
Funksjonen går gjennom avisene VG, Dagbladet og BT, og lager en oppslagstabell,
funn, over antall funn i hver av avisene av hvert søkeord i listen. (Utvalget av aviser
kan for enkelhets skyld være hardkodet i funksjonen.) Deretter skal funksjonen kalle
opp funksjonen stolper for å få grafisk framstilling av resultatet.
Kjørekesempelet
In [1]: søk(['Norge', 'Bergen'])
skal gi diagram av typen vist i forrige deloppgave i oppgaven
"""
def søk(søkeord):
    """
    Parameters
    ----------
    søkeord : LIST
        En liste med ord, som man vil finne antall funn av i vg, db og bt 
        nettsidene. Størrelsen på plottet i stolper funksjonen må justeres
        ved bruk av mange eller veldig lange søkeord.

    Returns
    -------
    None. Viser ett stolpediagram på skjerm/plot

    """
    # Oppretter en dictionary for resultetene
    resultat = {}
    # hard koder internet adresser til VG, Dagbladet og BT 
    urlVG = "http://www.vg.no"
    urlDB = "http://www.db.no"
    urlBT = "http://www.bt.no"
    # Henter nettside's respons objekt
    dataVG = get(urlVG)
    dataDB = get(urlDB)
    dataBT = get(urlBT)
    # Gjør om respons objektetene's nettside data til string
    dataTekstVG = dataVG.text
    dataTekstDB = dataDB.text
    dataTekstBT = dataBT.text
    #  Looper gjennom hver søkeord i parameter listen
    for søkeordet in søkeord:
        # Legger til ønsket data i resultat dictionary
        # Teller hvert søke ord funnet i hver av nettsidene.  Bruker 
        # lower() både på nettsideteksten og søkeord for å telle med 
        # alle ord uansett stor eller små bokstaver
        resultat[søkeordet] = {"VG" : dataTekstVG.lower().count(søkeordet.lower()),
                               "Dagbladet" : dataTekstDB.lower().count(søkeordet.lower()),
                               "BT" : dataTekstBT.lower().count(søkeordet.lower())}
    # Sender resultatet til stolper funksjonen, som tegner ett plott
    stolper(resultat)

#%% Oppgave 2. c)
"""
Skriv kode for et tkinter-basert grafisk brukergrensesnitt (GUI) som inneholder en ramme med disse komponentene:
    
• en forklarende tekst (Label),
• en liste med mulige søkeord (strenger) brukeren kan velge fra (Listbox) og
• en knapp (Button).

Listen med mulige søkeord kan være hardkodet til
'Verden', 'USA', 'Europa', 'Norge', 'Noreg', 'Oslo', 'Bergen',
'Nyhet', 'Sport', 'Valg', 'Fotball', 'Klima', 'Corona', 'Korona'

Brukeren skal kunne velge et vilkårlig antall søkeord. Knappen skal ha en påskrift
som f.eks. 'Start søk'. Den forklarende teksten skal informere brukeren kort om
at hun kan velge interessante søkeord, og deretter trykke på knappen for å lansere
søket. Knappen skal v.h.a. parameteren command kobles til en funksjon start_søk
som skal lage en liste av utvalgte søkeord, og sende listen til funksjonen søk 
fra forrige deloppgave. Resultatet skal dermed bli et stolpediagram over funn av utvalgte
søkeord i de tre avisene. Merk at du også må skrive funksjonen start_søk.
Eksempel: Dersom brukeren velger søkeordene som vist i figuren til venstre, og
deretter trykker på ‘Vis resultat’, skal et stolpediagram av typen vist i figuren til
høyre i oppgaven dukke opp.

Hint: Klassen Listbox har en metode curselection() som returnerer et tuppel
bestående av indeksene til de strengene som bruker har valgt.

"""
def GUI_Oppgave():
    """
    Lager en GUI hvor man velger søkeord i en liste.
    Når man klikker Vis resultat knappen, så gjøres søket og 
    det blir plottet og vist

    Returns
    -------
    None. Viser GUI på skjerm.  Viser resultat når man trykket på knappen

    """
    
    # Definerer GUI vinduet
    vinduet = Tk()
    # Setter minimum og start størrelse
    vinduet.minsize(400,400)
    # Setter tittel på vinduet.  Posisjonen på tittelen varierer ved bruk av
    # forskjellige operativsystem windows/mac
    vinduet.title("Velg søkeord")
    
    # Lager en Frame vi begynner å legge elementer i
    rammen = Frame(vinduet)
    rammen.pack()
    
    
    
    # Legger søkeordene definert i oppgaven i en liste
    hardkodetSøkeliste = ['Verden', 'USA', 'Europa', 'Norge', 'Noreg', 'Oslo', 'Bergen',
                          'Nyhet', 'Sport', 'Valg', 'Fotball', 'Klima', 'Corona', 'Korona']
    
    # Lager en ny Frame under den første for at rullestolpen til listeboksen 
    # skal ligge ved høyre side, tett intil listeBoksen. Denne rammen er bare så bred 
    # som listeBoks og rulleStolpen vil utvide Framen med sin størrelse og bli liggende
    # tett intilpå "RIGHT" side.
    ramme2 = Frame(vinduet)
    ramme2.pack()
    
    # Definerer en Scrollbar
    rulleStolpe = Scrollbar(ramme2)
    # Setter den til å posisjonere seg til høyre og utvide seg vertikalt i Framen
    rulleStolpe.pack(side=RIGHT, fill=Y)
    
    # Definerer en Listbox, i ramme2 Framen, høyde 12 elementer(som vist på bildet
    # i oppgaven, lar man velge flere elementer, og vertikal scrolling behandlers av
    # Scrollbar/rulleStolpe.set)
    listeBoks = Listbox(ramme2, height=12, selectmode=MULTIPLE, yscrollcommand=rulleStolpe.set)
    
    # Legger til elementer i listeBoks
    for søkeord in hardkodetSøkeliste:
        listeBoks.insert(END, søkeord)
    listeBoks.pack()
    
    # Legger en knapp i den første Framen, og gir knappen tekst og en funksjon som kalles
    # når man trykker på den.  Jeg måtte legge den inn etter at jeg lagde listeBoksen,
    # siden jeg bruker listeboksen som parameter i command.
    knappen = Button(rammen, text = "Vis resultat", command= lambda: start_søk(listeBoks))
    knappen.pack()
    
    # Legger så til en forklarende tekst, som da kommer under knappen
    tekstLabel = Label(rammen, text = "Velg så mange søkeord du vil, og trykk på knappen)")
    tekstLabel.pack()
    
    # Konfigurerer Scrollbar til å virke med listeBoks
    rulleStolpe.config(command=listeBoks.yview)

    vinduet.mainloop()
        

# Funksjonen som blir utført av kanppetrykk i GUI_Oppgave funksjonen
def start_søk(listen):
    # om det ikke er noen valgte elementer, returnerer vi bare
    if len(listen.curselection()) == 0:
        return
    # Definerer en søkeliste
    søkeListe = []
    # Looper gjennom tuplen med indexer som blir returnert av curselection()
    for i in listen.curselection():
        # Legger til søkeordet som i/indeksen viser til
        søkeListe.append(listen.get(i))
    # Sender søkelisten til søk funksjonen 
    søk(søkeListe)







#%% Main
def main():
    funn = {}
    funn['USA'] = {'VG': 11, 'Dagbladet': 4, 'BT': 14}
    funn['Norge'] = {'VG': 25, 'Dagbladet': 9, 'BT': 9}
    funn['Oslo'] = {'VG': 14, 'Dagbladet': 10, 'BT': 4}
    funn['Bergen'] = {'VG': 10, 'Dagbladet': 6, 'BT': 47}
    funn['Nyhet'] = {'VG': 30, 'Dagbladet': 25, 'BT': 17}
    funn['Sport'] = {'VG': 10, 'Dagbladet': 5, 'BT': 7}
    funn['Fotball'] = {'VG': 1, 'Dagbladet': 2, 'BT': 4}
    stolper(funn)
    søk(["Oslo", "Salg", "jul", "strøm", "fattig", "krig", "død", "rik"])
    GUI_Oppgave()
    
    
    
    
    
if __name__ == "__main__":
    main()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
