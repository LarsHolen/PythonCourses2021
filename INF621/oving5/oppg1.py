# -*- coding: utf-8 -*-
"""
Created on Thu Dec 16 08:59:59 2021

@author: Lars Holen

Øving 5
INF 621
Øvingsoppgavene er ikke obligatoriske, men vi anbefaler likevel at du gjør
de og leverer de innen fristen — Den eneste måten å lære å programmere på
er ved å programmere. Ved å gjøre oppgavene får du også testet deg selv og
sjekket at du forstår begrepene. Du skal levere én zip-fil, oving5.zip, som
inneholder filene oppg1.py–oppg2.py. For å komprimere en eller flere filer til
en zip-fil høyreklikker du filene (i dette tilfellet oppg1.py–oppg2.py) i 
maskinens filnavigasjonsprogram og velger Komprimer eller Send til → Komprimert
mappe. Frist: Torsdag 16. desember kl 23:59


"""

#%% Imports
import tkinter as tk

#%% Oppgave 1. a)
"""
Svar leveres på fil med navn oppg1.py.
En forenklet Beaufort-skala for vindstyrke er gitt som:
Intervall for vindstyrke (km/t) Kategori
[0, 12) Lite vind
[12, 40) Bris
[40, 76) Kuling
[76, 117) Storm
[117, ∞) Orkan
Skriv et GUI-basert program som tar inn en heltallig vindstyrke i et Entry-felt, og
som svarer med rett vindkategori i et Label-felt når brukeren trykker på en knapp
(Button) med påskriften OK. Alle inndata som ikke kan tolkes som heltall avvises
med en feilmelding. Figurene viser eksempel på utforming av skjermbildet.
Når du har fått koden til å fungere, oppfordres du til å utforske hvordan brukergrensesnittet kan utformes penere, f.eks. ved å bruke farger, ulike fonter, fontstørrelser, etc.
"""
def okSvar(svarTekst, inputString):
    try:
        x = int(inputString.get())
        # sjekker om det er en negativ verdi og gir tilhørende feilmelding
        if(x < 0):
            svarTekst.config(text="Feil: Vindstyrken må vera ikkje-negativ heiltal")
            return
        ## Tester vindstyrker og gir korrekt tilbakemelding
        if x >= 0 and x < 12:
            svarTekst.config(text="Lite vind")
        elif x < 40:
            svarTekst.config(text="Bris")
        elif x < 76:
            svarTekst.config(text="Kuling")
        elif x < 117:
            svarTekst.config(text="Storm")
        else:
            svarTekst.config(text="Orkan")
    except:
        # Fanger opp feil input, feks bokstaver og gir feilmending
        svarTekst.config(text="Feil: Vindstyrken må vera ikkje-negativ heiltal")

def Vindstyrke():
    # Setter opp vinduet og gir det størrelse og tittel
    vindu = tk.Tk()
    vindu.minsize(400,300)
    vindu.title("Beaufort")

    # Lager en ramme inne i vinduet
    ramme = tk.Frame(vindu).pack()
    
    # Definerer noen Tk variabler
    inputString = tk.StringVar(vindu, "")
    svarString = tk.StringVar(vindu, name="svarString", value="")
    
    # Legger en Label/Tekst in i rammen
    tekst = tk.Label(ramme, text="Vindstyrke(km/t):", font=("Times",18, "bold"))
    tekst.pack()

    # Legger inn ett inputfelt i rammen
    inputFelt = tk.Entry(ramme, textvariable=inputString, font=("Times",16, "bold"),)
    inputFelt.pack()
    
    # definerer svarteksten før knappen, fordi jeg skal bruke den som parameter
    # i knappen
    svarTekst = tk.Label(ramme, text=svarString.get(), font=("Times",14, "bold"))
    
    # Lager en knakk med OK tekst og en commando med parametere
    okKnapp = tk.Button(ramme, text = "OK", font=("Times",16, "bold"),  command= lambda: okSvar(svarTekst, inputString))
    okKnapp.pack()
    
    # Legger svarTeksten til under knappen
    svarTekst.pack()
   
    # Starter vinduets mainloop
    vindu.mainloop()
    

def main():
    Vindstyrke()
    
if __name__ == "__main__":
    main()