import matplotlib.pyplot as plt
import numpy as np
import cv2
import time

cap = cv2.VideoCapture(0)
cap.set(3,1280)
cap.set(4,720)
start = time.time()
count=0

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('output1.mp4',fourcc, 20.0, (1280,720))

while(True):
    ret, frame = cap.read()
    count+=1
    out.write(frame)

    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

elapsed_time = time.time()-start
print('Capture speed: {:.2f} frames per second'.format(count/elapsed_time))
cap.release()
out.release()
cv2.destroyAllWindows()

