# -*- coding: utf-8 -*-
"""
Created on Mon Sep 13 15:02:03 2021

@author: Lars Holen

"""

def main():
    myList = range(10)
    myList2 = sorted(myList)
    for i, item in enumerate(myList2):
        print("Main running: " + str(i % i) +"___" +  str(item))
    
    
if __name__ == "__main__":
    main()