#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 17 12:12:03 2019

@author: oscargalindo
"""    

import os, shutil
original_dataset_dir = '/Users/oscargalindo/Desktop/stanford-dogs-dataset/Images'
renames_dir = '/Users/oscargalindo/Desktop/stanford-dogs-dataset/Renamed'

def create_classes(): 
    dir_num = 0
    for x in os.listdir(original_dataset_dir): #Reads all the breeds from the original dataset
         if(x == ".DS_Store"):
             continue
         breed_name = str(x[10:]) #Extracts the name of the breed
         num_pics = len(os.listdir(os.path.join(original_dataset_dir, x))) #Obtains the number of pictures available
         num = 0 #Initializes the count of pictures
         if(os.path.isdir(os.path.join(renames_dir,breed_name)) == False): #Creates a directory only if it does not exist
             os.mkdir(os.path.join(renames_dir,breed_name))
         next    
         for pic in os.listdir(os.path.join(original_dataset_dir, x)): #Copies from the original dataset all pictures of that breed.
             num += 1
             i = (os.path.join(os.path.join(original_dataset_dir, x), pic)) #Image to copy
             name = breed_name+str(num)+".jpg" #Name of the picture
             file = os.path.join(os.path.join(renames_dir, breed_name), name) #Destination for the image
             shutil.copy(i, file)#Copy line
         print(x, num_pics)
         dir_num += 1
    print("The number of directories found:",dir_num)
    
#def make_counts():
#    for x in os.listdir(original_dataset_dir):
#        if(x != ".DS_Store" and 

create_classes()
