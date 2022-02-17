# -*- coding: utf-8 -*-
"""
Created on Wed Sep  8 08:31:15 2021

Andre øvingsoppgave INF620 Høstsemesteret 2021

@author: Lars Holen

"""

import decimal


def main():
    print("Main running")
    
    
    # OPPGAVE 1.A
    print("\n1.a")
    print("\n")
    
    print("9 - 3 =", 9 - 3) #  6
    print("\n")
    
    print("8 * 2.5 =", 8 * 2.5 ) #  20.0
    print("\n")
    
    print("9 / 2 =", 9 / 2 ) # 4.5
    print("\n")
    
    print("9 / -2 =", 9 / -2 ) # -4.5
    print("\n")
    
    print("9 // -2 =", 9 // -2) #  -4, her tok jeg feil.  -5 korrekt svar
    print("\n")
    
    print("9 % 2 =", 9 % 2 ) # 1  
    print("\n")
    
    print("9.0 % 2 =", 9.0 % 2 ) # 1.0
    print("\n")
    
    print("9 % 2.0 =", 9 % 2.0 ) # 1.0  
    print("\n")
    
    print("9 % -2 =", 9 % -2 ) # 1, -1 er korrekt
    print("\n")
    
    print("-9 % 2 =", -9 % 2 ) # -1, 1 er korrekt
    print("\n")
    
    print("9 / -2.0 =", 9 / -2.0 ) # -4.5
    print("\n")
    
    print("4 + 3 * 5 =", 4 + 3 * 5 ) # 19
    print("\n")
    
    print("abs(5 - 10) =", abs(5-10) ) # 5
    print("\n")
    
     # OPPGAVE 1.B
    print("\n1.b")
    print("\n")
    
    
    print("3 opphøyd i potens 6 = ", 3 ** 6 ) 
    print("\n")
    
    
    print("4 multiplisert med 2, og dette resultatet addert med 3 = ", 4 * 2 + 3 ) 
    print("\n")
    
    print("4 pluss 2, og dette resultatet multiplisert med 3 =", (4 + 2) * 3 ) 
    print("\n")
    
    print("Antall hele ganger 6 går opp i 100 =", 100 // 6 ) 
    print("\n")
    
    print("Resten man får ved å dele 100 på 6 =", 100 % 6 ) 
    print("\n")
    
    print("100 delt nøyaktig på 6 = ", 100 // 6, str(100 % 6) + "/6")
    print("\n")
    
    print("Eller med float presisjon:")
    print("100 delt nøyaktig(float) på 6 = ", 100.0 / 6.0)
    print("\n")
    
    print("Eller:")
    print("For å få flere desimaler, importerer jeg klassen decimal.")
    print("Decimal er ikke ett tall som int eller float, men kan bruke noen")
    print("matematiske funksjoner.")
    print("Velg antall desimaler i linjen: decimal.getcontext().prec = 1000")
    decimal.getcontext().prec = 1000
    print("100 delt på 6 med 1000 desimaler =", decimal.Decimal(100) / decimal.Decimal(6) ) 
    print("(Se avrundingen er forskjellig i float og decimal)")
    
    
    y = int(input("Skriv et årstall: ")) # Spør brukeren om et årstall y
    a = y % 19      # Del y på 19 og kall resten for a. Ignorer kvotienten.
    b = y // 100    # Del y på 100 slik at du får en kvotient b 
    c = y % 100     # og en rest c.
    d = b // 4      # Del b på 4 slik at du får en kvotient d 
    e = b % 4       # og en rest e.
    g = (8 * b + 13) // 25 # Del 8 ∗ b + 13 på 25 slik at du får en kvotient g. Ignorer resten.
    h = (19 * a + b - d - g + 15) % 30 # Del 19 ∗ a + b − d − g + 15 på 30 slik at du får en rest h. Ignorer kvotienten
    j = c // 4      # Del c på 4 slik at du får en kvotient j 
    k = c % 4       # og en rest k.
    m = (a + 11 * h) // 319 # Del a + 11 ∗ h på 319 slik at du får en kvotient m. Ignorer resten.
    r = (2*e +2*j -k -h + m + 32) % 7 # Del 2 ∗ e + 2 ∗ j − k − h + m + 32 på 7 slik at du får en rest r.
    n = (h - m + r + 90) // 25 # Del h − m + r + 90 på 25 slik at du får en kvotient n. Ignorer resten.
    p = (h - m + r + n + 19) % 32 # Del h − m + r + n + 19 på 32 slik at du får en rest p. Ignorer kvotienten.
    
    print("Første påskedag faller på dag", p, " av måneden", n)
    
    
    
    
if __name__ == "__main__":
    main()