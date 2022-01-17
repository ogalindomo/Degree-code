import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from skimage import transform as tf
from matplotlib import transforms
import cv2
import os

def display_control_lines(im0,im1,pts0,pts1,clr_str = 'rgbycmwk'):
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

def cond_num_and_det(H):
    # Very large condition numbers usually indicate a bad homography
    # Negative determinants and those with low absolute values usually indicate a bad homography
    # Large determinant also usually indicate a bad homography
    w,v = np.linalg.eig(np.array(H.params))
    w = np.sort(np.abs(w))
    cn = w[2]/w[0]
    d = np.linalg.det(H.params)
    return cn, d
    print('condition number {:7.3f}, determinant {:7.3f}'.format(cn,d))

def homography_error(H,pts1,pts2):
    pts1 =  np.hstack((pts1,np.ones((pts1.shape[0],1))))
    pts2 =  np.hstack((pts2,np.ones((pts2.shape[0],1))))
    proj = np.matmul(H,pts1.T).T
    proj = proj/proj[:,2].reshape(-1,1)
    err = proj[:,:2] - pts2[:,:2]
    return np.mean(np.sqrt(np.sum(err**2,axis=1)))

def select_matches_ransac(pts0, pts1):
    H, mask = cv2.findHomography(pts0.reshape(-1,1,2), pts1.reshape(-1,1,2), cv2.RANSAC,5.0)
    choice = np.where(mask.reshape(-1) ==1)[0]
    return pts0[choice], pts1[choice]

# def random_select(p1,p2):
#     type(p1)
#     type(p2)
#     selection = np.random.permutation(p1.shape[0])
#     selection = selection[:selection.shape[0]//2]
#     error = homography_error(tf.ProjectiveTransform().estimate(p1,p2), p1, p2)
#     pt1,pt2=None,None
#     for _ in range(10):
#         H = tf.ProjectiveTransform()
#         H.estimate(keypoints1, keypoints2)
#         if error > homography_error(H, p1[selection], p2[selection]):
#            pt1,pt2 = p1[selection], p2[selection] 
#     return pt1,pt2
        
    
    

if __name__ == "__main__":
    # An ORB feature consists of a keypoint (the coordinates of the region's center) and a descriptor (a binary vector of length 256 that characterizes the region)
    plt.close('all')

    img1 = mpimg.imread('/Users/oscargalindo/Downloads/a512bbf27f112d69e11ac8dfd2392c01.jpg')
    img2 = mpimg.imread('/Users/oscargalindo/Downloads/practice exam images/q7_b.jpg')

    orb = cv2.ORB_create()

    fig, ax = plt.subplots(ncols=2)
    keypoints1, descriptors1 = orb.detectAndCompute(img1,mask=None)
    ax[0].imshow(cv2.drawKeypoints(img1, keypoints1, None, color=(0,255,0), flags=0))

    keypoints2, descriptors2 = orb.detectAndCompute(img2,mask=None)
    ax[1].imshow(cv2.drawKeypoints(img2, keypoints2, None, color=(0,255,0), flags=0))

    # Create BFMatcher object
    matcher = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
    matches = matcher.match(descriptors1,descriptors2)

    # Extract data from orb objects and matcher
    dist = np.array([m.distance for m in matches])
    ind1 = np.array([m.queryIdx for m in matches])
    ind2 = np.array([m.trainIdx for m in matches])
    keypoints1 = np.array([p.pt for p in keypoints1])
    keypoints2 = np.array([p.pt for p in keypoints2])
    keypoints1 = keypoints1[ind1]
    keypoints2 = keypoints2[ind2]
    # keypoints1[i] and keypoints2[i] are a match

    print('Original number of matches',keypoints1.shape[0])
    H = tf.ProjectiveTransform()
    H.estimate(keypoints1, keypoints2)
    print('Resulting homography\n',H.params)
    cn,d = cond_num_and_det(H)
    print('condition number: {:7.3f}, determinant: {:7.3f}'.format(cn,d))
    print('Mean projection error {:7.3f}'.format(homography_error(H.params,keypoints1, keypoints2)))

    keypoints1, keypoints2 = select_matches_ransac(keypoints1, keypoints2)
    # keypoints1, keypoints2 = random_select(keypoints1, keypoints2)
    

    print('Number of matches after performing RANSAC',keypoints1.shape[0])
    H.estimate(keypoints1, keypoints2)
    print('Resulting homography\n',H.params)
    cn,d = cond_num_and_det(H)
    print('condition number: {:7.3f}, determinant: {:7.3f}'.format(cn,d))

    display_control_lines(img1,img2, keypoints1, keypoints2)

    print('Mean projection error {:7.3f}'.format(homography_error(H.params,keypoints1, keypoints2)))
    
    # for image in os.listdir('./img'):
    #     img1 = mpimg.imread('./img/'+image)
    #     key1, descriptors1 = orb.detectAndCompute(img1,mask=None)
    #     point_num = 0
    #     max_name = ''
    #     k1,k2 = None,None
    #     for image_j in os.listdir('./img'):
    #         if image == image_j: continue
    #         img2 = mpimg.imread('./img/'+image_j)
    #         keypoints2, descriptors2 = orb.detectAndCompute(img2,mask=None)
    #         matcher = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
    #         matches = matcher.match(descriptors1,descriptors2)
        
    #         # Extract data from orb objects and matcher
    #         dist = np.array([m.distance for m in matches])
    #         ind1 = np.array([m.queryIdx for m in matches])
    #         ind2 = np.array([m.trainIdx for m in matches])
    #         keypoints1 = np.array([p.pt for p in key1])
    #         keypoints2 = np.array([p.pt for p in keypoints2])
    #         keypoints1 = keypoints1[ind1]
    #         keypoints2 = keypoints2[ind2]
    #         keypoints1, keypoints2 = select_matches_ransac(keypoints1, keypoints2)
    #         if keypoints1.shape[0] > point_num:
    #             max_name = image_j
    #             k1,k2 = keypoints1,keypoints2
    #             point_num = keypoints1.shape[0]
        
    #     img2 = mpimg.imread('./img/'+max_name)
    #     display_control_lines(img1,img2 , k1, k2)
    #     plt.show()
