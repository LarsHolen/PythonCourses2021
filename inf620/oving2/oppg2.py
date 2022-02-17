# -*- coding: utf-8 -*-
"""
Created on Wed Sep  8 09:54:18 2021

Andre øvingsoppgave INF620 Høstsemesteret 2021

@author: Lars Holen

"""

def main():
    print("Main running")

    # OPPGAVE 2.A
    print("\n2.a")
    print("\n")
    

    x = 10 
    print("x = 10 gir type:", type(x))
    
    x = 10 + 10
    print("x = 10 + 10 gir type:", type(x))
    
    x = 5.5
    print("x = 5.5 gir type:", type(x))
    
    x = 10 + 5.5
    print("x = 10 + 5.5 gir type:", type(x))
    
    x = 5.5 + 5.5
    print("x = 5.5 + 5.5 gir type:", type(x))
    
    x = "abc"
    print("x = `abc` gir type:", type(x))
    
    x = "abc" + "5"
    print("x = `abc` + `5` gir type:", type(x))
    
    
    print("x = `abc` + 5 Gir error pga python vil ikke legge sammen teksten(str) abc og heltallet 5")
    
    x = "abc" + str(5)
    print("x = `abc` + str(5) gir type:", type(x))
    
   
    print(" x = `5` + 5 Gir error pga python vil ikke legge sammen teksten(str) 5 og heltallet 5")
    
    x = int("5") + 5
    print("x = int(`5`) + 5 gir type:", type(x))
       
    
if __name__ == "__main__":
    main()