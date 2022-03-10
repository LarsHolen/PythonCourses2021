# -*- coding: utf-8 -*-
"""
Created on Wed Nov  3 20:35:41 2021

@author: Lars Holen

INF621 - Høstsemesteret 2021
Øvingsoppgave 2

"""

#%% Imports

from datetime import datetime
import locale

# Setting culture to norwegian
locale.setlocale(locale.LC_ALL, "no_NO")

#%% Oppgave 1. a)

def hva_er_klokken():
    timer = datetime.now().hour
    sekunder = datetime.now().second
    print("Klokken er " + str(timer) + ":" + str(sekunder))


# In [1]: hva_er_klokken()
# Klokken er 15:59

#%% Oppgave 1. b)

def ukedag():
    dag = datetime.now()
    print(dag.strftime("%A"))

# In [2]: ukedag()
# Det er torsdag!

#%% Oppgave 1. c)

def tidspunkt():
    datoTid = datetime.now()
    
    print("Det er", 
          datoTid.strftime("%A"),
          datoTid.strftime("%w") + ".", 
          datoTid.strftime("%B"), 
          "og klokken er",
          datoTid.strftime("%X") )

# In [3]: tidspunkt()
# Det er torsdag 4. november og klokken er 15:59:55




#%% main:
def main():
    hva_er_klokken()
    ukedag()
    tidspunkt()
    
if __name__ == "__main__":
    main()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    