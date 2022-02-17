# -*- coding: utf-8 -*-
"""
Created on Wed Sep 22 17:36:29 2021

@author: Lars Holen

"""

def main():
    print("Main running")
    
    # PW must contain lowercase, uppercase, digit, special char 
    # and be atleast 8 chars long
    # Variable for each requirement set to false
    containsLowercase = False
    containsUppercase = False
    containsDigit = False
    containsSpecial = False
    containsMoreThan8Chars = False
   
    # Get input from user
    pw = input("Passord: ")
    
    # Test each requirement and change variable if it passes 
    # Testing length
    if(len(pw) >= 8):
        containsMoreThan8Chars = True

    # Looping through the password, and chech every character for requirements
    for character in pw:
        if(character.islower()):
            containsLowercase = True
        if(character.isupper()):
            containsUppercase = True
        if(character.isdigit()):
            containsDigit = True
        if(not character.islower() and not character.isupper() and not character.isdigit()):
            containsSpecial = True
            
     
    # Put all requirements in a list to easily test if all 5 are True
    requirementsList = [containsLowercase, containsUppercase, containsDigit, containsSpecial, containsMoreThan8Chars]
    if(requirementsList.count(True) == 5):
        print("Gyldig passord.")
    else:
        print("Ugyldig passord.")
    
    
if __name__ == "__main__":
    main()