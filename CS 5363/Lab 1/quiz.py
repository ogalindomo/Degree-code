#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 15:30:28 2021

@author: oscargalindo
"""

import numpy as np
import matplotlib.pyplot as plt
import os
import matplotlib.image as mpimg

image = mpimg.imread('/Users/oscargalindo/Documents/Desktop Images/IMG_0029.jpg')

def show_image(image,title='',save_im=True,filename=None):
    # Display image in new window
    fig, ax = plt.subplots()
    ax.imshow(image,cmap='gray')
    ax.axis('off')
    ax.set_title(title)
    if save_im:
        if filename==None:
            filename=title
        fig.savefig(filename+'.png',bbox_inches='tight', pad_inches=0.1,dpi=200)
    return fig, ax

def subsize(img,r0,c0,rows,cols):
    return img[r0:r0+rows,c0:c0+cols]

def zeroout(img,c):
    im = np.zeros((img.shape)).astype(type(img))
    im[:,:,c] = img[:,:,c]
    return im

def brightest(img):
    return np.unravel_index(np.argmax(np.mean(img,axis=2)), img.shape[:-1])

if __name__=="__main__":
    image = mpimg.imread('/Users/oscargalindo/Documents/Desktop Images/IMG_0029.jpg')
    a = subsize(image,0,0,1000,1000)
    a = zeroout(image, 0)
    coor = brightest(image)
    show_image(a,save_im=False)