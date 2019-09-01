#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 10 09:53:10 2019

@author: oscargalindo
"""
import os, shutil
class data_import: 
##########################################################################################
    global train_dir, validation_dir, test_dir #Directories are global for use.          #
    global train_cats, train_dogs, validation_cats, validation_dogs, test_cats, test_dogs#
    global original_dataset_dir                                                          #
    global base_dir                                                                      #
##########################################################################################
    
    def make_directories(base_dir, data_directory):
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
    
    def catndogs_dir(train_dir, validation_dir, test_dir):
        train_cats = os.path.join(train_dir, 'cats')
        train_dogs = os.path.join(train_dir, 'dogs')
        validation_cats = os.path.join(validation_dir,'cats')
        validation_dogs = os.path.join(validation_dir,'dogs')
        test_cats = os.path.join(test_dir,'cats')
        test_dogs = os.path.join(test_dir,'dogs')
        if not os.path.isdir(train_cats):
            os.mkdir(train_cats)
        if not os.path.isdir(train_dogs):
            os.mkdir(train_dogs)
        if not os.path.isdir(validation_cats):
            os.mkdir(validation_cats)
        if not os.path.isdir(validation_dogs):
            os.mkdir(validation_dogs)
        if not os.path.isdir(validation_dogs):
            os.mkdir(validation_dogs)
        if not os.path.isdir(test_cats):
            os.mkdir(test_cats)
        if not os.path.isdir(test_dogs):
            os.mkdir(test_dogs)   
        return train_cats, train_dogs, validation_cats, validation_dogs, test_cats, test_dogs
    
    def import_images_cats():
        global original_dataset_dir, train_cats, validation_cats, test_cats
        for i in range (5000):
            name = "cat.{}.jpg".format(i)
            src = os.path.join(original_dataset_dir, name)
            dst = os.path.join(train_cats, name)
            shutil.copyfile(src,dst)
            
        for i in range (5000, 9000):
            name = "cat.{}.jpg".format(i)
            src = os.path.join(original_dataset_dir, name)
            dst = os.path.join(validation_cats, name)
            shutil.copyfile(src,dst) 
            
        for i in range (9000,10000):
            name = "cat.{}.jpg".format(i)
            src = os.path.join(original_dataset_dir, name)
            dst = os.path.join(test_cats, name)
            shutil.copyfile(src,dst)
    
    def import_images_dogs():
        global original_dataset_dir, train_dogs, validation_dogs, test_dogs
        for i in range (5000):
            name = "dog.{}.jpg".format(i)
            src = os.path.join(original_dataset_dir, name)
            dst = os.path.join(train_dogs, name)
            shutil.copyfile(src,dst)
            
        for i in range (5000, 9000):
            name = "dog.{}.jpg".format(i)
            src = os.path.join(original_dataset_dir, name)
            dst = os.path.join(validation_dogs, name)
            shutil.copyfile(src,dst) 
            
        for i in range (9000,10000):
            name = "dog.{}.jpg".format(i)
            src = os.path.join(original_dataset_dir, name)
            dst = os.path.join(test_dogs, name)
            shutil.copyfile(src,dst)
        
        
    def __init__(self, original, base):        
#        original_dataset_dir = '/Users/oscargalindo/Desktop/Classes/CS 4371/Lab 1 (Ch.5)/dogs-vs-cats/train'
#        base_dir = '/Users/oscargalindo/Desktop/Classes/CS 4371/Lab 1 (Ch.5)/sets'
        original_dataset_dir = original
        base_dir = base
        (train_dir, validation_dir, test_dir) = self.make_directories(base_dir, original_dataset_dir)
        (train_cats, train_dogs, validation_cats, validation_dogs, test_cats, test_dogs) = self.catndogs_dir(train_dir, validation_dir, test_dir)
        self.import_images_cats()
        self.import_images_dogs()