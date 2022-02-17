# -*- coding: utf-8 -*-
"""
Created on Tue Sep  7 10:52:49 2021

@author: Lars Holen

"""


# %% Importerer pakker jeg trenger:
    
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import cv2
from cvzone.HandTrackingModule import HandDetector


# %% Oppgave Del a)

def main():
    print("Main running")
    cap = cv2.VideoCapture(0)
    cap.set(3,1280)
    cap.set(4,720)
    
    while True:
        success, img = cap.read()
        cv2.imshow("Image", img)
        cv2.waitKey(1)
        


# %% Oppgave Del a)

#if __name__ == "__main__":
#    main()


cap = cv2.VideoCapture(0)
cap.set(3,1280)
cap.set(4,720)
detector = HandDetector(detectionCon=0.8, maxHands=2)    

while True:
    
    success, img = cap.read()
    hands, img = detector.findHands(img) # draws to image
    hands = detector.findHands(img, draw=False)
    cv2.imshow("Image", img)
    cv2.waitKey(1)
    
    if hands:
        hand1 = hands[0] 
        lmList1 = hand1["lmList"] # List of 21 landmark points
        bbox1 = hand1["bbox"] # Bounding box info x,y,w,h
        centerPoint1 = hand1["center"] # center of hand, cx,cy
        handType1 = hand1["type"] # Left or Right
        
        fingers = detector.fingersUp(hand1) # return list of fingers 0 down 1 up
        
        length, info, img = detector.findDistance(lmList1[0], lmList1[1], img) # Draw lines
        length, info = detector.findDistance(lmList1[0], lmList1[1]) # no draw
        
        