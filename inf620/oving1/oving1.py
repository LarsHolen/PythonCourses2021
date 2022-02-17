# -*- coding: utf-8 -*-
"""
Created on Tue Aug 31 19:11:14 2021

Første øvingsoppgave INF620 Høstsemesteret 2021

@author: Lars Holen

"""

# 3.a

h = 'Hello'
w = 'World'
print(h + ' ' + w)

# 3.b

print(4 + 3 * 7)

# 4.a

dollarkurs = 9.17
pris_I_Kroner_Headset = 1500

#Runder av til to desimaler
pris_I_Dollar_Headset = round(pris_I_Kroner_Headset / dollarkurs,2)
print("Headsettet koster:", pris_I_Dollar_Headset, "dollar.")

# 4.b

tekst = "Mitt navn er"
myName = "Lars Holen"
fullTekst = tekst + " " + myName
print(fullTekst)

