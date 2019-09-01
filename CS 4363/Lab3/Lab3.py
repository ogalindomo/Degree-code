#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 16 12:48:51 2018

@author: oscargalindo
"""
import numpy as np
from PIL import Image
import pylab as plt
import cv2 
import time
#################PROBLEM 1###########################
'''
def area_based (I,r,c):
    value = np.zeros((3,r.shape[0]))
    for x in range(r.shape[0]):
        floor_x = r[x]//1
        floor_y = c[x]//1
        a = c[x] - floor_y
        b = r[x] - floor_x
        value[x] = ((1-a)*(1-b)*I[floor_x,floor_y]) +(a*(1-b)*I[floor_x + 1, floor_y])
        +((1-a)*b*I[floor_x,floor_y+1]) +(a*b*I[floor_x+1,floor_y+1])
    return value
'''
#####################################################

##############PROBLEM 2#############################
'''
def transform(H,fp):
    # Transforming point fp according to H
    # Convert to homogeneous coordinates if necessary
    if fp.shape[0]==2:
          t = np.dot(H,np.vstack((fp,np.ones(fp.shape[1]))))
    else:
        t = np.dot(H,fp)
    print (t[:2])
    return t[:2]


################Images#############################
im2 = np.array(Image.open('banner_small.jpg'), dtype=np.uint8)
plt.figure(1)
plt.imshow(im2)
plt.show()

source_im = np.array(Image.open('tennis.jpg'), dtype=np.uint8)
plt.figure(2)
plt.imshow(source_im)
plt.show()
###################################################

#############Vector Sizes of Banner################
x = [0,0,im2.shape[0]-1]
y = [0,im2.shape[1]-1,0]
fp = np.vstack((x,y))
####################################################

#############Point readings#########################
print("Click destination points, top-left, top-tight, bottom-left corners and bottorm right.")
tp = np.asarray(plt.ginput(n=4), dtype=np.float).T
#tp = tp[[1,0],0:4]
tp1 = tp[[1,0],0:3]
tp2 = tp[[1,0],1:4]
print (tp1)
print (tp2)
print(fp)
print(tp)
##################################################

#############Generate Pieces######################
part = np.zeros(((im2.shape[0], im2.shape[1],im2.shape[2])))
division_factor = (im2.shape[1]-1)/(im2.shape[0]-1)
for x_range in range(im2.shape[0]):
    dy = ((division_factor * x_range)//1)
    dy = int(dy)
    part[x_range,0:dy,:] = im2[x_range,0:dy]   
    
part2 = im2 - part  
##################################################

#############Original Pseudoinverse###############
'''
#Using pseudoinverse
# Generating homogeneous coordinates

#fph = np.vstack((fp,np.ones(fp.shape[1])))
#tph = np.vstack((tp,np.ones(tp.shape[1])))
#H = np.dot(tph,np.linalg.pinv(fph))
#print((transform(H,fp)+.5).astype(np.int))
'''
##################################################

###########Pseudoinverse of Parts#################

fph = np.vstack((fp,np.ones(fp.shape[1])))
tph1 = np.vstack((tp1,np.ones(tp1.shape[1])))
H1 = np.dot(tph1, np.linalg.pinv(fph))
tph2 = np.vstack((tp2,np.ones(tp2.shape[1])))
H2 = np.dot(tph2, np.linalg.pinv(fph))
#print((transform(H1,fp)+.5).astype(np.int))
#print((transform(H2,fp)+.5).astype(np.int))

##################################################

#################Display##########################
#Generating pixel coordinate locations

ind = np.arange(im2.shape[0]*im2.shape[1])
row_vect = ind//im2.shape[1]
col_vect = ind%im2.shape[1]
coords = np.vstack((row_vect,col_vect))

#new_coords = transform(H,coords).astype(np.int)
#target_im = source_im
#target_im[new_coords[0],new_coords[1],:] = im2[coords[0],coords[1],:]

new_coords = transform(H1,coords).astype(np.int)
target_im = source_im
target_im[new_coords[0],new_coords[1],:] = part[coords[0],coords[1],:]
ind = np.arange(im2.shape[0]*im2.shape[1])

new_coords = transform(H2,coords).astype(np.int)
target_im = source_im
target_im[new_coords[0],new_coords[1],:] = part2[coords[0],coords[1],:]

##################################################


###################Show Result####################
plt.figure(3)
plt.imshow(target_im)
plt.show()
'''
##################################################

#################PROBLEM 4###########################

source_im = np.array(Image.open('tennis.jpg'), dtype=np.uint8)
plt.figure(1)    
plt.imshow(source_im)    
plt.show()
while(True):
    plt.figure(1)    
    plt.imshow(source_im)    
    plt.show()
    plt.figure(2)    
    plt.imshow(source_im)    
    plt.show()
    print("Click source and destination of warp point")
    p = np.asarray(plt.ginput(n=2), dtype=np.float32)
    print(p)
    print(p[0]-p[1])
    plt.plot(p[:,0], p[:,1], color="blue")
    plt.plot(p[0][0], p[0][1],marker='x', markersize=3, color="red")
    plt.plot(p[1][0], p[1][1],marker='x', markersize=3, color="red")
    plt.show()
    start = time.time()
    
    #Generate pixels coordinates in the destination image       
    dest_im = np.zeros(source_im.shape, dtype=np.uint8)                 
    max_row = source_im.shape[0]-1
    max_col = source_im.shape[1]-1
    dest_rows = dest_im.shape[0]
    dest_cols = dest_im.shape[1]
    
    #Painting outline of source image black, so out of bounds pixels can be painted black  
    source_im[0]=0
    source_im[max_row]=0         
    source_im[:,0]=0
    source_im[:,max_col]=0 
             
    #Generate pixel coordinates in the destination image         
    ind = np.arange(dest_rows*dest_cols)
    row_vect = ind//dest_cols
    col_vect = ind%dest_cols
    coords = np.vstack((row_vect,col_vect))
    
    #Computing pixel weights, pixels close to p[1] will have higher weights    
    dist = np.sqrt(np.square(p[1][1] - row_vect) + np.square(p[1][0] - col_vect))
    weight = np.exp(-dist/100)         #Constant needs to be tweaked depending on image size
    
    #Computing pixel weights, pixels close to p[1] will have higher weights    
    source_coords = np.zeros(coords.shape, dtype=np.int)
    disp_r = (weight*(p[0][1]-p[1][1])).astype(int)
    disp_c = (weight*(p[0][0]-p[1][0])).astype(int)
    source_coords[0] = coords[0] + disp_r
    source_coords[1] = coords[1] + disp_c
                 
    #Fixing out-of-bounds coordinates               
    source_coords[source_coords<0] = 0
    source_coords[0,source_coords[0]>max_row] = max_row             
    source_coords[1,source_coords[1]>max_col] = max_col      
          
    dest_im = source_im[source_coords[0],source_coords[1],:].reshape(dest_rows,dest_cols,3)
    source_im = np.copy(dest_im)
    plt.figure(2)
    plt.imshow(dest_im)
    plt.show()
    

elapsed_time = time.time()-start
print('Elapsed time: {0:.2f} '.format(elapsed_time))   

######################################################

#################PROBLEM 5###########################
'''
source_im = np.array(Image.open('tennis.jpg'), dtype=np.uint8)

ref_points = np.zeros((4,2))





plt.figure(2)
plt.imshow(source_im)
plt.show()
'''
####################################################