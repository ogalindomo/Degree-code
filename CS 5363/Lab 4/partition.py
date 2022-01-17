#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 20 23:50:44 2021

@author: oscargalindo
"""

import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy as np
import random

img = mpimg.imread('/Users/oscargalindo/Downloads/2447866537_19e77ae3d6_k.jpg')
# plt.imshow(img)
# num = random.randint(100, img.shape[1])
# plt.imshow(img[:,:num])
# half = img.shape[1]//2


# for i in range(2):
#     plt.imsave(f"/Users/oscargalindo/Desktop/Classes/CS 5363/Lab 4/Part{i}.jpg",img[:,:half])
#     img = img[:,half:]
quarter = img.shape[1]//4
plt.imsave("/Users/oscargalindo/Desktop/Classes/CS 5363/Lab 4/Part0.jpg",img[:,:img.shape[1]//2])
plt.imsave("/Users/oscargalindo/Desktop/Classes/CS 5363/Lab 4/Part2.jpg",img[:,img.shape[1]//2:])
plt.imsave("/Users/oscargalindo/Desktop/Classes/CS 5363/Lab 4/Part1.jpg",img[:,quarter:3*quarter])

