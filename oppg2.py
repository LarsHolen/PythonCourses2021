# -*- coding: utf-8 -*-
"""
Created on Wed Nov  3 21:20:34 2021

@author: Lars Holen


INF621 - Høstsemesteret 2021
Øvingsoppgave 2

"""

#%% Imports

from datetime import datetime
import locale

# Setting culture to norwegian
locale.setlocale(locale.LC_ALL, "no_NO")

#%% Oppgave 2 a)

def parse_1(d):
    dateTimeObj = datetime.strptime(d, "%d.%m.%y")
    
    return dateTimeObj

# In [4]: parse_1('04.11.21')
# Out[4]: datetime.datetime(2021, 11, 4, 0, 0)


#%% Oppgave 2 b)

def parse_2(d):
    dateTimeObj = datetime.strptime(d, "%d. %B %Y")
    
    return dateTimeObj

# In [5]: parse_2('4. november 2021')
# Out[5]: datetime.datetime(2021, 11, 4, 0, 0)


#%% Oppgave 2 c)

def parse_3(datostring):
    datoTidObjekt = datetime.strptime(datostring, "%d/%m-%Y %H:%M:%S")
    return datoTidObjekt    
    
# In [6]: parse_3('04/11-2021 15:59:55')
# Out[6]: datetime.datetime(2021, 11, 4, 15, 59, 55)



#%% main  
def main():
    print("Main running")
    print(parse_1("04.11.21"))
    print(parse_2('4. november 2021'))
    print(parse_3('04/11-2021 15:59:55'))
    
if __name__ == "__main__":
    main()