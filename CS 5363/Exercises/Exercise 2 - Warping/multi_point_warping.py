#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 14 18:07:18 2021

@author: oscargalindo
"""
#Multi-point warping

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

def distance(p0,p1):
    return np.sqrt(np.power(p0[0]-p1[0],2) + np.power(p0[1]-p1[1],2))

def loop(points):
    while True:
        p = np.asarray(plt.ginput(n=2), dtype=np.int)
        if distance(p[0],p[1]) < 5:
            break
        points.append(p)
        plt.plot(p[:,0],p[:,1],marker = '.',color='cyan')
        plt.pause(0.01)
        plt.show()
    
def compute_image(img,points,dimensions,k=150):
    Target = np.zeros((dimensions)).astype(np.uint8)
    points = np.array(points).astype(int)
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            dx = 0
            dy = 0
            for pair in range(0,len(points)):
                p0,p1 = points[pair][0],points[pair][1]
                p0 = p0.astype(int)
                p1 = p1.astype(int)
                x_0,y_0 = p0[1],p0[0]
                x_1,y_1 = p1[1],p1[0]
                dx += np.exp(-1*distance((x_1,y_1),(i,j))/k) * (x_0-x_1)
                dy += np.exp(-1*distance((x_1,y_1),(i,j))/k) * (y_0-y_1)
            Target[i,j] = img[min(max(0,(i+dx).astype(int)),img.shape[0]-1),min(max(0,(j+dy).astype(int)),img.shape[1]-1)]
    return Target
    
if __name__=="__main__":
    points = []
    plt.close()
    img = mpimg.imread('/Users/oscargalindo/Downloads/2012-05-021.jpg')
    plt.figure()
    plt.imshow(img)
    loop(points)
    T = compute_image(img,points,img.shape)
    print(points)
    plt.imshow(img)
    plt.figure()
    plt.imshow(T/255.0)
    