# import numpy as np
import cv2 
from random import randrange
trained_face_data = cv2.CascadeClassifier('frontface.xml')

#Choose img
# img = cv2.imread('index5.png')
webcam = cv2.VideoCapture(0)

##Loop for webcam
while True:
    # Read the current frame
    sucessfull_frame_read, frame = webcam.read()

    grayscaled_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    face_coordinates = trained_face_data.detectMultiScale(grayscaled_img)    

    for (x, y, w, h) in face_coordinates:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0,randrange(50,256),0), 2)

    cv2.imshow('AI Face Detector', frame)
    key = cv2.waitKey(1)
    
    # Ascii 81/113 = q
    if key == 81 or key == 113:
        break
webcam.release()

# cv2.waitKey(1)
#Gray scale

# #Detect faces
# face_coordinates = trained_face_data.detectMultiScale(grayscaled_img)

# #Draw rectangles around the face
# for (x, y, w, h) in face_coordinates:
#     cv2.rectangle(img, (x, y), (x+w, y+h), (0,randrange(120,256),0), 2)

# #Display the image with faces
# cv2.imshow('Clever Programmer face detector', img)
# cv2.waitKey()

