# -*- coding: utf-8 -*-
"""
Created on Thu Nov  4 12:34:11 2021

@author: Lars Holen
INF621 - Høstsemesteret 2021
Øvingsoppgave 2

"""

#%% imports

from datetime import datetime
from datetime import timedelta
import locale

import locale

# Setting culture to norwegian
locale.setlocale(locale.LC_ALL, "no_NO")

#%% Oppgave 3 a)

def tidspunkt_om(n):
    datotidsObjektNow = datetime.now() 
    datotidsobjektInNSeconds = datotidsObjektNow + timedelta(0,n)
        
    print(datotidsobjektInNSeconds.strftime("%Y-%m-%d %H:%M:%S"))

    
    
"""
In [7]: tidspunkt_om(1)
2021-11-04 15:59:56
In [8]: tidspunkt_om(60)
2021-11-04 16:00:55
In [9]: tidspunkt_om(31536000)
2022-11-04 15:59:55

"""


#%% Oppgave 3b

def nedtelling():
      
    print("Antall hele dager igjen til nyttårsdag:", dagerTilDato(2022, 1, 1).days)
    print("Antall hele dager igjen til neste måned:", dagerTilDato(2021, 12, 1).days)
    print("Antall hele dager igjen til eksamen:", dagerTilDato(2021, 12, 17).days)
    print("Antall hele dager igjen til julaften:", dagerTilDato(2021, 12, 24).days)
    print("Antall hele dager igjen til 4. november klokken 15:59:54:", dagerTilDato(2022, 11, 4, 15, 59, 54).days)

"""
In [10]: nedtelling()
Antall hele dager igjen til nyttårsdag: 57
Antall hele dager igjen til neste måned: 26
Antall hele dager igjen til eksamen: 42
Antall hele dager igjen til julaften: 49
Antall hele dager igjen til 4. november klokken 15:59:54 : 364
"""

def dagerTilDato(y,m,d,h = 0, mi = 0, s = 0, ms = 0):
    datotimeNow = datetime.now()
    datetimeThen = datetime(y,m,d, h, mi, s, ms)
    return  datetimeThen - datotimeNow 
    
     

#%% main

def main():
    print("Main running")
    tidspunkt_om(1)
    tidspunkt_om(60)
    tidspunkt_om(31536000)
    nedtelling()
    
if __name__ == "__main__":
    main()