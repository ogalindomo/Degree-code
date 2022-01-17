#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 15:41:59 2021

@author: oscargalindo
"""


import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from scipy import signal

def correlate2d(image,filt):
    if len(image.shape) == 2:
        r,c = filt.shape
        result = np.zeros((image.shape[0]-r + 1, image.shape[1]-c + 1))
        for i in range(result.shape[0]):
            for j in range(result.shape[1]):
                result[i,j] = np.sum(image[i:i+r,j:j+c]*filt) # Dot product of image region and filter
        return result
    else:
        r,c = filt.shape
        result = np.zeros((image.shape[0]-r + 1, image.shape[1]-c + 1, 3))
        for i in range(result.shape[0]):
            for j in range(result.shape[1]):
                for channel in range(image.shape[2]):
                    result[i,j,channel] = np.sum(image[i:i+r,j:j+c,channel]*filt) # Dot product of image region and filter
        result = result/255
        return result.astype(np.float32)

def correlate2d_scipy(image,filt):
    if len(image.shape) == 2:
        return signal.correlate2d(image, filt,mode='valid')
    else:
        r,c = filt.shape
        img = np.zeros((image.shape[0]-r + 1, image.shape[1]-c + 1, 3))
        for channel in range(image.shape[2]):
            img[...,channel] = signal.correlate2d(image[...,channel], filt,mode='valid')
        return (img/255).astype(np.float32)

def histogram_gradients(img):
    filt = np.array([[-1,0,1],[-2,0,2],[-1,0,1]])
    b_w = np.average(img,axis=2)
    g_v = correlate2d_scipy(b_w, filt)
    g_h = correlate2d_scipy(b_w, filt.T)
    g_m = np.sqrt((np.power(g_v,2)+np.power(g_h,2)))
    return g_m
    
    
    
    
if __name__ == "__main__":
    img = mpimg.imread('/Users/oscargalindo/Downloads/2012-05-021.jpg')
    g_m = histogram_gradients(img).astype(np.float32)
    plt.figure()
    plt.imshow(g_m)
    plt.show()
    