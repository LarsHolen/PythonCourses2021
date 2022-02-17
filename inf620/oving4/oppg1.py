# -*- coding: utf-8 -*-
"""
Created on Tue Sep 28 17:15:29 2021

@author: Lars Holen

"""

#%%
def main():
    test = input("Skriv noe, for å få returnert vokaler: ")
    print(antall_vokaler(test))
    
    
#%%    
def antall_vokaler(s):
    """
    Parameters
    ----------
    s : String
    
    DESCRIPTION.
    ----------
    Teller vokalene i s    
    
    Returns 
    ----------
    Antallet vokaler
    
    >>> antall_vokaler("Eirik")
    3
    >>> antall_vokaler("Åse")
    2
    """
    
    # Definerer en streng, hvor jeg vil lagre svar/resultatet
    result = 0
    
    # Looper gjennom strengen, bokstav for bokstav
    for c in s:
        # Ser om bokstaven eksisterer i en array med vokalene(store og små)
        if c in ("a", "e","i","o","u", "y", "æ","ø","å","A", "E","I","O","U", "Y", "Æ","Ø","Å"):
            # Når bokstaven finnes i vokal samlingen, så er den en vokal.  Legger den så til result strengen
            result = result + 1
            
    # returnerer resultatet
    return result

    
    
#%%    
def vokaler(s):
    """
    Parameters
    ----------
    s : String
    
    DESCRIPTION.
    ----------
    Lager en ny streng av vokalene i s    
    
    Returns 
    ----------
    Den nye strengen
    
    >>> vokaler("Eirik")
    Eii
    >>> vokaler("Åse")
    Åe
    """
    
    # Definerer en streng, hvor jeg vil lagre svar/resultatet
    result = ""
    
    # Looper gjennom strengen, bokstav for bokstav
    for c in s:
        # Ser om bokstaven eksisterer i en array med vokalene(store og små)
        if c in ("a", "e","i","o","u", "y", "æ","ø","å","A", "E","I","O","U", "Y", "Æ","Ø","Å"):
            # Når bokstaven finnes i vokal samlingen, så er den en vokal.  Legger den så til result strengen
            result = result + c
            
    # returnerer resultatet
    return result

    
#%%    
if __name__ == "__main__":
    main()