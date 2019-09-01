#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 10 19:36:12 2019

@author: oscargalindo
"""
from package import data_import


original_dataset_dir = '/Users/oscargalindo/Desktop/Classes/CS 4371/Lab 1 (Ch.5)/dogs-vs-cats/train'
base_dir = '/Users/oscargalindo/Desktop/Classes/CS 4371/Lab 1 (Ch.5)/sets'
data = data_import(original_dataset_dir, base_dir)