# -*- coding: utf-8 -*-
"""
Created on Tue Nov 23 14:39:06 2021

@author: Lars Holen

"""

#%% Import 

from json import loads
from requests import get

ssburl = "https://data.ssb.no/api/v0/dataset/85430.json?lang=no"
data = get(ssburl)
tabell = loads(data.text)
areal = tabell["dataset"]
label = areal["dimension"]["Region"]["category"]["label"]
index = areal["dimension"]["Region"]["category"]["index"]
value = areal["value"]

oversikt = {}

for id in label:
    land = value[index[id]*2]
    vatn = value[index[id]*2+1]
    forhold = vatn/(land+vatn)
    oversikt[id] = (forhold, land, vatn)
    
liste = sorted(oversikt, key=oversikt.get, reverse=True)[:10]
for id in liste:
    (forhold, land, vatn) = oversikt[id]
    print("%-20s %9.2f %9.2f  %9.2f" % (label[id], forhold, land, vatn))


def main():
    print("Main running")
    
if __name__ == "__main__":
    main()