# -*- coding: utf-8 -*-
"""
Created on Wed Sep  8 11:01:12 2021

Andre øvingsoppgave INF620 Høstsemesteret 2021

@author: Lars Holen

"""

def main():
    print("Main running")
    
    # OPPGAVE 4.A
    print("\n4.a")
  
    while True:
        try:
             heltall1 = int(input("Skriv inn ett heltall: "))
             print("Takk!")
             break
        except:
            print("Det er ikke ett heltall!")
            
            
    while True:
        try:
             heltall2 = int(input("Skriv inn ett heltall til: "))
             print("Takk!")
             break
        except:
            print("Det er ikke ett heltall!")
            
            
    print("\n")
    print("%-13s" %"Sum:", "%-15d" %(heltall1 + heltall2))
    print("%-13s" %"Differanse:", "%-15d" %(heltall1 - heltall2)) 
    print("%-13s" %"Produkt:", "%-15d" %(heltall1 * heltall2))
    print("%-13s" %"Gjennomsnitt:", "%-15.2f" %((heltall1 + heltall2)/2))
    print("%-13s" %"Distanse:", "%-15d" %(abs(heltall1 - heltall2)))
    print("%-13s" %"Maximum:", "%-15d" %max((heltall1, heltall2)))
    print("%-13s" %"Minimum:", "%-15d" %(min(heltall1, heltall2)))
    
    print("%-20s %10s %15d" %("Start", "Minimum:", heltall1))
    


if __name__ == "__main__":
    main()