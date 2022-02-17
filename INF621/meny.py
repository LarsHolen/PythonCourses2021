# -*- coding: utf-8 -*-
"""
Created on Tue Dec  7 15:22:44 2021

@author: Lars Holen

"""


from tkinter import *
def spill():
    vindu = Tk()
    vindu.minsize(400,400)
    vindu.title("Mitt vindu")
    
    menybar = Menu(vindu)
    terningmeny = Menu(vindu)
    kortmeny= Menu(vindu)
    
    menybar.add_cascade(label="Terningspill", menu = terningmeny)
    menybar.add_cascade(label="Kortspill", menu = kortmeny)
    
    terningmeny.add_command(label="Yatzy", command=todo)
    terningmeny.add_command(label="Ludo", command=todo)
    
    kortmeny.add_command(label="Bridge", command=todo)
    kortmeny.add_command(label="21", command=todo)
    
    ramme = Frame(vindu)
    tekst = Label(ramme, text="Test")
    ramme.pack()
    
    vindu.config(menu=menybar)
    
    vindu.mainloop()

def todo():
    print("TODO")

def main():
    spill()
    
if __name__ == "__main__":
    main()