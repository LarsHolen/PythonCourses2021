# -*- coding: utf-8 -*-
"""
Created on Tue Dec  7 18:38:47 2021

@author: Lars Holen

Øving 4 

Oppgave 2

Flere norske kommuner er preget av fraflytting. Statistisk sentralbyrå gir på https:
//data.ssb.no/api/v0/dataset/26975.json?lang=no oversikt over folketallsutviklingen 
i norske kommuner fra 1986 til 2021. Dataene er gitt på json-format.
Hvis nettleseren din ikke gjør det mulig å visualisere dataene, kan du bruke https:
//jsonformatter.org/json-parser til dette.

"""

#%% Imports

# Importing json for parsing the data
#from json import loads

# Import get to download url
#from requests import get

#%% Oppgave 2. a)
"""
Gjør deg kjent med hvordan dataene er strukturerte. Observer at det finnes data
for totalt 359 kommuner, og at hver kommune har en egen id. Data du vil ha nytte
av finner du under:
• dataset/dimension/Region/category/index: En indeks for hver id
• dataset/dimension/Region/category/label: Kommunenavn for hver id
• dataset/value: Folketall
For hver kommune finnes det folketall for hvert av årene 1986, . . . , 2021, altså 36
år. Under dataset/value finner du totalt 359 · 36 = 12924 folketallsverdier. De 36
første er befolkningen i kommunen med indeks 0 i årene 1986, . . . , 2021. De 36 neste
er befolkningen i kommunen med indeks 1 i årene 1986, . . . , 2021, etc.
Ingen innlevering i denne deloppgaven.
"""

#%% Oppgave 2. b)
"""
Bruk modulene json og requests til å hente data fra nettsiden inn i din egen
pythonkode: Lag først en oppslagstabell (dict) som svarer til hele datamengden.
Plukk deretter ut de data du trenger i form av
• en oppslagstabell som svarer til dataset/dimension/Region/category/index,
• en oppslagstabell som svarer til dataset/dimension/Region/category/label,
• og en liste som svarer til dataset/value
Vi går ut fra at årene dataene er gitt for ligger fast, og dermed kan hardkodes hos
oss. Merk imidlertid at koden vår ikke lenger vil fungere dersom datasettet utvides
til f.eks. 2022. Idéelt sett burde koden lese hvilke år dataene er gitt for fra nettsiden,
men dette er ikke påkrevd i oppgaven
"""
def LesSSBData():
    url = "https://data.ssb.no/api/v0/dataset/26975.json?lang=no"
    dataGet = get(url)
    dataText = loads(dataGet.text)
    dataSet = dataText["dataset"]
    labelKommune = dataSet["dimension"]["Region"]["category"]["label"]
    indexKommune = dataSet["dimension"]["Region"]["category"]["index"]
    indexTid = dataSet["dimension"]["Tid"]["category"]["index"]
    tidListe = indexTid.keys()
    #antallÅr = len(tidListe)
    value = dataSet["value"]
    
    return indexKommune, labelKommune, value, tidListe
   



    

#%% Oppgave 2. c)
"""
Blant kommunene med positiv verdi i dataset/value hvert år, plukk ut de åtte
kommunene med størst relativ nedgang fra 1986 til 2021 (minst forhold mellom
folketallene i 2021 og 1986). Lag et stolpediagram over disse kommunene, hvor
folketallene i 1986 og 2021 presenteres med hver sin farge.
"""
def Plot8KommunerMedMestNedgangIFolketall():
    indexKommune, labelKommune, value, tidListe = LesSSBData()
    
    relativVekst = []
    for i, kommune in enumerate(indexKommune):
        #print(labelKommune[kommune], value[0 + i *(len(tidListe))], value[(len(tidListe)-1) + i * (len(tidListe))]  )
        rVekst = value[(len(tidListe)-1) + i * (len(tidListe))]  - value[0 + i *(len(tidListe))]
        if rVekst == 0:
            rVekst = 1000000000
        relativVekst.append(rVekst)
    
    bunnÅtteIVekst = []
    while (len(bunnÅtteIVekst) < 8):
        minVekst_tall = min(relativVekst)
        minVekst_index = relativVekst.index(minVekst_tall)
        bunnÅtteIVekst.append(minVekst_index)
        relativVekst[minVekst_index] = 1000000000
    for ind in bunnÅtteIVekst:
        kNum = indexKommune.values()
        print(kNum)
        
        
        #for j in range(len(tidListe)):
            #index = j + i*(len(tidListe)-1)
            #folketallListe += value[index] 
         #   print(labelKommune[kommune], value[0 + i *(len(tidListe)-1)], value[len(tidListe) + i *(len(tidListe)-1)]  )
  
            
 
            



#%% Main


from json import loads
from requests import get
from matplotlib import pyplot

ssburl = 'https://data.ssb.no/api/v0/dataset/26975.json?lang=no'
data = get(ssburl)
oppslag = loads(data.text)
index = oppslag['dataset']['dimension']['Region']['category']['index']
label = oppslag['dataset']['dimension']['Region']['category']['label']
value = oppslag['dataset']['value']
førsteår = 1986
sisteår = 2021
antår = sisteår-førsteår+1

oversikt = {}
for kid in label:
    folk = []
    folkfør = value[antår*index[kid]]
    folkno = value[antår*index[kid]+antår-1]
    if min(value[antår*index[kid]:antår*(index[kid]+1)]) > 0:
        forhold = folkno / folkfør
        oversikt[kid] = forhold
liste = sorted(oversikt, key=oversikt.get)[:8]
kommune = []
folkfør = []
folkno = []
for kid in liste:
    kommune.append(label[kid])
    folkfør.append(value[antår*index[kid]])
    folkno.append(value[antår*index[kid]+antår-1])
    
pyplot.bar(kommune, folkfør, width=-0.4, align='edge',
           color='blue', label=str(førsteår))
pyplot.bar(kommune, folkno, width=0.4, align='edge',
           color='red', label=str(sisteår))
pyplot.legend()
pyplot.show()

folk = []
kid = liste[0]
for år in range(førsteår, sisteår+1):
    folk.append(value[antår*index[kid]+år-førsteår])
tid = list(range(førsteår, sisteår+1))
pyplot.plot(tid, folk, label = 'Folketalsutvikling i '+kommune[0])
pyplot.legend()
pyplot.show()

    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    