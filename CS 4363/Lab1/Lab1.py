import numpy as np
import cv2 
import time

cap = cv2.VideoCapture(0)
start = time.time()
count=0

#Initial conditions for problems 5 & 7
'''
time_threshold = int(input('Please enter the amount of time you want to wait for a screenshot to be taken'))
time_interval = int(input('Please indicate the interval of time to keep taking pictures.'))
old_average = 0
capture_activated = False
time_start_capture = 0
'''

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
   
    count+=1
    #b = frame[:,:,0]
    #g = frame[:,:,1]
    #r = frame[:,:,2]
    unique = np.arange(256)
    counts = np.arange(256)
    unique, counts = np.unique(frame, return_counts=True)
    print(unique)
    print(counts)
    #order = dict(unique, counts)
    #grayscale = np.mean(frame,2)
    #igrayscale = grayscale.astype(int)
    #unique,counts = np.unique(igrayscale,return_counts = True)
    #
    
    '''
    n = 64;
    copy_f = frame/(256/n);
    copy_i = copy_f.astype(int)
    unique,counts = np.unique(copy_i,return_counts = True)
    print(unique)
    print(counts)'''
    #print(counts)
    #1 GrayScale Version (Average Method (R+G+B)/3)   
    
    grayscale = np.mean(frame,2)/255
    
    
    #2 Negative of GrayScale
    '''
    grayscale = np.mean(frame,2)/255
    grayscale = 1-grayscale
    '''
    
    
    #3 Mirrored color image
    '''
    frame = np.flip(frame,1)
    '''
    
    #4 Color image upside down
    '''
    frame = np.flip(frame,0)
    '''
    
    #5 Write to a file every n seconds 
    '''
    calc_time = time.time() - start
    if(int(calc_time - start) % time_threshold) == 0 :
        cv2.imwrite("frame%d.jpg" % count, frame)
    '''
    
    #6 Corrected version of grayscale
    '''
    grayscale = np.mean(frame,2)/255
    grayscale_max = np.max(grayscale)
    grayscale_min = np.min(grayscale)
    grayscale = (grayscale-grayscale_min)/(grayscale_max - grayscale_min)
    '''
    
    #7 Motion Dectector 
    '''
    new_average = np.average(frame)
    abs_difference = np.abs(old_average - new_average)
    
    if old_average == 0:
        old_average = new_average
    elif abs_difference > 5:
        capture_activated = True
        time_start_capture = time.time()
    current_time = time.time()    
    if capture_activated and (current_time - time_start_capture) <= time_interval:
        if(int(current_time - time_start_capture) % time_threshold == 0):
            cv2.imwrite("frame%d.jpg" % int(np.abs(old_average - new_average)), frame)
    elif (current_time - time_start_capture) > time_interval:
        capture_activated = False
        
    print('Average {0:.2f}'.format(np.abs(new_average - old_average)))
    old_average = new_average
    '''
    #Extra Credit Ghostly Figure
    
        
    
    # Display the resulting frame
    cv2.imshow('Camera',frame)
    #cv2.imshow('Camera', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
    #if count%30==0:
       # print(np.max(frame),np.min(frame))
    
    
elapsed_time = time.time()-start
print('Capture speed: {0:.2f} frames per second'.format(count/elapsed_time))   

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()