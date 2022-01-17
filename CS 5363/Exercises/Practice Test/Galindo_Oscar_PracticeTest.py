#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 15:47:46 2021

@author: oscargalindo
"""

import matplotlib.pyplot as plt
import numpy as np
from skimage.filters import gaussian
import matplotlib.image as mpimg


def gamma(img,gamma):
    img = img/np.amax(img)
    return (255*(np.power(img,(1/gamma)))).astype(np.uint8)

def problem1(img):
    plt.imshow(gamma(img,3))
    plt.imsave('dog.jpg',gamma(img,3))
    
def problem2(img):
    plt.imshow(gaussian(img,1.2))
    plt.imsave("corrected_2.jpg",gaussian(img,1.2))
    
def problem3(original,original_figure):
    result = np.zeros((original.shape))
    result = (0.7 *original + 0.3*original_figure).astype(np.uint8)
    plt.imshow(result)
    plt.imsave("ghost.jpg",result)
    
def problem5(src,target):
    shared_blue = src[:,:,2] / (np.sum(src,axis=2))
    modified_src = src.copy()
    modified_src[shared_blue > 0.4,:] = 0
    result = target.copy()
    smaller = target[:src.shape[0],:src.shape[1],:].copy()
    smaller[shared_blue <= 0.4,:] = 0
    result[:modified_src.shape[0],:modified_src.shape[1],:] = smaller
    result[:modified_src.shape[0],:modified_src.shape[1],:] += modified_src
    plt.imshow(result)
    plt.imsave("blue_background.jpg",result)
    
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
    
def problem4(img,points,dimensions,k=150):
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
    img1 = mpimg.imread('/Users/oscargalindo/Desktop/Classes/CS 5363/Exercises/Practice Test/practice exam images/q1_a.jpg')
    problem1(img1)
    # img2 = mpimg.imread('/Users/oscargalindo/Desktop/Classes/CS 5363/Exercises/Practice Test/practice exam images/q2_a.jpg')
    # problem2(img2)
    # original = mpimg.imread('/Users/oscargalindo/Desktop/Classes/CS 5363/Exercises/Practice Test/practice exam images/q3_a.jpg')
    # original_figure = mpimg.imread('/Users/oscargalindo/Desktop/Classes/CS 5363/Exercises/Practice Test/practice exam images/q3_b.jpg')
    # problem3(original,original_figure)
    # src = mpimg.imread('/Users/oscargalindo/Desktop/Classes/CS 5363/Exercises/Practice Test/practice exam images/q5_a.jpg')
    # dst = mpimg.imread('/Users/oscargalindo/Desktop/Classes/CS 5363/Exercises/Practice Test/practice exam images/q5_b.jpg')
    # problem5(src,dst)
    # points = []
    # plt.close('all')
    # img = mpimg.imread('/Users/oscargalindo/Desktop/Classes/CS 5363/Exercises/Practice Test/practice exam images/q4_a.jpg')
    # plt.figure()
    # plt.imshow(img)
    # loop(points)
    # T = problem4(img,points,img.shape)
    # print(points)
    # plt.imshow(img)
    # plt.figure()
    # plt.imshow(T/255.0)