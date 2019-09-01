#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  2 16:34:35 2018

@author: oscargalindo
"""

import numpy as np
import pylab as plt
import cv2

def plane_sweep_ncc(im_l,im_r,min_disp, max_disp,wid):
    steps = max_disp-min_disp+1
    sum_filt = np.ones((wid,wid))
    m,n,_ = im_l.shape
    dmaps = np.zeros((m,n,steps))
    # try different disparities
    for displ in range(steps):
        x = np.roll(im_r,min_disp+displ,axis=1)-im_l
        x = x*x
        x = np.sum(x,axis=2)
        d = cv2.filter2D(x,-1,sum_filt)
        d=np.sqrt(d)
        dmaps[:,:,displ] = d
    return dmaps
    
plt.close(0)
plt.close(1)

im_l = cv2.imread('i0_l.jpg',1).astype(np.float32)
im_r = cv2.imread('i0_r.jpg',1).astype(np.float32)
cv2.imshow('left',im_l/255)
cv2.imshow('right',im_r/255)

min_disp = 10
max_disp = 100
wid = 7
disp_map = plane_sweep_ncc(im_l,im_r,min_disp, max_disp, wid)
plt.figure(0)
# Plot some pixels' differences with respect to depth
plt.plot(disp_map[50,450,:])
plt.plot(disp_map[50,451,:])
plt.show()
plt.figure(1)
plt.plot(disp_map[400,450,:])
plt.plot(disp_map[400,451,:])
plt.show()

disp =np.argmin(disp_map,axis=2)+min_disp

salience = 1 - np.min(disp_map, axis=2)/np.mean(disp_map, axis=2)
disp = disp/np.max(disp)
cv2.imshow('disparity',disp)
cv2.imshow('salience',salience)






