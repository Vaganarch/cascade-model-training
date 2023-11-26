# Importing OpenCV package 
import cv2 
import os
  
# Reading the image 
#img = cv2.imread('Photos/img(2).jpg') 
  
# Converting image to grayscale 
#gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
  
# Loading the required haar-cascade xml classifier file 
haar_cascade = cv2.CascadeClassifier('cascade.xml') 
  
# Applying the face detection method on the grayscale image 
#faces_rect = haar_cascade.detectMultiScale(gray_img, 1.1, 9) 
  
# Iterating through rectangles of detected faces 
#for (x, y, w, h) in faces_rect: 
    #cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2) 
  
#cv2.imshow('Detected faces', img) 
  
#cv2.waitKey(0) 
n = 0
for i in os.listdir("D:\opencv_training\classes_pins_dataset"):
    print(i)
    # Reading the image 
    img = cv2.imread('classes_pins_dataset/' + i) 
  
    # Converting image to grayscale 
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 

    # Applying the face detection method on the grayscale image 
    faces_rect = haar_cascade.detectMultiScale(gray_img, 1.1, 9) 
    if len(faces_rect) != 0:
        print(faces_rect)
        n+=1
print(n)
