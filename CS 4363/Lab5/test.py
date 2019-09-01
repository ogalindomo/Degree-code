#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 25 10:06:11 2018

@author: oscargalindo
"""

'''Problem 2'''
# Segmantation based on connected components 
# Programmed by Olac Fuentes
# Last modified November 19, 2018

import numpy as np
import cv2 as cv2
#import pylab as plt
#import time
#import random

def find(i):
    if S[i] <0:
        return i
    s = find(S[i]) 
    S[i] = s #Path compression
    return s

def union(i,j,thr):
    # Joins two regions if they are similar
    # Keeps track of size and mean color of regions
    ri =find(i)
    rj = find(j)
    if (ri!= rj):
        d =  sum_pixels[ri,:]/count[ri] - sum_pixels[rj,:]/count[rj]
        diff = np.sqrt(np.sum(d*d))
        if diff < thr:	
            S[rj] = ri
            count[ri]+=count[rj]
            count[rj]=0
            sum_pixels[ri,:]+=sum_pixels[rj,:]
            sum_pixels[rj,:]=0
                  
def initialize(I):
    rows = I.shape[0]
    cols = I.shape[1]   
    S = np.zeros(rows*cols).astype(np.int)-1
    count = np.ones(rows*cols).astype(np.int)       
    sum_pixels = np.copy(I).reshape(rows*cols,3)      
    return S, count, sum_pixels         

def connected_components_segmentation(I,thr):
    rows = I.shape[0]
    cols = I.shape[1]   
    for p in range(S.shape[0]):
        if p%cols < cols-1:  # If p is not in the last column
            union(p,p+1,thr) # p+1 is the pixel to the right of p 
        if p%cols < cols-1 and p//cols < rows -1:
            union(p,p+cols+1, thr)
        if p//cols < rows-1: # If p is not in the last row   
            union(p,p+cols,thr) # p+cols is the pixel to below p
            
def calc_thr (I):
    blue_std = np.std(I[:,:,0])
    green_std = np.std(I[:,:,1])
    red_std = np.std(I[:,:,2])
    std_mean = (blue_std+green_std+red_std)/3
    median = np.median([blue_std, green_std, red_std])
    return np.mean([std_mean, median])

def calc_thr_weighted(I):
    std = np.array([np.std(I[:,:,0]), np.std(I[:,:,1]), np.std(I[:,:,2])])
    sort = np.sort(std)
    weighted_thr = ((sort[2] * 2)/3) + (1/6) * (sort[1]+sort[0])
    return weighted_thr
    
            
def join_single_regions(S,count,sum_pixels):
    non_one_regions = np.sum(count == 1)
    print('Single pixel regions', non_one_regions)
    print('Total regions', np.sum(S == -1))
            

I  =  (cv2.imread('171027-eiffel-tower-photography-illegal-at-night-feature.jpg',1)/255).astype(np.float64)
thr = calc_thr_weighted(I)
print('Calculated Threshold', calc_thr(I))
print('Calculated Weighted', calc_thr_weighted(I))
combined_channels = np.concatenate((I[:,:,2], I[:,:,1], I[:,:,0]), axis=1)
cv2.imshow('Image Channels', combined_channels)


rows = I.shape[0]
cols = I.shape[1]   
S, count, sum_pixels = initialize(I)
connected_components_segmentation(I,thr)

print('Regions found: ',np.sum(S==-1))
print('Size 1 regions found: ',np.sum(count==1))

rand_cm = np.random.random_sample((rows*cols, 3))
seg_im_mean = np.zeros((rows,cols,3))
seg_im_rand = np.zeros((rows,cols,3))
for r in range(rows-1):
    for c in range(cols-1):
        f = find(r*cols+c)
        seg_im_mean[r,c,:] = sum_pixels[f,:]/count[f]
        seg_im_rand[r,c,:] = rand_cm[f,:]
                    
print('Standard Deviation Channel Blue', np.std(I[:,:,0]))
print('Standard Deviation Channel Green', np.std(I[:,:,1]))
print('Standard Deviation Channel Red', np.std(I[:,:,2]))

combined = np.concatenate((I,seg_im_mean, seg_im_rand), axis=1)
cv2.imwrite('r.png', combined*255)