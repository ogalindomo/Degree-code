#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 21 22:51:21 2021

@author: oscargalindo
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from skimage import transform as tf
from scipy import signal

def correlate2d_scipy(image,filt):
    if len(image.shape) == 2:
        return signal.correlate2d(image, filt,mode='valid')
    else:
        r,c = filt.shape
        img = np.zeros((image.shape[0]-r + 1, image.shape[1]-c + 1, 3))
        for channel in range(image.shape[2]):
            img[...,channel] = signal.correlate2d(image[...,channel], filt,mode='valid')
        return (img/255).astype(np.float32)
    
def gaussian_filter(size, sigma):
    d = ((np.arange(size) - (size-1)/2)**2).reshape(-1,1)
    f = np.exp(-(d+d.T)/2/sigma/sigma)
    return f/np.sum(f)

def show(img,title=''):
    f,a = plt.subplots()
    f.suptitle(title)
    a.imshow(img)
    if title:
        f.savefig(title+".jpg")
    plt.show()
    
def show_multiple(images,title='',titles=[],figsize=(12,4)):
    f,a = plt.subplots(ncols=len(images),figsize=figsize)
    f.suptitle(title)
    for i in range(len(images)):
        a[i].imshow(images[i])
        if i < len(titles):
            a[i].set_title(titles[i])
    f.savefig(title+".jpg")
    plt.show()
    
def load_image(name,as_float=True):
    img = mpimg.imread(name)
    if as_float:
        return img/np.amax(img)
    else: 
        return img

def get_points(num_points):
    return np.asarray(plt.ginput(n=num_points,timeout=0))

def warp(img,src,dst,shape = None):
    H = tf.ProjectiveTransform()
    H.estimate(src,dst)
    result = None
    if not shape:
        result = tf.warp(img, H.inverse)
    else:
        result = tf.warp(img, H.inverse,output_shape=shape)
    return result,H   

def problem1():
    plt.close('all')
    #Image Loading
    img = load_image('mobile_billboard.jpg')
    img2 = load_image('utep720.jpg')
    ##############
    #Get Points
    show(img,'Original Image')
    print("Click four source points")
    src,src_2 = get_points(4),get_points(4)
    ##############
    
    #Computations
    dest2  = src
    src2 = np.array([[0, 0], [1, 0], [1, 1], [0, 1]]) * np.array([[img2.shape[1],img2.shape[0]]])
    warped,H1 = warp(img2,src2,dest2,shape=(img.shape[0],img.shape[1]))
    dest = src_2
    warped2,H2 = warp(img2,src2,dest,shape=(img.shape[0],img.shape[1]))
    warped += warped2
    mask = np.expand_dims(np.sum(warped,axis=2)==0,axis=2).astype(np.int)
    ###############
    
    # Combining masked source and warped image
    combined = warped + img*mask
    ##############
    
    #Display
    show_multiple([img*mask,warped,warped2,combined],'Problem1',
                  ['Original * mask','Destination','Destination2','Original * mask + destination'],
                  )
    show(combined,'Resulting Image')
    ##############
    
def problem2(automatic=True):
    automatic = True
    plt.close('all')
    
    #Display Images for 1st stitching
    img = load_image('WF01.jpg')
    img2 = load_image('WF02.jpg')
    show_multiple([img,img2],'Input First Stitching',['Left','Right'])
    #################################
    
    #Define Points First Stitching
    if not automatic:
        print("Click correspondences")
        src = get_points(12)
        img_p = src[::2]
        img2_p = src[1::2]
    else:
        img_p = np.array([[604.67338234, 379.29681609],
                [666.55126252, 344.34289904],
                [875.82964543, 374.10043988],
                [372.07164323, 356.73509445],
                [898.66898351, 317.52105153],
                [922.26814464, 443.32220864]])
    
        img2_p = np.array([[282.1093994 , 395.77670716],
                [344.90893857, 361.19145371],
                [545.91019538, 393.43328446],
                [ 34.77490072, 369.40850059],
                [567.27070332, 339.62639147],
                [587.22722512, 459.11012778]])
    ##################################
        
    #Change origin and reflect changes on points
    offset = max(img.shape[0],img.shape[1]) 
    space = np.zeros((offset*2,offset*2,3))
    space[offset:offset+img.shape[0],offset:offset+img.shape[1],:] = img
    img_p += offset
    img2_p += offset
    ##################################
    
    #Apply Homography and calculate limits of resulting image
    result,H1 = warp(space,img_p,img2_p)
    coords = tf.warp_coords(H1, space.shape[:-1])
    min_r = min(int(coords[0,offset,offset]),int(coords[0,offset+img.shape[0],offset]+1),offset,offset+img2.shape[0])
    max_r = max(int(coords[0,offset,offset]),int(coords[0,offset+img.shape[0],offset]+1),offset,offset+img2.shape[0])
    min_c = min(int(coords[1,offset,offset]),int(coords[1,offset+img.shape[0],offset]+1),offset,offset+img2.shape[1])
    max_c = max(int(coords[1,offset,offset]),int(coords[1,offset+img.shape[0],offset]+1),offset,offset+img2.shape[1])
    ##################################
    
    #Display results of first stitching
    r = result.copy()
    result[offset:offset+img2.shape[0],offset:offset+img2.shape[1],:] = np.maximum(img2,result[offset:offset+img2.shape[0],offset:offset+img2.shape[1],:])
    first_stitch = result[min_r:max_r,min_c:max_c]
    show_multiple([space,r,result],'First Warping',['Centered','Warped','Stitched'])
    show(first_stitch,'Results First Stitching')
    ###################################
    
    #Load and show images for second stitching
    img3 = load_image('WF03.jpg')
    show_multiple([first_stitch,img3],"Input Second Stitching",["Left","Right"])
    ###################################
    
    #Define Points Second Stitching
    if not automatic:
        print("Click correspondences")
        src = get_points(12)
        imgc_p = src[::2]
        img3_p = src[1::2]
    else:
        imgc_p = np.array([[ 974.7361245,502.30896434],
         [1186.07022588,382.99609307],
         [1249.54672906,420.65623014],
         [ 961.37444229,437.46662036],
         [1097.49030633,430.51680009],
         [1365.52645099,423.94189488]])
        
        img3_p = np.array([[135.56565561,478.24584038],
         [353.01205177,359.24339772],
         [413.66546917,396.3644444 ],
         [123.1317045,410.39270247],
         [263.8693006,404.9737237 ],
         [520.57390025,400.63621346]])
    ##################################
    
    #Change origin and reflect changes on points
    offset = max(first_stitch.shape[0],first_stitch.shape[1])
    spaced = np.zeros((offset*2,offset*2,3))
    spaced[offset:offset+first_stitch.shape[0],offset:offset+first_stitch.shape[1],:] = first_stitch
    imgc_p+=offset
    img3_p+=offset
    ##################################
    
    #Apply Homography and calculate limits of resulting image
    result,H2 = warp(spaced,imgc_p,img3_p)
    coords = tf.warp_coords(H2, spaced.shape[:-1])
    min_r = min(int(coords[0,offset,offset]),int(coords[0,offset+first_stitch.shape[0],offset]+1),offset,offset+img3.shape[0])
    max_r = max(int(coords[0,offset,offset]),int(coords[0,offset+first_stitch.shape[0],offset]+1),offset,offset+img3.shape[0])
    min_c = min(int(coords[1,offset,offset]),int(coords[1,offset+first_stitch.shape[0],offset]+1),offset,offset+img3.shape[1])
    max_c = max(int(coords[1,offset,offset]),int(coords[1,offset+first_stitch.shape[0],offset]+1),offset,offset+img3.shape[1])
    ##################################
    
    #Display results of first stitching
    r = result.copy()
    result[offset:offset+img3.shape[0],offset:offset+img3.shape[1]] = np.maximum(img3,result[offset:offset+img3.shape[0],offset:offset+img3.shape[1]])
    show_multiple([spaced,r,result],'Second Warping',['Centered','Warped','Stitched'])
    second_stitch = result[min_r:max_r,min_c:max_c,:]
    show(second_stitch,'Results Second Stitching')
    ###################################

def problem3():
    plt.close('all')
    #Display and Get Points
    baseball = load_image('soto.jpg',as_float=False)
    vll_banner = load_image('vll_utep_720.jpg',as_float=False)
    vll_banner = correlate2d_scipy(vll_banner, gaussian_filter(10, sigma=0.3))
    show(baseball)
    
    print("Click four corners of Green Area")
    src = get_points(4)
    print(src)
    #########################
    
    #Warp Banner
    cols = int(np.amax(src[:,0])-np.amin(src[:,0]))
    rows = int(np.amax(src[:,1])-np.amin(src[:,1]))
    s = np.array([[0, 0], [1, 0], [1, 1], [0, 1]]) * np.array([vll_banner.shape[1],vll_banner.shape[0]])
    dest = np.array([[0, 0], [1, 0], [1, 1], [0, 1]]) * np.array([[cols,rows]])
    
    w,H0 = warp(vll_banner,s,dest,shape=(rows,cols))
    show(w,'Warped Banner')
    ##########################
    
    #Show modified banner by mask and with color detection
    minr,minc = np.amin(src[:,1]).astype(int),np.amin(src[:,0]).astype(int)
    area = baseball[minr:minr+rows,minc:minc+cols,:]
    green_share = (area[:,:,1]/(np.sum(area, axis=2)+0.0000000001)).astype(np.float32)
    w[green_share < 0.5] = 0
    show(w)
    ##########################
    
    #Expand the banner to take all area of the image and combine with original
    src2 = np.array([[0, 0], [1, 0], [1, 1], [0, 1]]) * np.array([[w.shape[1],w.shape[0]]])
    warped2,H1 = warp(w,src2,src,shape=(baseball.shape[0],baseball.shape[1]))
    mask = np.expand_dims(np.sum(warped2,axis=2)==0,axis=2).astype(np.int)
    baseball_mod = (baseball*mask + warped2*255).astype(np.uint8)
    ##########################
    
    #Display Results
    show_multiple([baseball,area,baseball_mod],
                  'Transition',['Original','Area Selected','New Area'],
                  )
    show(baseball_mod,'Problem 3')
    ##########################

if __name__=="__main__":
    # problem1()
    problem2()
    # problem3()





