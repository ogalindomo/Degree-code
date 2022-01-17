#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 20:10:05 2020

@author: oscargalindo
"""
import random

def getList(l):
    e = []
    for line in l:
        parts = line.split(" ")
        a = [parts[0][5:],parts[1][6:]]
        e.append(a)
    return e

def getWords(l):
    e = []
    for elem in l:
        e.append(elem[0])
    return e

def getclean(l1,l2):
    c = []
    for e in l1:
        if not e in l2:
            c.append(e)
    return c

if __name__=="__main__":
    positive = open("/Users/oscargalindo/Downloads/Goodresults-6.txt","r")
    negative = open("/Users/oscargalindo/Downloads/badresults-6.txt","r")
    p_lines = positive.readlines()
    n_lines = negative.readlines()
    e1 = getList(p_lines)
    e2 = getList(n_lines)
    w1 = getWords(e1)
    w2 = getWords(e2)
    c1 = getclean(w1,w2)#Positive
    c2 = getclean(w2,w1)#Negative
    
    r = []
    indexes = random.sample(range(len(c2)), 50)
    for i in indexes:
        r.append(c2[i])
    print(r)