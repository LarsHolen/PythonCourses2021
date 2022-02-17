# -*- coding: utf-8 -*-
"""
Created on Wed Sep  8 10:21:45 2021

Andre øvingsoppgave INF620 Høstsemesteret 2021

@author: Lars Holen

"""

from math import pi


def main():
    print("Main running")
    
    # OPPGAVE 3.A
    print("\n3.a")
    print("Svar: %2.2f" %(pi**2))
         
    # OPPGAVE 3.B
    print("\n3.b")
    print("%-13s" %"Navn", "%13s" %"Larry", "%13s" %"Roger", "%13s" %"Graham")
    
     # OPPGAVE 3.C
    print("\n3.c")
    print("%-13s" %"Sted", "%13s" %"27. jan", "%13s" %"28. jan", "%13s" %"29. jan")
    print("-" * 56)
    print("%-13s" %"Geilo", "%13.2f" %(0.482), "%13.2f" %(0.501) ,"%13.2f" %(0.440))
    print("%-13s" %"Hemsedal", "%13.2f" %(0.472), "%13.2f" %(0.455) ,"%13.2f" %(0.454))
    print("%-13s" %"Sirdal", "%13.2f" %(0.253), "%13.2f" %(0.212) ,"%13.2f" %(0.200))
    
    
    
if __name__ == "__main__":
    main()