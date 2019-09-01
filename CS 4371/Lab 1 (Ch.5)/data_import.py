#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 10 09:53:10 2019

@author: oscargalindo
"""
import os, shutil
class data_import: 
###########################################################################################
#    global train_dir, validation_dir, test_dir #Directories are global for use.          #
#    global train_cats, train_dogs, validation_cats, validation_dogs, test_cats, test_dogs#
#    global original_dataset_dir, base_dir                                                #
##########################################################################################
    def __init__(self, original, base, train = 0, validation = 0, test = 0):        
        ##########################################################################################
        self.original_dataset_dir = original
        self.base_dir = base
        (self.train_dir, self.validation_dir, self.test_dir) = self.make_directories(self.base_dir, self.original_dataset_dir)
#        (self.train_cats, self.train_dogs, self.validation_cats, self.validation_dogs, self.test_cats, self.test_dogs) = self.catndogs_dir(self.train_dir, self.validation_dir, self.test_dir)
        #self.import_images_cats(train, validation, test)
        #self.import_images_dogs(train, validation, test)
        ##########################################################################################
        
    def make_directories(self,base_dir, data_directory):
        train_dir = os.path.join(base_dir, 'train')
        validation_dir = os.path.join(base_dir, 'validation')
        test_dir = os.path.join(base_dir, 'test')
        if not os.path.isdir(train_dir):
            os.mkdir(train_dir)
        if not os.path.isdir(validation_dir):
            os.mkdir(validation_dir)
        if not os.path.isdir(test_dir):    
            os.mkdir(test_dir)
        return train_dir, validation_dir, test_dir
        
#    def catndogs_dir(self,train_dir, validation_dir, test_dir):
#        train_cats = os.path.join(train_dir, 'cats')
#        train_dogs = os.path.join(train_dir, 'dogs')
#        validation_cats = os.path.join(validation_dir,'cats')
#        validation_dogs = os.path.join(validation_dir,'dogs')
#        test_cats = os.path.join(test_dir,'cats')
#        test_dogs = os.path.join(test_dir,'dogs')
#        if not os.path.isdir(train_cats):
#            os.mkdir(train_cats)
#        if not os.path.isdir(train_dogs):
#            os.mkdir(train_dogs)
#        if not os.path.isdir(validation_cats):
#            os.mkdir(validation_cats)
#        if not os.path.isdir(validation_dogs):
#            os.mkdir(validation_dogs)
#        if not os.path.isdir(validation_dogs):
#            os.mkdir(validation_dogs)
#        if not os.path.isdir(test_cats):
#            os.mkdir(test_cats)
#        if not os.path.isdir(test_dogs):
#            os.mkdir(test_dogs)   
#        return train_cats, train_dogs, validation_cats, validation_dogs, test_cats, test_dogs
    
#    def import_images_cats(self, train, validation, test):
#        for i in range (train):
#            name = "cat.{}.jpg".format(i)
#            src = os.path.join(self.original_dataset_dir, name)
#            dst = os.path.join(self.train_cats, name)
#            shutil.copyfile(src,dst)
#            
#        for i in range (train, train+validation):
#            name = "cat.{}.jpg".format(i)
#            src = os.path.join(self.original_dataset_dir, name)
#            dst = os.path.join(self.validation_cats, name)
#            shutil.copyfile(src,dst) 
#            
#        for i in range (train+validation,train+validation+test):
#            name = "cat.{}.jpg".format(i)
#            src = os.path.join(self.original_dataset_dir, name)
#            dst = os.path.join(self.test_cats, name)
#            shutil.copyfile(src,dst)
#    
#    def import_images_dogs(self, train, validation, test):
#        for i in range (train):
#            name = "dog.{}.jpg".format(i)
#            src = os.path.join(self.original_dataset_dir, name)
#            dst = os.path.join(self.train_dogs, name)
#            shutil.copyfile(src,dst)
#            
#        for i in range (train, train+validation):
#            name = "dog.{}.jpg".format(i)
#            src = os.path.join(self.original_dataset_dir, name)
#            dst = os.path.join(self.validation_dogs, name)
#            shutil.copyfile(src,dst) 
#            
#        for i in range (train+validation,train+validation+test):
#            name = "dog.{}.jpg".format(i)
#            src = os.path.join(self.original_dataset_dir, name)
#            dst = os.path.join(self.test_dogs, name)
#            shutil.copyfile(src,dst)