#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 10 18:35:32 2019

@author: oscargalindo
"""
import os
import numpy as np
class stock_data():
    def __init__(self, stock, basedir, test, validation):
        self.stock = stock
        self.base = basedir
        self.frac_test = test
        self.frac_validation = validation
        symbols = list()
        if os.path.isdir(basedir):
            for x in os.listdir(basedir):
                if x != 'DS.Store':
                    symbol = x
                    symbol = symbol[:-9]
                    symbols.append(symbol)
            symbols.sort()
            if stock in symbols:
                print("The symbol",stock,"was found.")
                print("Extracting information.")
                self.create_data()
            else:
                print("Symbol:",stock,"not found.")
        else: 
            print("Directory is not valid")
        
        
    def create_data(self):
        entries = list()
        with open(os.path.join(self.base,(self.stock+"_data.csv")), mode='r') as x:
            for line in x:
                input_line = line.split(',')
                entries.append(input_line[4])
            entries = np.asarray(entries[1:], dtype=np.float32)
            entries = entries.reshape(entries.shape[0], 1)
            self.divide_data(info=entries, space_time=7)

            
    def divide_data(self, info, space_time=30):
         self.x_test = []
         self.x_validation = []
         self.y_test = []
         self.y_validation = []
#         print(info)
         X = []
         Y = []
         for i in range(len(info)-space_time-1):
             X.append(info[i:(i+space_time),0])
             Y.append(info[(i+space_time), 0])
         
         self.x_test, self.x_validation = np.asarray(X[:int(len(X)*self.frac_test)]), np.asarray(X[int(len(X)*self.frac_test):])
         self.y_test, self.y_validation = np.asarray(Y[:int(len(Y)*self.frac_test)]), np.asarray(Y[int(len(Y)*self.frac_test):])
         print(self.x_test.shape)
         print(self.x_validation.shape)
         print(self.y_test.shape)
         print(self.y_validation.shape)