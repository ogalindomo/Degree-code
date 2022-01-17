#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 11:38:08 2021

@author: oscargalindo
"""

import matplotlib.pyplot as plt
import numpy as np
import cv2
import time,sys

cap = cv2.VideoCapture(0)
cap.set(3,1280)
cap.set(4,720)
start = time.time()

for i in range(10): # Discard first few frames
    ret, frame = cap.read()
    
bbox = cv2.selectROI(frame, False)
tracker = cv2.TrackerMIL_create()
ok = tracker.init(frame, bbox)
count = 0
    
while(True):
    ret, frame = cap.read()

    cv2.imshow('Tracker',frame)
    timer = cv2.getTickCount()
    ok, bbox = tracker.update(frame)
    fps = cv2.getTickFrequency() / (cv2.getTickCount() - timer)
    if ok:
        # Tracking success
        p1 = (int(bbox[0]), int(bbox[1]))
        p2 = (int(bbox[0] + bbox[2]), int(bbox[1] + bbox[3]))
        cv2.rectangle(frame, p1, p2, (255,0,0), 2, 1)
    else :
        # Tracking failure
        cv2.putText(frame, "Tracking failure detected", (100,80), cv2.FONT_HERSHEY_SIMPLEX, 0.75,(0,0,255),2)

    # Display tracker type on frame
    cv2.putText(frame, 'MIL' + " Tracker", (100,20), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (50,170,50),2);

    # Display FPS on frame
    cv2.putText(frame, "FPS : " + str(int(fps)), (100,50), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (50,170,50), 2);

    # Display result
    cv2.imshow("Tracking", frame)

    # Exit if ESC pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()