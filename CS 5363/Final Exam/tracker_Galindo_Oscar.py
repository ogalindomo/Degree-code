import matplotlib.pyplot as plt
import numpy as np
import cv2
import time
import sys

if __name__ == '__main__' :
    path = ''

    tracker_types = ['Boosting', 'MIL','KCF', 'TLD', 'MEDIANFLOW', 'CSRT']
    tracker_type = tracker_types[-1]

    exec('tracker = cv2.Tracker'+tracker_type+'_create()')
    print('Using',tracker_type,'tracker')

    # Read video
    video = cv2.VideoCapture(path+'tesvor1.avi')

    # Exit if video not opened.
    if not video.isOpened():
        print("Could not open video")
        sys.exit()

    # Read first frame.
    ok, frame = video.read()
    if not ok:
        print('Cannot read video file')
        sys.exit()

    # Define an initial bounding box
    bbox = (163, 339, 132, 111)

    # Uncomment this to change the box
    #bbox = cv2.selectROI("Select ROI",frame, False)
    #cv2.destroyWindow("Select ROI")

    # Initialize tracker with first frame and bounding box
    ok = tracker.init(frame, bbox)

    count = 0
    start = time.time()
    counter = np.zeros((frame.shape[0],frame.shape[1]),dtype=int)
    while True:
        # Read a new frame
        ok, frame = video.read()
        if not ok:
            break
        count+=1
        # Start timer
        timer = cv2.getTickCount()

        # Update tracker
        ok, bbox = tracker.update(frame)
        
        

        # Calculate Frames per second (FPS)
        fps = cv2.getTickFrequency() / (cv2.getTickCount() - timer);

        # Draw bounding box
        if ok:
            # Tracking success
            p1 = (int(bbox[0]), int(bbox[1]))
            p2 = (int(bbox[0] + bbox[2]), int(bbox[1] + bbox[3]))

            cv2.rectangle(frame, p1, p2, (255,0,0), 2, 1)
            
            counter[p1[1]:p2[1],p1[0]:p2[0]]+=1

            #count[int(bbox[0]):]
        else :
            # Tracking failure
            cv2.putText(frame, "Tracking failure detected", (100,80), cv2.FONT_HERSHEY_SIMPLEX, 0.75,(0,0,255),2)

        # Display tracker type on frame
        cv2.putText(frame, tracker_type + " Tracker", (100,20), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (50,170,50),2);

        # Display FPS on frame
        cv2.putText(frame, "FPS : " + str(int(fps)), (100,50), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (50,170,50), 2);

        # Display result
        cv2.imshow("Tracking", frame)

        # Exit if ESC pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        

elapsed_time = time.time()-start
print(tracker_type, 'processing speed: {:.2f} frames per second'.format(count/elapsed_time))

video.release()
cv2.destroyAllWindows()


plt.close('all')
plt.imshow(counter)

