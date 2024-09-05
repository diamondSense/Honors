import cv2
import numpy as np 
import Hand_Tracking_Module as htm 
import time
import autopy 




# Width and height of the camera
wCam, hCam = 640,480
frameR = 100 #Frame Reduction 
smoothening = 10

pTime = 0
plocX, plocY = 0,0
clocX, clocy = 0, 0


cap = cv2.VideoCapture(0)
cap.set(3,wCam)
cap.set(4,hCam)
detect = htm.handDetector(maxHands=1)
wScr, hScr = autopy.screen.size()
# print(wScr, hScr)
# 1536.0 864.0


while True:
    # Find hand landmarks
    success, img = cap.read()
    img = detect.findHands(img)
    lmList, bbox = detect.findPosition(img)

    # get the tip of the index and middle fingers
    if len(lmList) != 0:
        x1, y1 = lmList[8][1:]
        x2, y2 = lmList[12][1:]

    #Check which fingers are up
        fingers = detect.fingersUp()
        # print(fingers)
        cv2.rectangle(img, (frameR, frameR), (wCam - frameR,
                                              hCam - frameR),
                                              (255,0,255),2)
    # Only index finger moving mode
        if fingers[1]==1 and fingers[2]==0:
    
    # convert coordinates
            x3 = np.interp(x1, (frameR,wCam-frameR),(0,wScr))
            y3 = np.interp(y1, (frameR,hCam-frameR),(0,hScr))

    # Smoothen values
            clocX = plocX + (x3 - plocX) / smoothening
            clocy = plocY + (y3 - plocY) / smoothening
    # Move Mouse
            autopy.mouse.move(wScr - clocX, clocy)
            cv2.circle(img, (x1,y1), 15,(255,0,255), cv2.FILLED)
            plocX , plocY = clocX, clocy

    # Both index and middle fingers are up : Clicking mode
        if fingers[1]==1 and fingers[2]==1:
        # Finding the distance between the fingers
            length, img, lineInfo = detect.findDistance(8,12,img)
            print(length)
        # Clicking mouse if distance is short
            if length < 70:
                cv2.circle(img, (lineInfo[4], lineInfo[5]),
                       15, (8,255,0), cv2.FILLED)
            autopy.mouse.click()
# Frame rate
    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime
    cv2.putText(img, str(int(fps)), (20,80), cv2.FONT_HERSHEY_COMPLEX,
                3,(255,0,0),3) 

# Display
    cv2.imshow('Frame', img)
    cv2.waitKey(1)
   
