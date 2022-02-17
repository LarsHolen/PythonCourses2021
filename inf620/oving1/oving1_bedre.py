# -*- coding: utf-8 -*-
"""
Created on Sun Sep  5 22:56:25 2021

@author: Lars Holen

Øving nr 1 INF 620

"""


    
# 3.a
def oppgave3a():
    h = 'Hello'
    w = 'World'
    print(h + ' ' + w)

# 3.b
def oppgave3b():
    print(4 + 3 * 7)

# 4.a
def oppgave4a():
    dollarkurs = 9.17
    pris_I_Kroner_Headset = 1500

    #Runder av til to desimaler
    pris_I_Dollar_Headset = round(pris_I_Kroner_Headset / dollarkurs,2)
    print("Headsettet koster:", pris_I_Dollar_Headset, "dollar.")

# 4.b
def oppgave4b():
    tekst = "Mitt navn er"
    myName = "Lars Holen"
    fullTekst = tekst + " " + myName
    print(fullTekst)



# Funksjon som kjører alle oppgave funksjonene
def main():
    print("Oppgaver:\n")
    
    print("3.a")
    oppgave3a()
    print("\n")
    
    print("3.b")
    oppgave3b()
    print("\n")
    
    print("4.a")
    oppgave4a()
    print("\n")
    
    print("4.b")
    oppgave4b()
    print("\n")
    
    print("\nSlutt")
    

# Denne kjøres kun når en kjører denne filen, ikke om den blir importert i en
# annen fil som kjøres    
if __name__ == "__main__":
    main()
    