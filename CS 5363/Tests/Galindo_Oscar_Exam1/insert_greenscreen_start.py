import matplotlib.pyplot as plt
import numpy as np
import cv2
import sys

def place(src,target,r,c):
    share_green = src[:,:,1] / (np.sum(src,axis=2))
    sheep = src.copy()
    sheep[share_green > 0.4,:] = 0
    area = target[r:r+src.shape[0],c:c+src.shape[1]].copy()
    area[share_green <= 0.4,:] = 0
    result = target.copy()
    result[r:r+src.shape[0],c:c+src.shape[1]] = area + sheep
    plt.imshow(result[:,:,::-1].astype(np.uint8))
    return result.astype(np.uint8)

if __name__ == "__main__":
    plt.close('all')

    img = cv2.imread("lawn3.jpeg")
    video = cv2.VideoCapture('alpaca_scaled.avi')
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter('composite.mp4',fourcc, 20.0, (img.shape[1],img.shape[0]))

    if not video.isOpened():  # Exit if video not opened.
        print("Could not open video")
        sys.exit()

    plt.figure(1)
    # Click on position where alpaca should appear
    plt.imshow(img[:,:,::-1])
    p = plt.ginput()
    c0,r0 = int(p[0][0]+.5), int(p[0][1]+.5)
    plt.close(1)

    # Read first frame
    ok, frame = video.read()
    height, width,  =  frame.shape[0], frame.shape[1]

    c,r = p[0]
    c,r = int(c),int(r)
    while True:
        ok, frame = video.read()
        if not ok:
            break
        
        result = place(frame,img,r,c)

        cv2.imshow("Composite", img)
        cv2.imshow("Video", frame)

        # Generate composite frame

        out.write(result)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


    out.release()
    video.release()
    cv2.destroyAllWindows()
