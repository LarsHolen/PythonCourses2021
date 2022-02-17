# -*- coding: utf-8 -*-
"""
Created on Thu Sep 16 18:38:28 2021

@author: Lars Holen

"""
import timeit
import string
import random







def main():
    print("Main running")
    # Make a list with two non repeating characters b and c 
    myList = []
    listLength = 100000          
    for i in range(listLength):
        a = random.choice(string.ascii_lowercase)
        if(a == "b"):
            myList.append("a")
        elif(a == "c"):
            myList.append("a")
        else:
            myList.append(a)
        #
    
    myList[random.randint(0, listLength)] = "b"
    myList[random.randint(0, listLength)] = "c"
    firstNonDuplicate(myList)
    firstNonDuplicate1(myList)
    

def firstNonDuplicate1(l):
    
        for loc, i in enumerate(l):
            if i not in l[loc + 1:-1]:
                # Doesnt exist in dictionary.  We add it and set value to its location
                print("First non duplicate is at position: ", loc, " And is char: ", i )
                return


def firstNonDuplicate(l):
        dictionaryList = {}
        for loc, i in enumerate(l):
            if(dictionaryList.get(i) == None):
                # Doesnt exist in dictionary.  We add it and set value to its location
                dictionaryList[i] = loc
                
            else:
                dictionaryList[i] = -1
        #print(dictionaryList)                         
        for d in dictionaryList:
            #print(d, "--", num )
            if(dictionaryList[d] != -1):
                print("First non duplicate is at position: ", dictionaryList[d], " And is char: ", d )
                print(dictionaryList)
                return
        print("No non duplicates")    
        print(dictionaryList)
  
if __name__ == "__main__":
    main()