#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np
"""
Created on Mon Oct  1 07:05:26 2018

@author: oscargalindo
"""
x = np.array([1, 2, 3, 4])
print(x.shape[0])
x = 3.5
y = 4.5
floor_x = x//1
floor_y = y//1
upper_x = (x+0.5)//1
upper_y = (y+0.5)//1
print("Lower x: ", floor_x)
print("Lower y: ", floor_y)
print("Upper x: ", upper_x)
print("Upper y: ", upper_y)

