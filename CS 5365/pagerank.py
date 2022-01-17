#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 11 23:13:23 2020

@author: oscargalindo
"""
import numpy as np
from numpy import linalg as LA
import math

def pagerank(matrix,l,r=None):
    nodes = len(matrix)
    count = [0]*nodes
    
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[j][i] == 1:
                count[i] += 1
    # print(count)
    
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            matrix[j][i] = matrix[j][i]/count[i]
    # print(matrix)
    
    M = np.array(matrix)
    r = np.ones(nodes)/nodes
    # print(M)
    # print(r)
    
    for i in range(l):
        r = np.dot(M,r)
    print(r)
    print("Total:",sum(r))
    
def logistic(c,v):
    s = c[0]
    for i in range(len(v)):
        s+=(c[i+1]*v[i])
    print("Logistic probability:",1/(1+math.exp(-s)))
    
def randIndex(idx,benchmark):
    # print(idx)
    # print(benchmark)
    TP,FP,TN,FN = 0,0,0,0
    for i in range(len(idx)-1):
        for j in range(i+1,len(idx)):
            r_idx = idx[i]==idx[j]
            r_ben = benchmark[i]==benchmark[j]
            if not r_idx and not r_ben: 
                TN+=1
            elif r_idx and r_ben:
                TP += 1
            elif not r_idx and r_ben:
                FP += 1
            elif r_idx and not r_ben:
                FN += 1
    print("Rand Index:",((TP+TN)/(FP+FN+TN+TP)))
    
def tanimoto(A,B):
    A,B = np.array(A),np.array(B)
    print((np.dot(A,B))/((LA.norm(A)**2 + LA.norm(B)**2)-np.dot(A,B)))
    
def cosine(A,B):
    A,B = np.array(A),np.array(B)
    print((np.dot(A,B))/(LA.norm(A)*LA.norm(B)))
    
if __name__=="__main__":
    matrix = [
        [0,0,1,1],
        [1,0,1,0],
        [0,1,0,1],
        [1,1,0,0],
    ]
    # pagerank(matrix,l=10000)
    # randIndex([3,1,2,1,2,2],[3,2,1,2,1,1])
    logistic([-168.7313,-9.7069,56.5294],[6,4])
    # tanimoto([1,2,3,4,5],[1,2,3,4,5])
    # cosine([0,0,2*math.log(1.5,10),3*math.log(3,10)],[0,0,math.log(1.5,10),0])