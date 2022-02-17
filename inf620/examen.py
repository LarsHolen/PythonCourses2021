# -*- coding: utf-8 -*-
"""
Created on Fri Oct 22 09:21:09 2021

@author: Lars Holen

Skrivenfunksjonerfaringsomtarsomparameterenstrengnavn,enstrengsted,ogetheltallteller.Funksjonenskalskriveutstrengen'navnharværtistedminsttellerganger'medparameterverdienesattinnistrengen.EksempelpåutskriftfrakjøringavfunksjonenfrakonsolleniSpyder:In [1]: erfaring('Per', 'Bergen', 15)Per har vært i Bergen minst 15 gangerIn [2]: erfaring('Anne', 'Oslo', 4)Anne har vært i Oslo minst 4 ganger



"""

def erfaring(navn, sted, teller):
    print(navn, "har vært i", sted, "minst", str(teller), "ganger")
    
    
def sensurer(streng, tabu):
    resultatStreng = ""
    for i in streng:
        if tabu.find(i) != -1:
            resultatStreng += "*"
        else:
            resultatStreng += i
    return resultatStreng

def quiz(spørsmål, svar):
    antallRiktige = 0;
    i = 0
    while(i < len(spørsmål)):
        
        mittSvar = input(spørsmål[i] + " ")
        if mittSvar.lower() == svar[i].lower():
            print("Riktig!")
            antallRiktige += 1
        else:
            print("Feil. Riktig svar er", svar[i])
        i += 1
    return antallRiktige

def vri(streng):
    resultatStrengVenstre = ""
    resultatStrengHøyre = ""
    for index, i in enumerate(streng):
        if index %2 == 0:
            # Partall
            resultatStrengVenstre += i
        else:
            resultatStrengHøyre += i
    return resultatStrengVenstre + resultatStrengHøyre

"""
milliarderListe = []
while True:
    try:
        inn = input("Formue i hele milliarder: ") 
        if inn == "":
            if len(milliarderListe) > 0:
                milliarderListe.sort(reverse=True)
                antallInput = len(milliarderListe)
                rikereEnnAlle = 0
                i = 0
                while(True):
                    i += 1
                    rikereEnnAlle += milliarderListe.pop(0)
                    if rikereEnnAlle > sum(milliarderListe):
                        print("De", i, "rikeste til sammen er rikere enn de", antallInput-i, "andre til sammen.")
                        break
                break
            else:
                break
        else:
            heltall = int(inn)
            milliarderListe.append(heltall)
    except:
        print("Det er ikke ett heltall!")


brukerId = str(input("Brukerid: "))
if len(brukerId) == 6 and brukerId[0 : 3].isalpha() and brukerId[3 : 6].isnumeric():
    print(brukerId, "er ett gyldig brukerid")
else:
    print(brukerId, "er ikke gyldig brukerid")
    
"""
from random import randint
def kast(n):
    result = True
    resultatListe = []
    for i in range(n):
        resultatListe.append(randint(1, 6))
    print(*resultatListe, sep=", ")
    for i in range(min(resultatListe), max(resultatListe)):
        if resultatListe.count(i) < 1:
            result = False
            break
    
    return result

def strake(m,n):
    # n antall terninger
    # m hvor mange sammenhengende kast etter hverandre
    mOrg = m
    result = 0
    while (m > 0):
        result += 1
        if kast(n):
            m -= 1
        else:
            m = mOrg
    print(mOrg, "strake sammenhengende kast med", n, "terninger etter", result, " omganger")
            
    
    





