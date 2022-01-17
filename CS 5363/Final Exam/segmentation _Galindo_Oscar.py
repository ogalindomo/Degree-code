import matplotlib.pyplot as plt
import numpy as np
import os
from skimage.data import astronaut
from skimage.color import rgb2gray
from skimage.filters import sobel
from skimage.segmentation import felzenszwalb, slic, quickshift, watershed, active_contour
from skimage.segmentation import mark_boundaries
from skimage.util import img_as_float
from skimage.filters import gaussian

def show_images(images,titles=None,fig_title='', save_im=False,filename=None):
    if titles==None:
        titles = ['' for i in range(len(images))]
    # Display image in new window
    fig, ax = plt.subplots(1,len(images),figsize=(12, 4))
    for i in range(len(images)):
        ax[i].imshow(images[i],cmap='gray')
        ax[i].axis('off')
        ax[i].set_title(titles[i])
    fig.suptitle(fig_title, fontsize=16)
    if save_im:
        if filename==None:
            if fig_title!='':
                filename=fig_title
            else:
                filename='show_images'
        fig.savefig(filename+'.jpg',bbox_inches='tight', pad_inches=0.1)
    plt.tight_layout()
    return fig, ax

def mean_region_colors(img,seg):
    cmap = np.zeros((np.amax(seg)+1,3),dtype=np.float32)
    for i in range(cmap.shape[0]):
        m = img[seg==i]
        if len(m)>0:
            cmap[i] = np.mean(m,axis=0)
    return cmap

def indexed_to_rgb(seg,cmap=[]):
    if len(cmap)==0:
        cmap = np.float32(np.random.random((np.amax(seg)+1,3)))
    im = cmap[seg.reshape(-1)].reshape((seg.shape[0],seg.shape[1],3))
    return im

if __name__ == "__main__":
    algorithms =  ['Felzenszwalb']#,'Quickshift','SLIC','Watershed']
    # algorithm = algorithms[3]
    plt.close('all')

    img = plt.imread('horse.jpg')

    img = img/np.amax(img)

    # Find best algorithm and parameters
    for algorithm in algorithms:
        print('Running',algorithm,'segmentation')
        if algorithm == 'Felzenszwalb':
            segments = felzenszwalb(img, scale=1000, sigma=2, min_size=850)
        elif algorithm == 'Quickshift':
            segments = quickshift(img.astype(np.float64), kernel_size=11, max_dist=np.amax(img.shape), ratio=100, sigma=0)
        elif algorithm == 'SLIC':
            segments = slic(img, n_segments=100, compactness=5, sigma=0, start_label=0)
        else:
            gradient = sobel(rgb2gray(img))
            segments = watershed(gradient, markers=70)
    
        s = 0
        mean_intensity = 0
        for region in range(np.amax(segments)):
            modified = np.mean(img,axis=2)
            pixel_num = np.count_nonzero(segments == region)
            modified[segments!=region] = 0
            added_intensities = np.cumsum(np.cumsum(modified,axis=0),axis=1)
            added_intensities = added_intensities[-1,-1]
            if pixel_num>0:
                mean = (added_intensities/pixel_num)
                if mean > mean_intensity:
                    s = region
                    mean_intensity = mean
            
        print("Region found"+str(s))
        plt.imshow(segments==s,cmap='gray')
        #Part 3
        groundtruth = np.load('ground_truth_horse.npy')
        horse = segments==s
        intersection = np.logical_and(groundtruth,horse)
        count_intersection = np.count_nonzero(intersection)
        union = np.logical_or(groundtruth,horse)
        count_union = np.count_nonzero(union)
        print("IoU:"+str(count_intersection/count_union))
        ################################################
        num_regions = np.amax(segments)+1
        print(algorithm, 'number of regions found:',num_regions)
    
        if num_regions<1000:
            cmap = mean_region_colors(img,segments)
            # Find region with highest mean (closest to white)
            # Create binary image, pixels in white region are 1, others are 0
            white_image =  np.zeros((img.shape[0],img.shape[1]))
    
            images = [img, indexed_to_rgb(segments),indexed_to_rgb(segments,cmap),white_image,segments==segments[img.shape[0]//2,img.shape[1]//2],groundtruth]
            titles = ['Original image','Regions with random color','Regions with mean color','Binary segmentation','horse','groundtruth']
            show_images(images,titles,fig_title=algorithm+' segmentation', save_im=True)
        else:
            print('Too many regions to display!')






