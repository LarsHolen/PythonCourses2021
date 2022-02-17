# -*- coding: utf-8 -*-
"""
Created on Tue Nov 30 14:56:49 2021

@author: Lars Holen

"""
from tkinter import *



def svar():
    tekst = "Du heiter altså: " + navn.get().title()
    konklusjon.config(text = tekst)
    


vindu = Tk()
vindu.minsize(400,400)
vindu.title("Strenginnlesing")

ramme = Frame(vindu)
ramme.pack()

forklaring = Label(ramme, text = "Navn:)")
forklaring.pack()

navn = StringVar(ramme, "-----")
lesefelt = Entry(ramme, textvariable = navn)
lesefelt.pack()

knapp = Button(ramme, text = "Ok", command=svar)
knapp.pack()

konklusjon = Label(ramme, text = "")
konklusjon.pack()

inf621 = ["Lars", "Nova", "Ada", "Luna", "Kara"]

def func1():
    indeksar = liste.curselection()
    for i in indeksar:
        namn = liste.get(i)
        if namn not in utvalgsliste.get(0, END):
            utvalgsliste.insert(END, namn)

def func2():
    indeksar = liste.curselection()
    for i in indeksar:
        namn = liste.get(i)
        if namn in utvalgsliste.get(0, END):
            indeks = utvalgsliste.get(0,END).index(namn)
            utvalgsliste.delete(indeks)
            
            

ramme3 = Frame(vindu)
ramme3.pack()

rulle = Scrollbar(ramme3)
rulle.pack(side=RIGHT, fill=Y)
liste = Listbox(ramme3, height=3, selectmode=MULTIPLE, yscrollcommand=rulle.set)
for namn in inf621:
    liste.insert(END, namn)
liste.pack()
rulle.config(command=liste.yview)

ramme4 = Frame(vindu)
ramme4.pack()

jaknapp = Button(ramme4, text="Ja", command = func1)
jaknapp.grid(row=0, column=0)
neiknapp = Button(ramme4, text = "Nei", command= func2)
neiknapp.grid(row=0, column=1)



ramme6 = Frame(vindu)
ramme6.pack()
utvalgsliste = Listbox(ramme6)
utvalgsliste.pack()



vindu.mainloop()
"""

# Basic vindu
vindu = Tk()
vindu.minsize(400,200)
vindu.title("Mitt vindu") 

# ramme
ramme = Frame(vindu)
ramme.grid(row=0, column=0)


# Button
knapp = Button(ramme, text="Trykk")
knapp.pack()


tekst = Label(ramme,text="Hei")
tekst.pack()

val = Checkbutton(ramme, text="forstått")
val.pack()

# ny ramme
nyramme = Frame(vindu)
nyramme.grid(row=0, column=1)


nyknapp = Button(nyramme, text="Trykk ramme2)")
nyknapp.pack()

nytekst = Label(nyramme, text = "Hei2)")
nytekst.pack()


forklaring = Label(ramme, text = "Forklaring:")
forklaring.pack()
lesefelt = Entry(ramme)
lesefelt.pack()

liste = Listbox(nyramme, height=4, selectmode=MULTIPLE)
liste.pack()
liste.insert(END, "Navn1")
liste.insert(END, "Navn2")
liste.insert(END, "Navn3")
liste.insert(END, "Navn4")
liste.insert(END, "Navn5")
liste.insert(END, "Navn6")
liste.insert(END, "Navn7")
liste.insert(END, "Navn8")
liste.insert(END, "Navn9")
liste.insert(END, "Navn10")
liste.insert(END, "Navn11")
liste.insert(END, "Navn12")
"""




vindu.mainloop()