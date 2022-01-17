#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 15:41:59 2021

@author: oscargalindo
"""

import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from scipy import signal

def display(img):
    plt.figure()
    plt.imshow(img)
    plt.show()

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
    
def color_histograms(img,display=True):
    r,_ = np.histogram(img[:,:,0], bins=255)
    g,_ = np.histogram(img[:,:,1], bins=255)
    b,_ = np.histogram(img[:,:,2], bins=255)
    if display:
        fig, ((i,r_x),(g_x,b_x)) = plt.subplots(2, 2)
        fig.suptitle('Histograms by Color')
        i.imshow(img)
        r_x.hist(img[:,:,0].reshape(img.shape[0]*img.shape[1]),bins=256,color='red')
        g_x.hist(img[:,:,1].reshape(img.shape[0]*img.shape[1]),bins=256,color='green')
        b_x.hist(img[:,:,2].reshape(img.shape[0]*img.shape[1]),bins=256,color='blue')
        fig.subplots_adjust(wspace=0.5,hspace=0.5)
        r_x.set_xlabel("Intensities")
        g_x.set_xlabel("Intensities")
        b_x.set_xlabel("Intensities")
        r_x.set_ylabel("Counts")
        g_x.set_ylabel("Counts")
        b_x.set_ylabel("Counts")
        plt.show()
    #Normalize to be able to compare
    r = r.astype(np.float32)/(img.shape[0]*img.shape[1])
    g = g.astype(np.float32)/(img.shape[0]*img.shape[1])
    b = b.astype(np.float32)/(img.shape[0]*img.shape[1])
    return r,g,b

def histogram_gradients(img):
    filt = np.array([[-1,0,1],[-2,0,2],[-1,0,1]])
    b_w = np.average(img,axis=2)
    g_v = correlate2d_scipy(b_w,filt)
    g_h = correlate2d_scipy(b_w, filt.T)
    g_m = np.sqrt((np.power(g_v,2)+np.power(g_h,2)))
    g_d = np.arctan2(g_v, g_h)
    normalized = (((g_d/np.amax(g_d))*180))
    normalized = normalized.reshape(normalized.shape[0]*normalized.shape[1])
    normalized+=180
    g_m = g_m.reshape(g_m.shape[0]*g_m.shape[1])
    hist = np.zeros(360).astype(np.float32)
    for i in range(normalized.shape[0]):
        j = min(359,int(normalized[i]))
        hist[j] += g_m[i]
    return hist

def construct_descriptor(h_r,h_g,h_b,q1_hog,q2_hog,q3_hog,q4_hog,g_d):
    return [h_r,h_g,h_b,q1_hog,q2_hog,q3_hog,q4_hog,g_d]

def compute_distance(orig_descriptor,target_descriptor):
    s = 0
    for arr in range(len(orig_descriptor)):
        s+= np.sum(np.power(orig_descriptor[arr]-target_descriptor[arr],2),axis=0)
    return np.sqrt(s)
    
if __name__ == "__main__":
    src = '/Users/oscargalindo/Desktop/Classes/CS 5363/Exercises/Exercise 3/Images/'
    descriptors = []
    images = os.listdir(src)
    for image in images:
        img = mpimg.imread(src+image)
        g_d = histogram_gradients(img).astype(np.float32)
        h_r,h_g,h_b = color_histograms(img)
        h_w,h_l = int(img.shape[0]/2),int(img.shape[1]/2)
        pixel_cout = img.shape[0]*img.shape[1]
        q1_hog = histogram_gradients(img[:h_w,:h_l])/pixel_cout
        q2_hog = histogram_gradients(img[:h_w,h_l:])/pixel_cout
        q3_hog = histogram_gradients(img[h_w:,:h_l])/pixel_cout
        q4_hog = histogram_gradients(img[h_w:,h_l:])/pixel_cout
        descriptors.append(construct_descriptor(h_r, h_g, h_b, q1_hog, q2_hog, q3_hog, q4_hog,g_d))
    for i in range(0,len(descriptors)):
        best = float("inf")
        best_j = 0
        for j in range(0,len(descriptors)):
            if j==i: continue
            d = compute_distance(descriptors[i], descriptors[j])
            if best > d:
                best = d
                best_j = j
            
        fig, (orig,target) = plt.subplots(1, 2)
        fig.suptitle(f'Best Match for {images[i]}')
        img = mpimg.imread(src+images[i])
        orig.imshow(img)
        orig.set_xlabel(images[i])
        img = mpimg.imread(src+images[best_j])
        target.imshow(img)
        target.set_xlabel(images[best_j])
            
                
    