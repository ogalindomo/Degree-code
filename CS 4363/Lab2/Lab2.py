#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import cv2 
import numpy as np
#import matplotlib.pyplot as plt
#import math
#from scipy import interpolate
"""
Created on Sat Sep 22 14:35:42 2018

@author: oscargalindo
"""
image1 = cv2.imread('cat.jpg',-1)
image2 = cv2.imread('cheetah.jpg',-1)
image3 = cv2.imread('city.jpg',-1)
image4 = cv2.imread('deer.jpg',-1)
image5 = cv2.imread('dog.jpg',-1)
image6 = cv2.imread('husky.jpg',-1)
image7 = cv2.imread('leopard.jpg',-1)
image8 = cv2.imread('ny.jpg',-1)
image9 = cv2.imread('rose.jpg',-1)   
image10 = cv2.imread('tricycle.jpg',-1)
dst = cv2.imread('futbol.png',-1)
#Problem 1 Filters

def cat(img):#Equalizes the Histogram
    global dst
    dst = np.copy(img)
    dst[:,:,0] = cv2.equalizeHist(dst[:,:,0])
    dst[:,:,1] = cv2.equalizeHist(dst[:,:,1])
    dst[:,:,2] = cv2.equalizeHist(dst[:,:,2])
    join = np.concatenate((dst,img),axis=1)
    cv2.imshow('Cat', join)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
def cheetah(img): #Sharpens the image
    global dst
#    f = np.array([[0,0,0],[0,2,0],[0,0,0]],np.float32)
#    r = np.ones((3,3),np.float32)/8
#    f = f - r
    dst = np.copy(img)
    dst[:,:,0] = cv2.equalizeHist(dst[:,:,0])
    dst[:,:,1] = cv2.equalizeHist(dst[:,:,1])
    dst[:,:,2] = cv2.equalizeHist(dst[:,:,2])
    #dst = cv2.filter2D(img,-1,f)
    join = np.concatenate((dst,img),axis=1)
    cv2.imshow('Cheetah', join)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
def city(img):#Equalization of Histogram is not very productive
    #The image is better by the sharping, it makes the tones more true
    global dst
    f = np.array([[0,0,0],[0,2,0],[0,0,0]],np.float32)
    r = np.ones((3,3),np.float32)/8
    f = f - r   
    dst = cv2.filter2D(img,-1,f)
#    dst[:,:,0] = cv2.equalizeHist(dst[:,:,0])
#    dst[:,:,1] = cv2.equalizeHist(dst[:,:,1])
#    dst[:,:,2] = cv2.equalizeHist(dst[:,:,2])
    join = np.concatenate((dst,img),axis=1)
    cv2.imshow('City', join)
    cv2.waitKey(0)
    cv2.destroyAllWindows()    
    
def deer(img):
    global dst
    f = np.array([[0,0,0],[1,2,-1],[0,0,0]],np.float32)
    r = np.ones((3,3),np.float32)/8
    f = f - r
    dst = cv2.filter2D(img,-1,f)
#    dst[:,:,0] = cv2.equalizeHist(dst[:,:,0])
#    dst[:,:,1] = cv2.equalizeHist(dst[:,:,1])
#    dst[:,:,2] = cv2.equalizeHist(dst[:,:,2])
    join = np.concatenate((dst,img),axis=1)
    cv2.imshow('Deer', join)
    cv2.waitKey(0)
    cv2.destroyAllWindows()   
    
def dog(img):
    global dst
    f = np.array([[0,0,0],[0,2,0],[0,0,0]],np.float32)
    r = np.ones((3,3),np.float32)/15
    f = f - r   
    dst = cv2.filter2D(img,-1,f)
    join = np.concatenate((dst,img),axis=1)
    cv2.imshow('Dog', join)
    cv2.waitKey(0)
    cv2.destroyAllWindows() 
    
def husky(img):
    global dst
    dst = np.copy(img)
    dst[:,:,0] = cv2.equalizeHist(dst[:,:,0])
    dst[:,:,1] = cv2.equalizeHist(dst[:,:,1])
    dst[:,:,2] = cv2.equalizeHist(dst[:,:,2])
    join = np.concatenate((dst,img),axis=1)
    cv2.imshow('Husky', join)
    cv2.waitKey(0)
    cv2.destroyAllWindows() 
    
def leopard(img):
    global dst
    f = np.array([[0,0,0],[0,2,0],[0,0,0]],np.float32)
    r = np.ones((3,3),np.float32)/25
    f = f-r
    dst = cv2.filter2D(img,-1,f)
    join = np.concatenate((dst,img),axis=1)
    cv2.imshow('Leopard', join)
    cv2.waitKey(0)
    cv2.destroyAllWindows() 
    
def ny(img):
    global dst
    dst = np.copy(img)
    dst[:,:,0] = cv2.equalizeHist(dst[:,:,0])
    dst[:,:,1] = cv2.equalizeHist(dst[:,:,1])
    dst[:,:,2] = cv2.equalizeHist(dst[:,:,2])
    join = np.concatenate((dst,img),axis=1)
    cv2.imshow('NY', join)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
def rose(img):
    global dst
    r = np.ones((5,5),np.float32)/25
    dst = cv2.filter2D(img,-1,r)
    join = np.concatenate((dst,img),axis=1)
    cv2.imshow('Rose', join)
    cv2.waitKey(0)
    cv2.destroyAllWindows() 
    
def tricycle(img):
    global dst
    r = np.ones((7,7),np.float32)/49
    dst = np.copy(img)
    dst[:,:,0] = cv2.equalizeHist(dst[:,:,0])
    dst[:,:,1] = cv2.equalizeHist(dst[:,:,1])
    dst[:,:,2] = cv2.equalizeHist(dst[:,:,2])
    dst = cv2.filter2D(dst,-1,r)
    join = np.concatenate((dst,img),axis=1)
    cv2.imshow('Tricycle', join)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    

def coordinate (x1,y1,x2,y2,increment):
    return y1 + (increment)((y2-y1)/(x2-x1))


def interpolateBig(img, factor):
    res = cv2.resize(img,None, fx=factor, fy=factor, interpolation = cv2.INTER_LINEAR)
    cv2.imshow('Bigger Image', res)
    cv2.waitKey(0)
    cv2.destroyAllWindows() 
    
    
def averagingSmall(img,factor):
    res = cv2.resize(img,None, fx=factor, fy=factor, interpolation = cv2.INTER_LINEAR)
    cv2.imshow('Smaller Image', res)
    cv2.waitKey(0)
    cv2.destroyAllWindows() 
    
    x =0
    y = 0
    newframe = [np.size(img,0)*factor,np.size(img,1)*factor, 3]
    increment = np.size(newframe,0)/np.size(img,0)
    oldSizex = np.size(img,0)
    oldSizey = np.size(img,1)
    for x in range (0, oldSizey):
        for y in range(0, oldSizex):
            newframe[y*factor,x*factor,3] = img[y,x,3]
            y+=1
        x+=1   
    res = newframe    
cat(image1)
#cheetah(image2)
#city(image3)
#deer(image4)
#dog(image5)
#husky(image6)
#leopard(image7)
#ny(image8)
#rose(image9)
#tricycle(image10)
#averagingSmall(image1,0.5)
#interpolateBig(image1,2)
    
    
#Exercise Transitioning Images
#x=0
#for x in range(0,101):q
#    accumulation = (((((100-x)/100) *image1) + ((x)/100 * image2a))).astype(np.uint8)
#    cv2.imshow('image',accumulation)q
#    if cv2.waitKey(1) & 0xFF == ord('q'):
#       break
    
#bigger = averagingSmall(image1)
#smaller = interpolateBig(image1)

    
    

    