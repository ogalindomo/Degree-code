#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 26 12:08:06 2020

@author: oscargalindo
"""


import numpy as np
from fractions import Fraction 
P = np.array([
     [1/40,13/40,13/40,13/40],
     [1/4,1/4,1/4,1/4],
     [1/4,1/4,1/4,1/4],
     [1/4,1/4,1/4,1/4]
     ])
x = np.array([1,0,0,0])

print("-----------------------")
for i in range(75):
    print("Iteration",i)
    x_p = x.dot(P)
    print("x' = [",end=" ")
    for e in x_p:
        print(e,end=' ')
    print("]")
    x = x_p
    print("-----------------------")
