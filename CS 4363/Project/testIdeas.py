#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 16 17:38:31 2018

@author: oscargalindo
"""
import numpy as np
import cv2


def convolve (I):
    blurred = np.zeros((I.shape[0]-2, I.shape[1]-2, 3))
        for x in range (blurred.shape[0]):
            for y in range(blurred.shape[1]):
                blurred[x,y,z] = np.sum(I[x:x+3, y:y+3,:])/9
    return blurred.astype(np.uint8)

face_cascade = cv2.CascadeClassifier('/anaconda3/share/OpenCV/haarcascades/haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('/anaconda3/share/OpenCV/haarcascades/haarcascade_eye.xml')
img = cv2.imread('IMG_5838.JPG')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray, 1.2, 5)

for (x,y,w,h) in faces:
    I = img[y+2:y+h-2, x+2:x+w-2] #Change the order to get the actual face Sliced.
#    cv2.rectangle(img,(x,y),(x+w,y+h),(0,215,255),2)
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = img[y:y+10, x:x+10]

cv2.imshow('Original Image',img)


image_number = 1
for (x,y,w,h) in faces:
    face  =  img[y+2:y+h-2,x+2:x+w-2,:]
    cv2.imshow(f'Face{image_number}', face)
    rows = img.shape[0]
    cols = img.shape[1]   
#    S, count, sum_pixels = initialize(img)
#    connect_face_region(x,y,h,w,img)
#    if x+w < I.shape[1] and y+h < I.shape[0]:
#    connect_face_region(x,y+h,h,w,img)
    cv2.imshow('Image body', img[y+h:y+h+face.shape[0], x:x+w,:])
    blurred = convolve(img)
    cv2.imshow('Blurred',blurred)
#    thr = calculate_threshold(img[y+h:img.shape[0], x:x+w,:])
#    thr = calculate_threshold(img[y:y+h, x:x+w,:])
#    thr = thr * 2
#    print(thr)
#    connected_components_segmentation(img,thr)
#    print("Maximum number of pixels together",np.max(count))
    
#    print('Regions found: ',np.sum(S==-1))
#    print('Size 1 regions found: ',np.sum(count==1))
    
#    rand_cm = np.random.random_sample((rows*cols, 3))
#    seg_im_mean = np.zeros((rows,cols,3)) 
#    seg_im_rand = np.zeros((rows,cols,3))
#    for r in range(rows-1):
#        for c in range(cols-1):
#            f = find(r*cols+c)
#            seg_im_mean[r,c,:] = sum_pixels[f,:]/count[f]
#            seg_im_rand[r,c,:] = rand_cm[f,:]
                
#    cv2.imshow('Segmentation 1 - using mean colors',seg_im_mean)
#    cv2.imshow('Segmentation 2 - using random colors',seg_im_rand)
    image_number += 1
cv2.waitKey(0)
cv2.destroyAllWindows()  