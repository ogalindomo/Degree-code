import numpy as np
import cv2
import time
import matplotlib.pyplot as plt

cap = cv2.VideoCapture(0)
cap.set(3,1280)
cap.set(4,720)
start = time.time()
count=0

while(True):
    ret, frame = cap.read()
    count+=1

    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

elapsed_time = time.time()-start
print('Capture speed: {:.2f} frames per second'.format(count/elapsed_time))
cap.release()
cv2.destroyAllWindows()

plt.imsave('frame.jpg',frame[:,:,::-1])

