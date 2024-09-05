# #static_image_mode: It is used to specify whether the input images must be treated as static images or as a video stream. The default value is False.
# model_complexity: It is used to specify the complexity of the pose landmark model: 0, 1, or 2. As the model complexity of the model increases the landmark accuracy and latency increase. The default value is 1.
# smooth_landmarks: This parameter is used to reduce the jitter in the prediction by filtering pose landmarks across different input images. The default value is True.
# min_detection_confidence: It is used to specify the minimum confidence value with which the detection from the person-detection model needs to be considered as successful. Can specify a value in [0.0,1.0]. The default value is 0.5.
# min_tracking_confidence: It is used to specify the minimum confidence value with which the detection from the landmark-tracking model must be considered as successful. Can specify a value in [0.0,1.0]. The default value is 0.5.


# ----------------------------------------------------

# Code to access landmarks
# for landmark in mp_holistic.HandLandmark:
#     print(landmark, landmark.value)
# print(mp_holistic.HandLandmark.WRIST.value)

# ----------------------------------------------------

import cv2
import mediapipe as mp 
import time



# Grabbing the holistic model from mediapipe and initializing the model 
mp_holistic = mp.solutions.holistic
holistic_model = mp_holistic.Holistic(
    min_detection_confidence = 0.5,
    min_tracking_confidence = 0.5
)

# Initializing the drawing utils for drawing the facial landmarks on image
mp_drawing = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)
# initializing current time and previous time for calculating the FPS
previousTime = 0
currentTime = 0

while cap.isOpened():
    ret, frame = cap.read()
    # resizing the frame
    frame = cv2.resize(frame,(800,600))
    image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
      # Making predictions using holistic model
    # To improve performance, optionally mark the image as not writeable to
    # pass by reference.
    image.flags.writeable = False
    results = holistic_model.process(image)
    image.flags.writeable= True
    # converting back to bgr
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    # Drawing the facial landmarks 
    mp_drawing.draw_landmarks(
      image,
      results.face_landmarks,
      mp_holistic.FACEMESH_CONTOURS,
      mp_drawing.DrawingSpec(
        color=(255,0,255),
        thickness=1,
        circle_radius=1
      ),
      mp_drawing.DrawingSpec(
        color=(0,255,255),
        thickness=1,
        circle_radius=1
      )
    )
    # Drawing Right hand landmarks
    mp_drawing.draw_landmarks(
        image,
        results.right_hand_landmarks,
        mp_holistic.HAND_CONNECTIONS
    )
    # Drawing left hand land marks
    mp_drawing.draw_landmarks(
        image,
        results.left_hand_landmarks,
        mp_holistic.HAND_CONNECTIONS
    )

# calculating the fps
    currentTime = time.time()
    fps = 1/(currentTime-previousTime)
    previousTime = currentTime

# dislpaying fps on the image
    cv2.putText(image,str(int(fps))+"FPS", (10,70),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),2)
# displaying the resulting image
    cv2.imshow("Facial and Hand Landmarks", image)
    if cv2.waitKey(5) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()


