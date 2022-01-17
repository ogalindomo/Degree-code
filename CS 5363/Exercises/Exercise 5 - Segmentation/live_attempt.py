#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 15 18:33:20 2021

@author: oscargalindo
"""

import matplotlib.pyplot as plt
import numpy as np
from skimage.data import astronaut
from skimage.color import rgb2gray
from skimage.filters import sobel
from skimage.segmentation import felzenszwalb, slic, quickshift, watershed, active_contour
from skimage.segmentation import mark_boundaries
from skimage.util import img_as_float
from skimage.filters import gaussian
import time 
import cv2
import time
import matplotlib.pyplot as plt

def mean_region_colors(img,seg):
    cmap = np.zeros((np.amax(seg)+1,3),dtype=np.float32)
    for i in range(cmap.shape[0]):
        m = img[seg==i]
        if len(m)>0:
            cmap[i] = np.mean(m,axis=0)
    return cmap

def indexed_to_rgb(seg,cmap=[]):
    if len(cmap)==0:
        cmap = np.random.random((np.amax(seg)+1,3))
    rows,cols = seg.shape
    img=np.zeros((rows,cols,3),dtype=np.float32)
    for r in range(rows):
        for c in range(cols):
            img[r,c] = cmap[seg[r,c]]
    return img

def show_images(images,titles=None,fig_title='',save_im=True,filename=None):
    if titles==None:
        titles = ['' for i in range(len(images))]
    # Display image in new window
    fig, ax = plt.subplots(1,len(images),figsize=(12, 4))
    fig.suptitle(fig_title)
    for i in range(len(images)):
        ax[i].imshow(images[i],cmap='gray')
        ax[i].axis('off')
        ax[i].set_title(titles[i])
    if save_im:
        if filename==None:
            filename='show_images'
        fig.savefig(filename+'.jpg',bbox_inches='tight', pad_inches=0.1,dpi=200)
        plt.show()
    fig.savefig(fig_title+".jpg")
    return fig, ax

if __name__=="__main__":
    print("Hello Started ")
    cap = cv2.VideoCapture(0)
    cap.set(3,640)
    cap.set(4,480)
    start = time.time()
    count=0
    while(True):
        ret, frame = cap.read()
        count+=1
        segments = felzenszwalb(frame, scale=120, sigma=15, min_size=50)
        val = segments[240,320]
        g = (gaussian(frame,sigma=15,multichannel=True)).astype(np.float32)
        g[segments==val,:] = (frame[segments==val,:]/255).astype(np.float32)
        print(f"Center cluster value: {val} for the center pixel.")
        cv2.imshow('Blurr',g)
        print(f"Frame {count}")
        if cv2.waitKey(1) & 0xFF == ord('q'):
            print("Exited")
            break
    elapsed_time = time.time()-start
    print('Capture speed: {:.2f} frames per second'.format(count/elapsed_time))
    cap.release()
    # cv2.destroyAllWindows()

        
    
    