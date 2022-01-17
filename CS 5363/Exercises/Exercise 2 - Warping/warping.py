#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 13:29:08 2021

@author: oscargalindo
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

img = mpimg.imread('/Users/oscargalindo/Desktop/Research/Ultrasound C-SCAN/Session_4/U4_6.jpg')
img = img/np.amax(img)

plt.figure()
plt.imshow(img[:,:,0])

def distance(p1,p2):
    return np.sqrt(np.power(p1[0]-p2[0],2)+np.power(p1[1]-p2[1],2))

T = np.zeros((img.shape[0],img.shape[1],img.shape[2]))
x_1, y_1 = 63,65
x_0, y_0 = 17,23
x_2, y_2 = 0,0
x_3, y_3 = 0, 350
k = 35.0
for k in np.linspace(1,150,5):
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            dx = np.exp(-1*distance((x_1,y_1),(i,j))/k) * (x_0-x_1)
            dy = np.exp(-1*distance((x_1,y_1),(i,j))/k) * (y_0-y_1)
            dx += np.exp(-1*distance((x_3,y_3),(i,j))/k) * (x_2-x_3)
            dy += np.exp(-1*distance((x_3,y_3),(i,j))/k) * (y_2-y_3)
            T[i,j] = img[(i+dx).astype(int),(j+dy).astype(int)]
    plt.figure()
    plt.imshow(T)
        