# -*- coding: utf-8 -*-
"""
Created on Thu Dec 16 13:57:47 2021

@author: Lars Holen

2 Yatzy (50%)
Skriv et GUI-basert program som lar brukeren kaste fem terninger så lenge hun
vil. Programmet skal bare vise terningverdiene (f.eks. en Label-komponent for hver
terning), og telle kastene. Hver gang bruker trykker på en knapp (Button) med
påskriften Kast og antall kast så langt, skal alle terningene kastes på nytt. Antall
kast som vises på knappen skal da oppdateres, og nye terningverdier skal vises. Før
første kast skal ingen terningverdier vises. Figurene viser eksempel på utforming av
skjermbildet.
Når du har fått koden til å fungere, oppfordres du til å utforske hvordan brukergrensesnittet kan utformes videre, f.eks. ved å legge til flere muligheter for bruker.
Eksempler på videreutvikling kan være
• brukerbestemt antall terninger,
• varsel om hvor mange like verdier det er i kastet,
• valg av hvilke terninger som skal kastes,
• gjøre spillet valgbart fra en meny som tilbyr ulike spill (se meny.py fra forelesing 7).



"""

#%% Imports
import tkinter as tk

#%%
def nyttKast(antallKast, listen, knapp):
    print("press")
    

#%%

def kast():
    antallKast = 0
    
    
    # Åpne vindu
    vindu = tk.Tk()
    vindu.minsize(400,400)
    vindu.title("Yatzy")
    
    # Legge inn en ramme
    ramme = tk.Frame(vindu)
    ramme.pack()
    
    
    
    kast1 = tk.Label(ramme, text="1", font=("Times",14, "bold"))
    kast1.grid(row=0,column=1)
    kast2 = tk.Label(ramme, text="2", font=("Times",14, "bold"))
    kast2.grid(row=0,column=2)
    kast3 = tk.Label(ramme, text="3", font=("Times",14, "bold"))
    kast3.grid(row=0,column=3)
    kast4 = tk.Label(ramme, text="4", font=("Times",14, "bold"))
    kast4.grid(row=0,column=4)
    kast5 = tk.Label(ramme, text="5", font=("Times",14, "bold"))
    kast5.grid(row=0,column=5)
    
    ramme2 = tk.Frame(vindu)
    ramme2.pack()
    listen = [kast1, kast2, kast3, kast4, kast5]
    
    knapp = tk.Button(ramme2, text = "Kast: 0", font=("Times",16, "bold"),  command= lambda: nyttKast(antallKast, listen, knapp))
    
    knapp.grid(row=2, column=3)
    vindu.mainloop()


def main():
    kast()
    
if __name__ == "__main__":
    main()