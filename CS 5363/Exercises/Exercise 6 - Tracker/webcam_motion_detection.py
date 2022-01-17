import matplotlib.pyplot as plt
import numpy as np
import cv2
import time

out_dir = 'C:\\Users\\OFuentes\\Documents\\Research\\Vision\\motion\\frames\\'
cap = cv2.VideoCapture(0)
cap.set(3,1280)
cap.set(4,720)
start = time.time()
count, frame_count = 0,0
thr = 3.0
max_frames = 500

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('output1.mp4',fourcc, 20.0, (1280,720))

for i in range(10): # Discard first few frames
    ret, frame = cap.read()

float_frame = np.float32(frame)

while(True):
    count+=1
    old_frame = float_frame
    ret, frame = cap.read()
    cv2.imshow('frame',frame)
    float_frame = np.float32(frame)
    diff = np.mean(np.abs(float_frame-old_frame))

    if diff > thr:
        frame_count+=1
        # plt.imsave(out_dir+'frame'+str(1000+frame_count)[1:]+'.jpg',frame[:,:,::-1])
        
        print('saved frame',frame_count)
        out.write(frame)
        # if frame_count>=max_frames:
        #     break

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

elapsed_time = time.time()-start
print('Capture speed: {:.2f} frames per second'.format(count/elapsed_time))
print('Frames saved: {}'.format(frame_count))
cap.release()
out.release()
cv2.destroyAllWindows()

