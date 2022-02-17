# -*- coding: utf-8 -*-
"""
Created on Wed Sep 22 19:09:46 2021

@author: Lars Holen

"""

import re

def main():
    print("Main running")
    
    # Lese inn ett navn fra bruker.  Angi sorteringsgrad etter hvor mange bokstavpar
    # ligger i rett rekkefølge. a-c er par, c-a er ikke.  Dvs ett korekt par, så
    # er neste bokstav etter i alfabetet.
   
    alfabetet = "abcdefghijklmnopqrstuvwxyzæøå"
    gjenta = True
    
    navn = input("Første navn: ")
    
    while gjenta:
        sorteringsgrad = 0
        navnLower = navn.lower()
        
        #Bruker regex for å fjerne uønskede tegn og tall.
        regex = re.compile('[^a-zA-Z]')
        navnLower = regex.sub('', navnLower)
        
        # Looper gjennom navnet, bokstav for bokstav og tester posisjon i alfabetet
        for index, bokstav in enumerate(navnLower):
           
            if(index < len(navnLower)-1):
                if(alfabetet.index(bokstav) < alfabetet.index(navnLower[index+1])):
                    sorteringsgrad += 1
        print(navn, "er et navn med sorteringsgrad", sorteringsgrad, ".")
        
        
        navn = input("Neste navn: ")
        
        if(navn == ""):
            gjenta = False
        
    
    
if __name__ == "__main__":
    main()