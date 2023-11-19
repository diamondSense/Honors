import cv2

cascade_face = cv2.CascadeClassifier('Face Detection\haarcascade_frontalface_default.xml')


cap = cv2.VideoCapture(0)

while True:
    ret, img = cap.read() 
    print(ret)
    g = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    f = cascade_face.detectMultiScale(g, 1.3, 4)

    for (x, y , w, h) in f :
        cv2.rectangle(img, (x,y), (x + w, y + h), (0,255,0),4 )

    cv2.imshow('img', img)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()