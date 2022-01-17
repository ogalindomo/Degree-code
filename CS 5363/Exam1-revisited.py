#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  9 16:44:20 2021

@author: oscargalindo
"""
import numpy as np
import matplolib.pyplot as plt
from skimage.segmentation import felzenszwalb, slic, quickshift, watershed, active_contour


def brightest_region(image,reg_rows,reg_cols):
    if len(image.shape) > 2:
        sum_img = np.zeros((image.shape[0]+1,image.shape[1]+1,image.shape[2]))
        result = np.zeros((image.shape[0],image.shape[1],image.shape[2]))
    else: 
        sum_img = np.zeros((image.shape[0]+1,image.shape[1]+1))
        result = np.zeros((image.shape[0],image.shape[1]))
    sum_img[1:,1:] = image
    sum_img = np.cumsum(np.cumsum(sum_img,axis=1),axis=0)
    result = sum_img[:image.shape[0]-reg_rows+1,:image.shape[1]-reg_cols+1]+sum_img[reg_rows:,reg_cols:]- sum_img[reg_rows:,:image.shape[1]-reg_cols+1] - sum_img[:image.shape[0]-reg_rows+1,reg_cols:]
    if len(result.shape) > 2: result = np.mean(result,axis=2)  
    y,x = np.unravel_index(np.argmax(result, axis=None), result.shape)
    print(x,y)
    x = [x,x,x+reg_cols,x+reg_cols,x]
    y = [y,y+reg_rows,y+reg_rows,y,y]
    return x,y,result

def make_box(x, y, dx, dy):
    # Returns coordinates of box given upper left corner (x,y) and sizes (dx, dy)
    # Notice x corresponds to image columns and y to image rows
    xs = x + np.array([0,1,1,0,0])*dx - 0.5
    ys = y + np.array([0,0,1,1,0])*dy - 0.5
    return xs,ys


def problem1(img):
    x,y,_ = brightest_region(2*img[:,:,0] - (img[:,:,1]+img[:,:,2]), 150, 150)
    box_x,box_y = make_box(x, y, 150, 150)
    plt.figure()
    plt.imshow(img)
    plt.plot(box_x,box_y)
    
def problem2(img):
    labels = felzenszwalb(img,scale=1,sigma=0.9,min_size=int(img.shape[0]*img.shape[1]*0.25), multichannel=True) 
    plt.imshow(labels)
    return np.amax(labels)

    #build dsf
    #graph -> vector
    # count -1 
    # return count -1
    
def problem3():
    
    