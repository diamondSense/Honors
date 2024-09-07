import cv2

import clx.xms
import requests

client = clx.xms.Client(service_plan_id= 'service ID',
                        token= 'token ID')


create = clx.xms.api.MtBatchTextSmsCreate()
create.sender = 'sender no'
create.recipients = {'your phone number'}
create.body = 'ALERT: Someone has approched your device'

detector = cv2.CascadeClassifier('Face Detection\haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

# We want to send SMS just once not until the face is there in the frame
count = 0

while True:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = detector.detectMultiScale(gray, 1.1,4)

    for face in faces:
        x,y,w,h = face
        # If their is any face and counter is zero then only it will send notification
        if (face.any() and count ==0):
                try:
                    batch = client.create_batch(create)
                except(requests.exceptions.RequestException, clx.xms.exceptions.ApiException) as ex:
                    print('Failed to communicate with XMS: %s' % str(ex))
                # sms ends here
        cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0,),2)
    
    cv2.imshow('Face', img)
    count = 1

    key = cv2.waitKey(1)
    if key == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()



