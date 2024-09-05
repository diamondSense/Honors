import cv2 
import numpy as np 
import pyautogui 

low_green = np.array([25, 52, 72]) 
high_green = np.array([102, 255, 255]) 
cap = cv2.VideoCapture(0) 
prev_y = 0

while True:                                                                    
    ret, frame = cap.read() 
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) 
    mask = cv2.inRange(hsv, low_green, high_green) 
    contours, hierarchy = cv2.findContours( 
        mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) 
    
    for i in contours: 
        area = cv2.contourArea(i) 
        if area > 1000: 
            x, y, w, h = cv2.boundingRect(i) 
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2) 
            if y < prev_y: 
                pyautogui.press('space') 
            prev_y = y 
            
    cv2.imshow('frame', frame) 
    if cv2.waitKey(1) == ord('q'): 
        break

cap.release() 
cap.closeAllWindow() 