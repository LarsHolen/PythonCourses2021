# -*- coding: utf-8 -*-
"""
Created on Mon Sep 20 22:48:48 2021

@author: Lars Holen


Grafisk visning av hvordan bouble sort fungerer.

"""




# %% imports

import pygame
import random

# %% Global variables


#List to be sorted:
counter = 0
myList = []
listLength = 200   
j = -1


myListOfRectsAndColors = [[],[]]
for c in range(listLength):
    col = (random.randint(0, 255), random.randint(0, 255),random.randint(0, 255))
    myListOfRectsAndColors[1].append(col)

 
for i in range(listLength):
    a = random.randint(0, 500)
    myList.append(a)
    

color = (255,0,0)
border = 50
clock = pygame.time.Clock()


# %% Main 

pygame.init()
(width, height) = (len(myList)*2 + border * 2, 700)
screen=pygame.display.set_mode((width, height))
pygame.display.update()

for index, item in enumerate(myList):
    myListOfRectsAndColors[0].append(pygame.Rect(index*2 + border, height - border - item, 1, item))


#%% on enter frame loop
while True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() 
            break
    screen.fill((0, 0, 0))
    for index, rects in enumerate(myListOfRectsAndColors[0]):
        pygame.draw.rect(screen, myListOfRectsAndColors[1][index] , rects)
        
        
    # insertion sort list, frame by frame
    
    
    if(counter < len(myList) and j == -1):
        value = myList[counter]  
        j = counter - 1 
    if(j >= 0 and value < myList[j]):
         myList[j + 1] = myList[j]  
         j -= 1  
         myList[j + 1] = value  
    else:
        j = -1
    
    
    
    
   
    myListOfRectsAndColors[1][counter] = (counter + 50,0,0)
    
    counter += 1
    if(counter >= len(myList)):
        counter = 0
        
    
    
    if(counter < len(myList)):
        myListOfRectsAndColors[0][counter].update(counter * 2 + border, height - border - myList[counter], 1, myList[counter])
    pygame.display.flip()
    #clock.tick(10000)
    #print(myList[counter])
    
        
  
    
    
    