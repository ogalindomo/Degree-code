#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 14:04:09 2020

@author: oscargalindo
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

r = pd.read_csv('/Users/oscargalindo/Desktop/Classes/CS 5365/US_Accidents_Dec19.csv')
# print(r.head())
l = [e for e in r.columns]
severity = [e for e in r['Severity']]
distance = [e for e in r['Distance(mi)']]
latitude = [e for e in r['Start_Lat']]
longitude = [e for e in r['Start_Lng']]
rl = []
rl.insert(0, ['Index','Severity','Distance(mi)'])
loc = []
loc.insert(0,['Index','Start_Lat','Start_Lng'])
index = 1
for i in range(len(severity)):
    if severity[i] == 0:
        continue 
    elif distance[i] < 0.00:
        continue
    else:
        rl.append([str(index),severity[i],distance[i]])
        index+=1
index = 1     
for i in range(len(latitude)):
    loc.append([index,latitude[i],longitude[i]])
    index+=1
    
graph_loc = [[0 for j in range((int(max(longitude)-min(longitude))*10)+1)]for i in range((int(max(latitude)-min(latitude))*10)+1)]
graph_loc = np.array(graph_loc)
#TO store latitude = int((max(latitude)-min(latitude))/0.5)
graph = [[0 for j in range(int(max(distance)//5)+1)] for i in range(int(max(severity)//.5))]
graph = np.array(graph)

for i in range(1,len(rl)):
    s = (rl[i][1])
    d = (rl[i][2])
    s = int(max((s//0.5) -1 , 0))
    d = int(d//5)
    graph[s,d] += 1

min_lat = min(latitude)
min_log = min(longitude)
for i in range(1,len(loc)):
    lat = (loc[i][1])
    log = (loc[i][2])
    lat = max(int((lat - min_lat)/0.1)-1,0)
    log = max(int((log - min_log)/0.1)-1,0)
    graph_loc[lat,log] += 1
    
fig,ax = plt.subplots()
ax.set_ylabel('Severity')
ax.set_xlabel('Distance (mi)')
for i in range(len(graph)):
    for j in range(len(graph[i])):
        r_s = (i+1) //2
        r_d = (j-1) * 5
        if graph[i,j] == 0:
            continue
        else:
            ax.scatter(r_d,r_s,s=max(int((graph[i,j] /len(distance))*100),1))
plt.show()

fig,ax = plt.subplots()
ax.set_ylabel('Latitude')
ax.set_xlabel('Longitude')
for i in range(len(graph_loc)):
    for j in range(len(graph_loc[i])):
        r_lat = ((i+1)*0.1)+min_lat
        r_log = ((j+1)*0.1)+min_log
        if graph_loc[i,j] == 0:
            continue
        else:
            ax.scatter(r_log,r_lat,s=max(int((graph_loc[i,j] /len(latitude))*100),3))
plt.show()