#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 17 12:12:03 2019

@author: oscargalindo
"""    
import os, shutil
class data_creation:
    
    def __init__(self, original, sets, rename, train = 0, validation = 0, test = 0):
        self.original_dataset_dir = original
        self.rename_dir =  rename
        self.base_dir = sets
        self.create_renaming()
        self.test, self.validation, self.train = self.__create_dir()
        self.create_separation()
        self.populate(train, validation, test)
#        self.eliminate_extra()
        
    def create_renaming(self): 
        dir_num = 0
        for x in os.listdir(self.original_dataset_dir): #Reads all the breeds from the original dataset
             if(x == ".DS_Store"):
                 continue
             breed_name = str(x[10:]) #Extracts the name of the breed
#             num_pics = len(os.listdir(os.path.join(self.original_dataset_dir, x))) #Obtains the number of pictures available
             num = 0 #Initializes the count of pictures
             if(os.path.isdir(os.path.join(self.rename_dir,breed_name)) == False): #Creates a directory only if it does not exist
                 os.mkdir(os.path.join(self.rename_dir,breed_name))
             for pic in os.listdir(os.path.join(self.original_dataset_dir, x)): #Copies from the original dataset all pictures of that breed.
                 num += 1
                 i = (os.path.join(os.path.join(self.original_dataset_dir, x), pic)) #Image to copy
                 name = breed_name+str(num)+".jpg" #Name of the picture
                 file = os.path.join(os.path.join(self.rename_dir, breed_name), name) #Destination for the image
                 shutil.copy(i, file)#Copy line
#             print(x, num_pics)
             dir_num += 1
        print("The number of directories found:",dir_num)
        
    def __create_dir(self):
        division = ['train','test', 'validation']
        for x in division:
            if not os.path.isdir(os.path.join(self.base_dir, x)):
                os.mkdir(os.path.join(os.path.join(self.base_dir, x)))
            if x == 'train':
                self.train = os.path.join(os.path.join(self.base_dir, x))
            elif x == 'test':
                self.test = os.path.join(os.path.join(self.base_dir, x))
            else :
                self.validation = os.path.join(os.path.join(self.base_dir, x))
        return os.path.join(self.base_dir, division[1]), os.path.join(self.base_dir, division[2]), os.path.join(self.base_dir, division[0])
                
    def create_separation(self):
        for x in os.listdir(self.rename_dir):
            if not x == ".DS_Store":
                if not os.path.isdir(os.path.join(self.validation, x)):
                    os.mkdir(os.path.join(self.validation, x))
                if not os.path.isdir(os.path.join(self.test, x)):
                    os.mkdir(os.path.join(self.test, x))
                if not os.path.isdir(os.path.join(self.train, x)):
                    os.mkdir(os.path.join(self.train, x))
                
    def populate(self, train, validation, test):
        for x in os.listdir(self.rename_dir):
            if not x == ".DS_Store":
               total = len(os.listdir(os.path.join(self.rename_dir, x)))
               training = (int)(total * train)
               valid = (int)(total*validation)
#               tests = (int)(test*total)
               images = os.listdir(os.path.join(self.rename_dir, x))
#               print("Breed:",x,"Total:",total," Train:", training," Valid:",valid," Test:",tests," Added:",(training+valid+tests))
               for num in range(0, training):
                   file = os.path.join(os.path.join(self.rename_dir, x), str(images[num]))
                   target = os.path.join(os.path.join(self.train, x), str(images[num]))
                   shutil.copy(file, target)
              
               for num in range(training, training+valid):
                   file = os.path.join(os.path.join(self.rename_dir, x), str(images[num]))
                   target = os.path.join(os.path.join(self.validation, x), str(images[num]))
                   shutil.copy(file, target)
                   
               for num in range(training+valid, len(images)):
                   file = os.path.join(os.path.join(self.rename_dir, x), str(images[num]))
                   target = os.path.join(os.path.join(self.test, x), str(images[num]))
                   shutil.copy(file, target)
            elif x == ".DS_Store":
                 os.remove(os.path.join(self.rename_dir,x))
                 
    def eliminate_extra(self):
        for x in os.listdir(self.test):
            if x == ".DS_Store":
                os.remove(os.path.join(self.test,x))
        for x in os.listdir(self.validation):
            if x == ".DS_Store":
                os.remove(os.path.join(self.validation,x))
        for x in os.listdir(self.train):
            if x == ".DS_Store":
                os.remove(os.path.join(self.train,x))