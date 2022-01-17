#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 20 20:59:11 2021

@author: oscargalindo
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from skimage import transform as tf
from matplotlib import transforms
from scipy import signal
import cv2
import os

def warp(img,src,dst,shape = None):
    H = tf.ProjectiveTransform()
    H.estimate(src,dst)
    result = None
    if not shape:
        result = tf.warp(img, H.inverse)
    else:
        result = tf.warp(img, H.inverse,output_shape=shape)
    return result,H 

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
    dist = np.array([m.distance for m in matches])
    ind1 = np.array([m.queryIdx for m in matches])
    ind2 = np.array([m.trainIdx for m in matches])
    keypoints1 = np.array([p.pt for p in keypoints1])
    keypoints2 = np.array([p.pt for p in keypoints2])
    keypoints1 = keypoints1[ind1]
    keypoints2 = keypoints2[ind2]
    # keypoints1[i] and keypoints2[i] are a match

    print('Original number of matches',keypoints1.shape[0])
    keypoints1, keypoints2 = select_matches_ransac(keypoints1, keypoints2)
    print('Number of matches after performing RANSAC',keypoints1.shape[0])
    return keypoints1,keypoints2

if __name__=="__main__":
    img1 = mpimg.imread('WF01.jpg')
    img2 = mpimg.imread('WF02.jpg')
    img3 = mpimg.imread('WF03.jpg')
    img_p,img2_p = get_points(img1, img2)
    offset = max(img1.shape[0],img1.shape[1])
    offset2 = max(img2.shape[0],img2.shape[1])
    offset = max(offset,offset2)
    space = np.zeros((offset*2+img2.shape[0],offset*2+img2.shape[1],3)).astype(np.float32)
    space2 = np.zeros((offset*2+img2.shape[0],offset*2+img2.shape[1],3)).astype(np.float32)
    space[offset:offset+img1.shape[0],offset:offset+img1.shape[1],:] = img1
    space2[offset:offset+img2.shape[0],offset:offset+img2.shape[1],:] = img2
    img_p += offset
    img2_p += offset
    dst_avg = (img_p+img2_p)/2
    ##################################
    
    #Apply Homography and calculate limits of resulting image
    result1,H1 = warp(space,img_p,dst_avg)
    plt.imshow(result1.astype(np.uint8))
    plt.show()
    result,H2 = warp(space2,img2_p,dst_avg)
    plt.imshow(result.astype(np.uint8))
    plt.show()
    plt.imshow(np.maximum(result1,result).astype(np.uint8))
    coords = tf.warp_coords(H1, space.shape[:-1])
    coords2 = tf.warp_coords(H2, space2.shape[:-1])
    
    corners_img_1 = np.array([
        [int(coords[0,offset,offset]),int(coords[1,offset,offset])],
        [int(coords[0,offset+img1.shape[0],offset]),int(coords[1,offset+img1.shape[0],offset])],
        [int(coords[0,offset,offset+img1.shape[1]]),int(coords[1,offset,offset+img1.shape[1]])],
        [int(coords[0,offset+img1.shape[0],offset+img1.shape[1]]),int(coords[1,offset+img1.shape[0],offset+img1.shape[1]])]
        ])
    print(corners_img_1)
    corners_img_2 = np.array([
        [int(coords2[0,offset,offset]),int(coords2[1,offset,offset])],
        [int(coords2[0,offset+img2.shape[0],offset]),int(coords2[1,offset+img2.shape[0],offset])],
        [int(coords2[0,offset,offset+img2.shape[1]]),int(coords2[1,offset,offset+img2.shape[1]])],
        [int(coords2[0,offset+img2.shape[0],offset+img2.shape[1]]),int(coords2[1,offset+img2.shape[0],offset+img2.shape[1]])]
        ])
    print(corners_img_2)
    
    min_r = min(min(corners_img_1[:,0])-1,min(corners_img_2[:,0])-1)
    max_r =max(max(corners_img_1[:,0])+1,max(corners_img_2[:,0])+1)
    min_c = min(min(corners_img_1[:,1])-1,min(corners_img_2[:,1])-1)
    max_c =max(max(corners_img_1[:,1])+1,max(corners_img_2[:,1])+1)
    print(min_r,max_r)
    print(min_c,max_c)
    
    result = np.maximum(result1,result).astype(np.uint8)
    first_stitch = result[min_r:max_r,min_c:max_c]
    plt.imshow(first_stitch)
    plt.show()