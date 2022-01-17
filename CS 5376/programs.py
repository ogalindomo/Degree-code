#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  8 18:12:03 2020

@author: oscargalindo
"""
import numpy as np

def calculate_joint_probability(matrix,direction):
    p_r = np.zeros((matrix.shape[0]))
    p_c = np.zeros((matrix.shape[1]))
    if direction =='r':
        for r in range(matrix.shape[0]):
            p_r[r] = np.sum(matrix[r,:])
        return p_r
    if direction == "c":
        for c in range(matrix.shape[1]):
            p_c[c] = np.sum(matrix[:,c])
        return p_c
    
def independent(matrix):
    p_r = calculate_joint_probability(matrix, 'r')
    p_c = calculate_joint_probability(matrix, 'c')
    print(p_r,p_c)
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            if not p_c[j] == matrix[i,j]/p_r[i]:
                return False
    return True
    
if __name__=="__main__":
    # m = [[0.35,0.15],[0.25,0.25]]
    m = [[0.1,0.2,0.2],[0.2,0.2,0.1]]
    a = np.array([0,1,2,3])
    m = np.array(m)
    print(independent(m))
    # print(calculate_joint_probability(m, row=True, column=True))
    
    