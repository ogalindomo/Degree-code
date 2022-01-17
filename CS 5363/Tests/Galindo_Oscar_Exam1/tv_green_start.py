#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 29 18:13:15 2021

@author: oscargalindo
"""

import numpy as np
import matplotlib.pyplot as plt
from skimage.segmentation import felzenszwalb, slic, quickshift, watershed, active_contour
from skimage import transform as tf
import cv2

def indexed_to_rgb(seg,cmap=[]):
    if len(cmap)==0:
        cmap = np.random.random((np.amax(seg)+1,3))
    rows,cols = seg.shape
    img=np.zeros((rows,cols,3),dtype=np.float32)
    for r in range(rows):
        for c in range(cols):
            img[r,c] = cmap[seg[r,c]]
    return img

def segment(img,sigma):
    return felzenszwalb(img, scale=10000, sigma=sigma, min_size=40000)

def get_representatives(img,segmented):
    groups = np.unique(segmented)
    representatives = []
    for identifier in groups:
        representatives.append([identifier,np.mean(img[segmented==identifier], axis = 0)])
    return representatives

def convert_to_green_scale(representatives):
    representatives_scale = []
    for p in range(len(representatives)):
        index = representatives[p][0]
        vector = representatives[p][1]
        representatives_scale.append([index,vector[1]/np.sum(vector,axis=0)])
    return representatives_scale

def find_group(representatives_scaled):
    for i in range(len(representatives_scaled)):
        if representatives_scaled[i][1] > 0.4:
            return i
    else:
        return np.argmax(representatives_scaled,representatives_scaled.shape)
    
def warp(img,src,dst,shape = None):
    H = tf.ProjectiveTransform()
    H.estimate(src,dst)
    result = None
    if not shape:
        result = tf.warp(img, H.inverse)
    else:
        result = tf.warp(img, H.inverse,output_shape=shape)
    return result,H

def calculate_change(p1,p2,approximate_val):
    m = (p1[0]-p2[0])/(p1[1]-p2[1])
    change = approximate_val*m
    return int(change)
    

if __name__=="__main__":
    img = plt.imread('/Users/oscargalindo/Desktop/Classes/CS 5363/Tests/Galindo_Oscar_Exam1/tv_greenscreen2.jpg')    
    cap = cv2.VideoCapture(0)
    cap.set(3,1280)
    cap.set(4,720)
    
    segmented = segment(img,0.55)
    s2 = segment(img,0.3)
    representatives_scaled = convert_to_green_scale(get_representatives(img, segmented))
    group = find_group(representatives_scaled)
    representatives_scaled = convert_to_green_scale(get_representatives(img, s2))
    group2 = find_group(representatives_scaled)
    v_s = np.zeros((segmented.shape))
    v_s[segmented==group] = 255
    
    a = (np.argwhere(segmented==group))
    a2 = (np.argwhere(s2==group2))
    result = img.copy()
    result[segmented==group,:] = 0
    plt.imshow(result.astype(np.uint8))
    
    change_y = calculate_change(a[0,:],a2[0,:],a[-1,0])
    upper_left_corner = [a[-1,1],-change_y+a[0,0]]
    upper_right_corner = [a[0,1],a[0,0]]
    change_y = calculate_change(a[-1,:],a2[-1,:],a[0,0])
    bottom_right_corner = [a[0,1],change_y+a[-1,0]]
    bottom_left_corner = [a[-1,1],a[-1,0]]
    plt.scatter(upper_left_corner[0],upper_left_corner[1])
    plt.scatter(upper_right_corner[0],upper_right_corner[1])
    plt.scatter(bottom_right_corner[0],bottom_right_corner[1])
    plt.scatter(bottom_left_corner[0],bottom_left_corner[1])
    
    d = np.array([upper_left_corner,upper_right_corner,
                            bottom_right_corner,bottom_left_corner]).astype(np.float64)
    
    result = result[:,:,::-1]
    print("Showing live feed on tv.")
    while True:
        ret, src = cap.read()
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        s = np.array([[0, 0], [1, 0], [1, 1], [0, 1]]) * np.array([[src.shape[1],src.shape[0]]])
        H1 = tf.ProjectiveTransform()
        H1.estimate(s, d)
        warped = tf.warp(src, H1.inverse, output_shape=(img.shape[0],img.shape[1])) *255
        warped = warped.astype(np.uint8)
        cv2.imshow("Live Feed", warped+result)
        
    cap.release()
    cv2.destroyAllWindows()
    
    
    
    
    