#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  8 12:51:25 2021

@author: oscargalindo
"""
import numpy as np
import time
import matplotlib.pyplot as plt
import os
from skimage.transform import rescale, resize, rotate 
import tensorflow as tf
from PIL import Image
import matplotlib.image as mpimg
import cv2
from tqdm import tqdm


class DataGenerator(tf.keras.utils.Sequence):
    def __init__(self, image_dir, size, width, length, pos_frac = 0.5, neg_frac = 0.5, batch_size=8, num_classes=2, shuffle=True):
        self.batch_size = batch_size
        self.indices = [i for i in range(size)]
        self.num_classes = num_classes
        self.shuffle = shuffle
        self.image_dir = image_dir
        self.on_epoch_end()
        self.generate_lists()
        self.size = size
        self.width = width
        self.length = length
        self.pos_frac = pos_frac
        self.neg_frac = neg_frac
        self.create_dataset()

    def __len__(self):
        return len(self.indices) // self.batch_size

    def __getitem__(self, index):
        index = self.index[index * self.batch_size:(index + 1) * self.batch_size]
        batch = [self.indices[k] for k in index]
        
        X, y = self.__get_data(batch)
        print("HERE")
        return X, y

    def create_dataset(self):
        limit = int(self.size * self.pos_frac)
        self.dataset = np.zeros((self.size,self.width,self.length,3))
        self.idx = np.zeros((self.size))
        for i in tqdm(range(self.size)):
            if i < limit:
                images, bboxes = self.gen_images(self.neg_list, self.pos_list, num_ims = 1, canv_rows = self.width, canv_cols = self.length,n_objects=1)
                # self.dataset[i,] = images[0]
                self.idx[i] = 1
                img = (255*images[0]).astype(np.uint8)
                im = Image.fromarray(img)
                name = f'./Images/Validation/Positive/{00000+i}.jpg'
                im.save(name)
            else:
                images = self.gen_images(self.neg_list, num_ims = 1, canv_rows = self.width, canv_cols = self.length,n_objects=1)
                # self.dataset[i,] = images[0]
                img = (255*images[0]).astype(np.uint8)
                im = Image.fromarray(img)
                name = f'./Images/Validation/Negative/{00000+i}.jpg'
                im.save(name)
                self.idx[i] = 0
        plt.close()

    def on_epoch_end(self):
        self.index = np.arange(len(self.indices))
        if self.shuffle == True:
            np.random.shuffle(self.index)

    def generate_lists(self):
        image_dir = self.image_dir
        image_list = os.listdir(image_dir)
        
        # We define the positive class as the im images containing bat images
        self.pos_list, self.neg_list = [],[]    
        for im in image_list:
            if 'bat' in im:
                self.pos_list.append(im)
            else:
                self.neg_list.append(im)
        
    def __get_data(self, batch):
        X = np.zeros((self.batch_size,self.width,self.length,3))
        y = np.zeros((self.batch_size)).astype(np.uint8)
        limit = int(self.size * self.pos_frac)
        for i, id in enumerate(batch):
            # X[i,] = # logic
            print(i,id)
            if id < limit:
                y[i] = 1 #1 is bat
                #images, bboxes = self.gen_images(self.neg_list, self.pos_list, num_ims = 1, canv_rows = self.width, canv_cols = self.length,n_objects=5)
                img = mpimg.imread('./Images/Validation/Positive/'+str(id)+'.jpg').astype(np.float32)
                img = (img/255).astype(np.float32)
                X[i,] = img
            else:
                y[i] = 0 
                #images = self.gen_images(self.neg_list, num_ims = 1, canv_rows = self.width, canv_cols = self.length,n_objects=5)
                img = mpimg.imread('./Images/Validation/Negative/'+str(id)+'.jpg').astype(np.float32)
                img = (img/255).astype(np.float32)
                X[i,] = img
        return X, y
        
    def gen_images(self,image_list, positive_list = [], num_ims = 1,canv_rows=1080,canv_cols=1920, n_objects=80, alpha =0.7,game = False):
    # Generates a list of images of size (canv_rows,canv_cols)
    # If positive_list is not empty, each image will contain exactly one object from that list
    # If positive_list is not empty, it will also return a list with the bounding boxes of the positive objects
        images, bboxes = [], []
        for k in range(num_ims):
            canvas =  np.zeros((canv_rows,canv_cols,3),dtype=np.float32)
            if game:
                canvas[:50,-50:,0] = 1
            objects = np.random.randint(0,len(image_list),n_objects)
            
            objects = [image_list[np.random.randint(0,len(image_list))] for i in range(n_objects)]
            if len(positive_list)>0:
                objects[np.random.randint(0,n_objects)] = positive_list[np.random.randint(0,len(positive_list))]
                                          
            for obj in objects:
                image = np.load(self.image_dir + obj)*255
                image = rotate(image, np.random.random()*360, resize=True)
                if image.shape[0] < canv_cols and image.shape[1] < canv_rows:
                    image = rescale(image, np.random.random()*0.5+0.5)
                else:
                    image = rescale(image,np.random.random()*0.3 +0.1)
                image = (image>0.5).astype(np.float32)
                if obj in positive_list: # Crop if positive image to get correct bounding box
                    sr = np.where(np.sum(image,axis=0)>0)[0]
                    sc = np.where(np.sum(image,axis=1)>0)[0]
                    image = image[sc[0]:sc[-1]+1,sr[0]:sr[-1]+1]
                alpha_im =  np.expand_dims(image>0.5,axis=-1)*alpha
                image = np.expand_dims(image,axis=-1)
                image = image*(np.sqrt(np.random.random((1,3))))
                m_min = 2
                for j in range(10): # Choose the location with the least overlap   
                    ri,ci = np.random.randint(canv_rows-image.shape[0]),np.random.randint(canv_cols-image.shape[1])
                    background = canvas[ri:ri+image.shape[0],ci:ci+image.shape[1]] 
                    mask_bgnd = np.amax(background,axis=2)>0.001
                    m = np.mean(mask_bgnd)
                    if m<m_min:
                        r,c = ri,ci
                        m_min = m  
                        if m<0.2:
                            break
                canvas[r:r+image.shape[0],c:c+image.shape[1]] = image*alpha_im + canvas[r:r+image.shape[0],c:c+image.shape[1]]*(1-alpha_im)
                if obj in positive_list:
                    bboxes.append([c,r,c+image.shape[1],r+image.shape[0]]) #[x0,y0,x1,y1]
            images.append(canvas)
        if len(positive_list)>0:
            return images, bboxes
        return images
    

# a = DataGenerator("./MPEG7Dataset/resized_npy/" , 10, 256,256, batch_size=2)
# print(a.__len__())
# x,y = (a.__getitem__(0))
# for i in range(x.shape[0]): 
#     plt.imshow(x[-1])

