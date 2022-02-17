# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 18:44:42 2021

@author: Lars Holen

"""

# %% Hoved funksjon 

def main(): 
    # Kjører en "while" loop, så jeg kan be om ny input, uten å restarte 
    # programmet.  Mens "break" vil hoppe ut av loopen og stoppe programmet.
    while True:
        # Bruker "try" her, for å kunne fange opp om man skriver noe som
        # ikke er int/heltall.  Gi en feilmelding og la en prøve på nytt
        try:
            poeng = int(input("Oppnådde poeng på eksamen(0-100): "))
            if(poeng < 0 or poeng > 100):
                print("Ugyldig poengsum")
                # Bruker ikke break her, så looper man videre i while loopen
                # og man får skrive inn nytt tall uten å restarte programmet
            elif(poeng < 40):
                # 0 til 39 poeng er F
                print("Karakter: F")
                break
            elif(poeng < 50):
                # 40 til 49 poeng er E
                print("Karakter: E")
                break
            elif(poeng < 60):
                # 50 til 59 poeng er D
                print("Karakter: D")
                break
            elif(poeng < 80):
                # 60 til 79 er C
                print("Karakter: C")
                break
            elif(poeng < 90):
                # 80 til 89 poeng er B
                print("Karakter: B")
                break
            elif(poeng < 101):
                # 90 til 100 poeng er A
                print("Karakter: A")
                break
        except:
            print("Det er ikke ett heltall!")
            # Bruker ikke break her, så looper man videre i while loopen
            # og man får skrive inn nytt tall uten å restarte programmet
    
    
    # %% Sjekker om dette programmet heter "__main__", altså ikke importert som en pakke
    # Og kjører funksjonen main() om så
if __name__ == "__main__":
    main()