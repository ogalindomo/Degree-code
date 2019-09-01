#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 24 12:46:13 2018

@author: oscargalindo
"""

'''Problem 1'''
#import keras
#import os
#import cv2
#import numpy as np
#from keras.models import Sequential
#from keras.layers import Dense, Dropout, Flatten
#from keras.layers import Conv2D, MaxPooling2D
#import random
#
#
#def load_images_from_folder(folder):
#    x = 0
#    random_choice = random.sample(range(0,25000), 5000)
#    random_choice.sort()
#    data_x  = np.zeros((((25000,256,256, 3)))) #ALL DATA
#    data_y = np.zeros(25000) #0 for Cats and 1 for Dogs
#    x_train = np.zeros((((20000,256,256,3)))) #TRAINING DATA
#    y_train = np.zeros(20000)
#    x_test = np.zeros((((5000,256,256,3)))) #TESTING DATA
#    y_test = np.zeros(5000)
#    
#    for filename in os.listdir(folder): #Obtain all info
#        img = cv2.imread(os.path.join(folder,filename))
#        resized = cv2.resize(img, (256, 256), interpolation = cv2.INTER_CUBIC)
#        print (filename)
#        if img is not None:
#            data_x[x] = resized
#        if "cat" in filename:
#            data_y[x] = 0
#        elif "dog" in filename:
#            data_y[x] = 1
#        x += 1
#        
#    y = 0;
#    for x in range(x_test.shape[0]):#Obtain Testing Data
#        print("Selected", random_choice[x])
#        print("Placing in ", y)
#        x_test[y] = data_x[random_choice[x]]
#        y_test[y] = data_y[random_choice[x]]
#        y+=1
#    
#    y = 0
#    for x in range(data_x.shape[0]): #Obtain Training Data
#        if x not in random_choice:
#            print("Taking ",x, "for analysis to ",y)
#            x_train[y] = data_x[x]
#            y_train[y] = data_y[x]
#            y+=1
#    return x_train, y_train, x_test, y_test
#
#
#x_train, y_train, x_test, y_test = load_images_from_folder('/Users/oscargalindo/Downloads/all/train/')
#print("Processed")
#
#batch_size = 128
#num_classes = 2
#epochs = 12
#
## input image dimensions
#img_rows, img_cols = 256, 256
#input_shape = (img_rows, img_cols, 3)
#x_train = x_train.astype('float32')
#x_test = x_test.astype('float32')
#x_train /= 255
#x_test /= 255
#print('x_train shape:', x_train.shape)
#print(x_train.shape[0], 'train samples')
#print(x_test.shape[0], 'test samples')
#
## convert class vectors to binary class matrices
#y_train = keras.utils.to_categorical(y_train, num_classes)
#y_test = keras.utils.to_categorical(y_test, num_classes)
#
#model = Sequential()
#model.add(Conv2D(32, kernel_size=(3, 3), input_shape=input_shape))
#model.add(MaxPooling2D(pool_size=(2, 2)))
#model.add(Dropout(0.2))
#model.add(Conv2D(64, (3, 3), activation='relu'))
#model.add(MaxPooling2D(pool_size=(2, 2)))
#model.add(Dropout(0.2))
#model.add(Flatten())
#model.add(Dense(128, activation='relu'))
#model.add(Dense(num_classes, activation='softmax'))
#
#model.summary()
#
#model.compile(loss=keras.losses.categorical_crossentropy,
#              optimizer=keras.optimizers.RMSprop(),
#              metrics=['accuracy'])
#
#model.fit(x_train, y_train, batch_size=batch_size, epochs=epochs, verbose=1, validation_data=(x_test, y_test))
#score = model.evaluate(x_test, y_test, verbose=0)
#print('Test loss:', score[0])
#print('Test accuracy:', score[1])
##############################################################

'''Problem 2'''
#import numpy as np
#import cv2 as cv2
#
#def find(i):
#    if S[i] <0:
#        return i
#    s = find(S[i]) 
#    S[i] = s #Path compression
#    return s
#
#def union(i,j,thr):
#    # Joins two regions if they are similar
#    # Keeps track of size and mean color of regions
#    ri =find(i)
#    rj = find(j)
#    if (ri!= rj):
#        d =  sum_pixels[ri,:]/count[ri] - sum_pixels[rj,:]/count[rj]
#        diff = np.sqrt(np.sum(d*d))
#        if diff < thr:	
#            S[rj] = ri
#            count[ri]+=count[rj]
#            count[rj]=0
#            sum_pixels[ri,:]+=sum_pixels[rj,:]
#            sum_pixels[rj,:]=0
#            
#def unweighted_union(i,j):
#    # Joins two regions if they are similar
#    # Keeps track of size and mean color of regions
#    ri =find(i)
#    rj = find(j)
#    if (ri!= rj):
#        S[rj] = ri
#        count[ri]+=count[rj]
#        count[rj]=0
#        sum_pixels[ri,:]+=sum_pixels[rj,:]
#        sum_pixels[rj,:]=0
#                  
#def initialize(I):
#    rows = I.shape[0]
#    cols = I.shape[1]   
#    S = np.zeros(rows*cols).astype(np.int)-1
#    count = np.ones(rows*cols).astype(np.int)       
#    sum_pixels = np.copy(I).reshape(rows*cols,3)      
#    return S, count, sum_pixels         
#
#def connected_components_segmentation(I,thr):
#    rows = I.shape[0]
#    cols = I.shape[1]   
#    for p in range(S.shape[0]):
#        if p%cols < cols-1:  # If p is not in the last column
#            union(p,p+1,thr) # p+1 is the pixel to the right of p 
#        if p%cols < cols-1 and p//cols < rows -1:#Pixel down and to the right
#            union(p,p+cols+1, thr)
#        if p//cols < rows-1: # If p is not in the last row   
#            union(p,p+cols,thr) # p+cols is the pixel to below p
#            
#def calc_thr (I):
#    blue_std = np.std(I[:,:,0])
#    green_std = np.std(I[:,:,1])
#    red_std = np.std(I[:,:,2])
#    std_mean = (blue_std+green_std+red_std)/3
#    median = np.median([blue_std, green_std, red_std])
#    return np.mean([std_mean, median])
#
#def calc_thr_weighted(I):
#    std = np.array([np.std(I[:,:,0]), np.std(I[:,:,1]), np.std(I[:,:,2])])
#    sort = np.sort(std)
#    weighted_thr = ((sort[2] * 2)/3) + (1/6) * (sort[1]+sort[0])
#    return weighted_thr
#
#def connect_ones(S, count):
#    for x in range(S.shape[0]-1):
#        if S[x] == -1 and count[x] == 1:
#            for y in range(x+1, S.shape[0]):
#                if S[y] == -1 and count[y]:
#                    unweighted_union(x,y)
#                    break
#            
#
#I  =  (cv2.imread('images.png',1)/255).astype(np.float64)
#thr = calc_thr_weighted(I)
#print('Calculated Threshold using median and mean', calc_thr(I))
#print('Calculated Weighted', calc_thr_weighted(I))
#combined_channels = np.concatenate((I[:,:,2], I[:,:,1], I[:,:,0]), axis=1)
#
#rows = I.shape[0]
#cols = I.shape[1]   
#S, count, sum_pixels = initialize(I)
#connected_components_segmentation(I,thr)
#connect_ones(S,count)
#
#
#print('Regions found: ',np.sum(S==-1))
#print('Size 1 regions found: ',np.sum(count==1))
#
#rand_cm = np.random.random_sample((rows*cols, 3))
#seg_im_mean = np.zeros((rows,cols,3))
#seg_im_rand = np.zeros((rows,cols,3))
#for r in range(rows-1):
#    for c in range(cols-1):
#        f = find(r*cols+c)
#        seg_im_mean[r,c,:] = sum_pixels[f,:]/count[f]
#        seg_im_rand[r,c,:] = rand_cm[f,:]
#                    
#print('Standard Deviation Channel Blue', np.std(I[:,:,0]))
#print('Standard Deviation Channel Green', np.std(I[:,:,1]))
#print('Standard Deviation Channel Red', np.std(I[:,:,2]))
#
#combined = np.concatenate((I,seg_im_mean, seg_im_rand), axis=1)
#cv2.imwrite('r.png', combined*255)
#cv2.imwrite('r_channels.png', combined_channels*225)
##############################################################

'''Problem 3'''
# Simple bayesian correlation filter
# Programmed by Olac Fuentes
# Last modified November 19, 2018

import numpy as np
import cv2
import time

def get_coordinates(event,x,y,flags,param):
    global x0, x1, y0, y1
    if event == cv2.EVENT_LBUTTONDOWN:
        if x0==-1:
            x0=x
            y0=y
            print('Entered x0 =',x0,'y0 =',y0)
        elif x1==-1:
            x1=x+1
            y1=y+1
            print('Entered x1 =',x1,'y1 =',y1)
            
global original_pattern
def get_pattern():
    global x0, x1, y0, y1, original_pattern
    cv2.namedWindow('image')
    cv2.setMouseCallback('image',get_coordinates)
    while(x1==-1):
        ret, img = cap.read()
        img = cv2.GaussianBlur(img,(5,5),0)
        cv2.imshow('image',img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cv2.destroyWindow('image') 
    original_pattern = img[y0:y1,x0:x1,:]
    return (img[y0:y1,x0:x1,:]/255).astype(np.float)

x0=x1=y0=y1=-1
cap = cv2.VideoCapture(0)
pattern = get_pattern()
mean_filt = np.ones((pattern.shape[0],pattern.shape[1]))
mean_filt = mean_filt/np.sum(mean_filt)
py = pattern.shape[0]
px = pattern.shape[1]
cv2.imshow('pattern',pattern)
for i in range(3):
    pattern[:,:,i] = pattern[:,:,i] - np.mean(pattern[:,:,i])
start = time.time()
count=0
rows = 720
cols = 1280
fm = np.zeros((rows,cols,3))
col_mat = np.tile(np.arange(cols),(rows,1))
row_mat = np.tile(np.arange(rows),(cols,1)).T
k=1000

while(True): 
    count+=1
    ret, frame = cap.read()
    frame = cv2.GaussianBlur(frame,(5,5),0)
    frame = (frame/255).astype(np.float32)
    for i in range(1,3):
        fm[:,:,i]=cv2.filter2D(frame[:,:,i],-1,mean_filt,anchor =(0,0))
    centered_frame = frame - fm
    
    match=cv2.filter2D(centered_frame[:,:,0],-1,pattern[:,:,0],anchor =(0,0))
    match+=cv2.filter2D(centered_frame[:,:,1],-1,pattern[:,:,1],anchor =(0,0))
    match+=cv2.filter2D(centered_frame[:,:,2],-1,pattern[:,:,2],anchor =(0,0))
    match = match/np.max(match)
    
    print(original_pattern.shape)
    sift = cv2.xfeatures2d.SIFT_create()
    pattern_grayscale = cv2.cvtColor(original_pattern, cv2.COLOR_BGR2GRAY)
    p_pattern_grayscale = cv2.cvtColor(frame[y0:y0+pattern.shape[0],x0:x0+pattern.shape[1],:], cv2.COLOR_BGR2GRAY)
#    cv2.imshow('Original', pattern_grayscale)
#    cv2.imshow('Candidate', p_pattern_grayscale)
#    kp_original = sift.detect(pattern_grayscale, None)
#    kp_new = sift.detect(p_pattern_grayscale, None)
    distance = np.sqrt(np.sum(np.abs(pattern_grayscale-p_pattern_grayscale)))
    print("Distance", distance)
    distance_threshold = np.sqrt(32*original_pattern.shape[0]*original_pattern.shape[1])
    
    if distance < distance_threshold:
        pattern = frame[y0:y0+pattern.shape[0],x0:x0+pattern.shape[1],:]
    prior_x = col_mat - x0
    prior_y = row_mat - y0
    prior = prior_x*prior_x +prior_y*prior_y
    prior = np.exp(-prior/k)  
    combined = match*prior
    cv2.imshow('prior probability',prior)
    cv2.imshow('match probability',match)
    cv2.imshow('combined probability',combined)
    y0,x0 = np.unravel_index(combined.argmax(), match.shape)
   
    cv2.rectangle(frame,(x0, y0), (x0+px, y0+py),(0,255,0),1)    
    cv2.imshow('frame',frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
elapsed_time = time.time()-start
print('Capture speed: {0:.2f} frames per second'.format(count/elapsed_time)) 
  
cap.release()
cv2.destroyAllWindows()
##############################################################