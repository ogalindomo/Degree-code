#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 21:31:58 2019

@author: oscargalindo
"""
import os
class data():
    def __init__(self, basedir, test, validation):
        self.base = basedir
        self.frac_test = test
        self.frac_validation = validation
        
        if os.path.isfile(basedir):
                print("The dataset was found.")
                print("Extracting information.")
                self.create_data()
        else: 
            print("Directory is not valid")
            
            'ham' == 'ham'
    def create_data(self):     
        Y = []
        X = []
        with open(self.base, mode='r') as x:
            for line in x:
                input_line = line.split(',', 1)
                if(len(input_line) == 2):
                    if(input_line[0] == 'ham'):
                        Y.append(0)
                    elif(input_line[0] == 'spam'):
                        Y.append(1)
                    X.append(input_line[1])
        self.y = (Y)
        self.x = (X)
#        print(self.y)
#        print(self.x)
#        print(self.y.shape)
#        print(self.x.shape)
        