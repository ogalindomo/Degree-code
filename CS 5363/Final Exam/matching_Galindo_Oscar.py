#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 10 13:08:44 2021

@author: oscargalindo
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

def display_control_lines(im0,im1,pts0,pts1,clr_str = 'rgbycmwk'):
    canvas_shape = (max(im0.shape[0],im1.shape[0]),im0.shape[1]+im1.shape[1],3)
    canvas = np.zeros(canvas_shape,dtype=type(im0[0,0,0]))
    canvas[:im0.shape[0],:im0.shape[1]] = im0
    canvas[:im1.shape[0],im0.shape[1]:canvas.shape[1]]= im1
    fig, ax = plt.subplots(figsize=(8, 4))
    ax.imshow(canvas)
    ax.axis('off')
    pts2 = pts1+np.array([im0.shape[1],0])
    for i in range(pts0.shape[0]):
        ax.plot([pts0[i,0],pts2[i,0]],[pts0[i,1],pts2[i,1]],color=clr_str[i%len(clr_str)],linewidth=1.0)
    fig.suptitle('Point correpondences', fontsize=16)
    
def select_matches_ransac(pts0, pts1):
    H, mask = cv2.findHomography(pts0.reshape(-1,1,2), pts1.reshape(-1,1,2), cv2.RANSAC,5.0)
    choice = np.where(mask.reshape(-1) ==1)[0]
    return pts0[choice], pts1[choice]

def get_points(img1,img2):
    orb = cv2.ORB_create()

    # fig, ax = plt.subplots(ncols=2)
    keypoints1, descriptors1 = orb.detectAndCompute(img1,mask=None)
    # ax[0].imshow(cv2.drawKeypoints(img1, keypoints1, None, color=(0,255,0), flags=0))

    keypoints2, descriptors2 = orb.detectAndCompute(img2,mask=None)
    # ax[1].imshow(cv2.drawKeypoints(img2, keypoints2, None, color=(0,255,0), flags=0))

    # Create BFMatcher object
    matcher = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
    matches = matcher.match(descriptors1,descriptors2)

    # Extract data from orb objects and matcher
    ind1 = np.array([m.queryIdx for m in matches])
    ind2 = np.array([m.trainIdx for m in matches])
    keypoints1 = np.array([p.pt for p in keypoints1])
    keypoints2 = np.array([p.pt for p in keypoints2])
    keypoints1 = keypoints1[ind1]
    keypoints2 = keypoints2[ind2]
    # keypoints1[i] and keypoints2[i] are a match
    # display_control_lines(img1,img2, keypoints1, keypoints2)

    print('Original number of matches',keypoints1.shape[0])
    keypoints1, keypoints2 = select_matches_ransac(keypoints1, keypoints2)
    # display_control_lines(img1,img2, keypoints1, keypoints2)
    print('Number of matches after performing RANSAC',keypoints1.shape[0])
    return keypoints1,keypoints2

if __name__ == "__main__":
    # An ORB feature consists of a keypoint (the coordinates of the region's center) and a descriptor (a binary vector of length 256 that characterizes the region)
    plt.close('all')

    img1 = mpimg.imread('/Users/oscargalindo/Desktop/Classes/CS 5363/Final Exam/fit_closeup2.jpg')
    img2 = mpimg.imread('/Users/oscargalindo/Desktop/Classes/CS 5363/Final Exam/fit2.jpg')

    orb = cv2.ORB_create()

    fig, ax = plt.subplots(ncols=2)
    keypoints1, descriptors1 = orb.detectAndCompute(img1,mask=None)
    ax[0].imshow(cv2.drawKeypoints(img1, keypoints1, None, color=(0,255,0), flags=0))

    keypoints2, descriptors2 = orb.detectAndCompute(img2,mask=None)
    ax[1].imshow(cv2.drawKeypoints(img2, keypoints2, None, color=(0,255,0), flags=0))

    # Create BFMatcher object
    matcher = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
    matches = matcher.match(descriptors1,descriptors2)

    # Extract data from orb objects and matcher
    dist = np.array([m.distance for m in matches])
    ind1 = np.array([m.queryIdx for m in matches])
    ind2 = np.array([m.trainIdx for m in matches])
    keypoints1 = np.array([p.pt for p in keypoints1])
    keypoints2 = np.array([p.pt for p in keypoints2])
    keypoints1 = keypoints1[ind1]
    keypoints2 = keypoints2[ind2]
    # keypoints1[i] and keypoints2[i] are a match

    keypoints1, keypoints2 = select_matches_ransac(keypoints1, keypoints2)    
    display_control_lines(img1,img2, keypoints1, keypoints2)
    min_x,max_x = np.amin(keypoints2[:,0]),np.amax(keypoints2[:,0])
    min_y,max_y = np.amin(keypoints2[:,1]),np.amax(keypoints2[:,1])
    print(f"Bounding box of points {min_x,min_y}, {max_x,max_y}")
    
