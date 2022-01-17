import numpy as np
import matplotlib.pyplot as plt
from skimage import transform as tf
from matplotlib import transforms
import cv2

def display_correspondences(im0,im1,pts0,pts1,clr_str = 'rgbycmwk'):
    canvas_shape = (max(im0.shape[0],im1.shape[0]),im0.shape[1]+im1.shape[1],3)
    canvas = np.zeros(canvas_shape,dtype=type(im0[0,0,0]))
    canvas[:im0.shape[0],:im0.shape[1]] = im0
    canvas[:im1.shape[0],im0.shape[1]:canvas.shape[1]]= im1
    fig, ax = plt.subplots(figsize=(8, 4))
    ax.imshow(canvas)
    ax.axis('off')
    pts2 = pts1+np.array([im0.shape[1],0])
    for i in range(pts0.shape[0]):
        ax.plot([pts0[i,0],pts2[i,0]],[pts0[i,1],pts2[i,1]],color=clr_str[i%len(clr_str)],linewidth=1.0)
    fig.suptitle('Point correpondences', fontsize=16)
    
def select_matches_ransac(pts0, pts1):
    # print(pts0, pts1)
    print(pts0.shape)
    print(pts0.reshape(-1,1,2))
    print(pts0.shape)
    H, mask = cv2.findHomography(pts0.reshape(-1,1,2), pts1.reshape(-1,1,2), cv2.RANSAC,5.0)
    choice = np.where(mask.reshape(-1) ==1)[0]
    return pts0[choice], pts1[choice]

if __name__ == "__main__":

    plt.close('all')
    model = plt.imread('stop_model.jpg')

    orb = cv2.ORB_create()

    keypoints1, descriptors1 = orb.detectAndCompute(model,mask=None)
    keypoints1 = np.array([p.pt for p in keypoints1])

    f = [2,3,6,7,9,11,12,15] # Work for stop_model.jpg

    files = ['stop'+str(i)+'.jpg' for i in f]

    for file in  files:
        img = plt.imread(file)

        keypoints2, descriptors2 = orb.detectAndCompute(img,mask=None)
        keypoints2 = np.array([p.pt for p in keypoints2])

        matcher = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
        matches = matcher.match(descriptors1,descriptors2)

        # Extract data from orb objects and matcher
        dist = np.array([m.distance for m in matches])
        ind1 = np.array([m.queryIdx for m in matches])
        ind2 = np.array([m.trainIdx for m in matches])
        

        keypoints_match1 = keypoints1[ind1]
        keypoints_match2 = keypoints2[ind2]
        
        keypoints_match1, keypoints_match2 = select_matches_ransac(keypoints_match1, keypoints_match2)

        print('Original number of matches',keypoints_match1.shape[0])
        H = tf.ProjectiveTransform()
        H.estimate(keypoints_match1, keypoints_match2)
        display_correspondences(model,img,keypoints_match1, keypoints_match2)

        # Display stop sign using inverse warp
        warped = tf.warp(img, H, output_shape=(model.shape[0],model.shape[1]))
        plt.figure()
        plt.imshow(warped)

