# -*- coding: utf-8 -*-
"""
Created on Thu Feb 11 19:42:58 2021

@author: larsh
"""

# %% Definerer variabler

odd = (1,3,5,7,9,11,13)
primes = (2,4,6,8,10,12)
mix = odd + primes


# %% Skriv til skjerm

print("11 finnes ", mix.count(11), "ganger i mix.")
print("Finnes 14 i mix? ", mix.__contains__(14))