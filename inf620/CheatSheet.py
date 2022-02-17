# -*- coding: utf-8 -*-
"""
Created on Tue Sep  7 18:49:37 2021

@author: Lars Holen

"""
import decimal
from math import pi



"""
CHEAT SHEET:::
    
    Enkel loop
    
    
    for i in range(10):
        print("Main running: " + str(i))
    
    for n in numbers:
        print(n)
    
    
    Looper to lister på en gang(stopper ved korteste liste)
    for header, rows in zip(headers, columns):
        print("{}: {}".format(header, ", ".join(rows)))

    Loop med index
    for num, line in enumerate(lines):
        print("{0:03d}: {}".format(num, line))
      
        
      
        GET INPUT
     while True:
        try:
             heltall1 = int(input("Skriv inn ett heltall: "))
             print("Takk!")
             break
        except:
            print("Det er ikke ett heltall!")



    STRING FORMAT OLD STYLE  print("%-20s %10s %15d" %("Start", "Minimum:", heltall1))



DICTIONARY SWITCH:
    
def f(): pass
def g(): pass
def default(): pass

_switch_dic = {0: f, 1:g, 2,:g, 3:f}

def switch_dict_sample(x):
    do_next = _switch_dic.get(x, default=default)
    do_next()
    

"""
