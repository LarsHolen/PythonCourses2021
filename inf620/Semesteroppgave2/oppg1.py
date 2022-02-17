# -*- coding: utf-8 -*-
"""
Created on Tue Oct  5 16:51:21 2021

@author: Lars Holen

Semesteroppgave 2
INF620 - Høstsemesteret 2021

"""


#%%
"""
Oppgave 1. a):

Skriv en funksjon les som leser inn så mange personnavn (strenger) som
brukeren ønsker å gi. Innlesing avsluttes med en tom streng. Funksjonen skal
returnere en liste med de innleste navnene. Som parameter skal funksjonen ta
en streng som sier hvilken kategori (f.eks. ‘gruppeleder’ eller ‘administrator’)
personene tilhører.

"""

def les(kategori):
    """
    Parameters
    ----------
    kategori : string
        En streng som skal velge gruppeleder eller administrator

    Returns
    -------
    l : List
        Returnerer en liste med gruppeledere eller administratorer's navn.
        Ved feil kategori, returneres en liste med ett element "ugyldig kategori"

    """
    # Sjekker om man har skrevet inn korrekte kategorier.
    # Bruker .lower() for å tillate feil med stor bokstav
    # Ved ugyldig kategori skriver vi "ugyldig kategori"
    # og returnerer en liste med ett element som er "ugyldig 
    # kategori"
    if(kategori.lower() == "gruppeleder"):
        kategori = kategori.lower()
        
    elif(kategori.lower() == "administrator"):
        kategori = kategori.lower()
    else:
        print("Ugyldig kategori");
        l = ["ugyldig kategori"]
        return l
    
    # Looper til vi får en blank streng som input
    # Lagrer navn i listen l
    l = []       
    n = str(input("Første %s : " % (kategori)))
    while True:
       try:   
            if(n != ""):
                l.append(n)
                n = str(input("Neste %s : " % (kategori)))
                continue
            else:
                break
       except:
           print("Feil!")
    return l
#%%
    
"""
Oppgave 1. b):

Skriv en funksjon skriv_pent som tar en liste med strenger som parameter, 
og som skriver ut strengene med stor forbokstav og med små bokstaver
ellers.

"""   

def skriv_pent(minListe):
    """
    Parameters
    ----------
    minListe : List
        Tar inn en liste med strenger, og skriver strengene til skjerm etter
        å ha brukt title() funksjonen på de. Dette gjør at alle ord vil få
        stor forbokstav om det er første bokstav, har ett ikke alfabetisk
        tegn forran, eller har mellomrom forran.

    Returns
    -------
        None.

    """
    # Looper gjennom listen og bruker string.title() funksjonen
    # på hvert ord, og skriver de til skjermen
    for i in minListe:
        print(i.title())

#%%
    
"""
Oppgave 1. c):

Skriv en funksjon flett som tar to lister (liste1 og liste2) som
parametre, og som returnerer en ny liste som består av elementene i liste1
og liste2. I listen som returneres skal rekkefølgen være slik at elementene fra
1
liste1 og liste2 kommer vekselvis, dvs, liste1[0], liste2[0], liste1[1],
liste2[1], . . ., så langt det finnes element i begge listene.

"""   

#  Fletter elementene fra listene, frem til lengden av den korteste listen
# og ignorerer rest i den lengste listen

def flett(liste1, liste2):
    """
    Parameters
    ----------
    liste1 : List
        En liste med hva som helst
    liste2 : List
        En liste med hva som helst.

    Returns
    -------
    result : List
        liste1 og liste2 blir blandet annenhver frem til lengden av 
        korteste liste, resterende blir ignorert.

    """
    result = []
    # Bruker zip, for å loope gjennom begge listene på en gang.  zip looper
    # bare til den korteste listen slutter.
    for i1, i2 in zip(liste1, liste2):
        result.append(i1)
        result.append(i2)
    
    return result

# Sidenote::::
# Funksjon som fletter to lister og fyller på med elementene 
# fra den lengste listen når den ene listen går tom

def flett2(liste1, liste2):
    """
    Parameters
    ----------
    liste1 : List
        En liste med hva som helst
    liste2 : List
        En liste med hva som helst.

    Returns
    -------
    result : List
        liste1 og liste2 blir blandet annenhver frem til lengden av 
        korteste liste, resterende av den lengre listen blir lagt til 
        på slutten av resultat listen.

    """
    # Sjekker om listene er like lange.  Om ikke, så utviders den korteste 
    # listen til lik lengde med å fylle på med None
    if len(liste1) < len(liste2):
        liste1.extend([None] * (len(liste2) - len(liste1)))
    else:
        liste2.extend([None] * (len(liste1) - len(liste2)))
        
    # Definerer en liste som skal inneholde resultatet
    result = []
  
    # Bruker zip, for å loope gjennom begge listene på en gang.  zip looper
    # bare til den korteste listen slutter, derfor ble listene gjort like lange.
    for i1, i2 in zip(liste1, liste2):
        # Legger ett element fra hver liste til result listen, for hver 
        #iterasjon
        result.append(i1)
        result.append(i2)
    # Bruker filter for å fjerne alle None elementer i resultatet
    result = list(filter((None).__ne__, result))
    # returnerer result listen
    return result


#%%
"""
Oppgave 1. d):

Skriv en funksjon skriv_pent som tar en liste med strenger som parameter, 
og som skriver ut strengene med stor forbokstav og med små bokstaver
ellers.

"""   

def korriger(minListe):
    """
    Parameters
    ----------
    minListe : List
        Tar en liste med strenger som skal korrigeres med title() funksjonen

    Returns
    -------
    None.

    """
    # Looper gjennom listen og bruker string.title() funksjonen
    # på hvert element, og skriver de tilbake i listen på samme plass
    for i in range(len(minListe)):
        minListe[i] = minListe[i].title()  
    
