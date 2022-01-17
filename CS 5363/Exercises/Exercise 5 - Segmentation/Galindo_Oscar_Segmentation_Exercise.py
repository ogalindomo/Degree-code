import matplotlib.pyplot as plt
import numpy as np
from skimage.data import astronaut
from skimage.color import rgb2gray
from skimage.filters import sobel
from skimage.segmentation import felzenszwalb, slic, quickshift, watershed, active_contour
from skimage.segmentation import mark_boundaries
from skimage.util import img_as_float
from skimage.filters import gaussian
import time 

def mean_region_colors(img,seg):
    cmap = np.zeros((np.amax(seg)+1,3),dtype=np.float32)
    for i in range(cmap.shape[0]):
        m = img[seg==i]
        if len(m)>0:
            cmap[i] = np.mean(m,axis=0)
    return cmap

def indexed_to_rgb(seg,cmap=[]):
    if len(cmap)==0:
        cmap = np.random.random((np.amax(seg)+1,3))
    rows,cols = seg.shape
    img=np.zeros((rows,cols,3),dtype=np.float32)
    for r in range(rows):
        for c in range(cols):
            img[r,c] = cmap[seg[r,c]]
    return img

def show_images(images,titles=None,fig_title='',save_im=True,filename=None):
    if titles==None:
        titles = ['' for i in range(len(images))]
    # Display image in new window
    fig, ax = plt.subplots(1,len(images),figsize=(12, 4))
    fig.suptitle(fig_title)
    for i in range(len(images)):
        ax[i].imshow(images[i],cmap='gray')
        ax[i].axis('off')
        ax[i].set_title(titles[i])
    if save_im:
        if filename==None:
            filename='show_images'
        fig.savefig(filename+'.jpg',bbox_inches='tight', pad_inches=0.1,dpi=200)
        plt.show()
    fig.savefig(fig_title+".jpg")
    return fig, ax

if __name__ == "__main__":
    algorithms =  ['Felzenszwalb']#,'Quickshift','SLIC','Watershed']
    algorithm = algorithms[0]
    plt.close('all')
    image_dir = ''

    # img = plt.imread(image_dir+'cars750.jpg')

    img = plt.imread('frame.jpg')
    img = img/np.amax(img)
    for i in range(len(algorithms)):
        algorithm = algorithms[i]
        print('Running',algorithm,'segmentation')
        if algorithm == 'Felzenszwalb':
            start = time.time()
            segments = felzenszwalb(img, scale=100, sigma=3, min_size=50)
            print("Result",str(time.time()-start))
        elif algorithm == 'Quickshift':
            segments = quickshift(img.astype(np.float64), kernel_size=11, max_dist=np.amax(img.shape), ratio=50, sigma=3)
        elif algorithm == 'SLIC':
            segments = slic(img, n_segments=250, compactness=5, sigma=10, start_label=0)
        else:
            gradient = sobel(rgb2gray(img))
            segments = watershed(gradient, markers=50)
    
        num_regions = np.amax(segments)+1
        print(algorithm, 'number of regions found:',num_regions)
    
        if num_regions<1000:
            cmap = mean_region_colors(img,segments)
            images = [img, indexed_to_rgb(segments),indexed_to_rgb(segments,cmap)]
            titles = ['Original image','Regions with random color','Regions with mean color']
            show_images(images,titles,fig_title=algorithm+' segmentation', save_im=True)
            points = np.asarray(plt.ginput(n=3,timeout=0)) 
            points = points.astype(np.float32)
            g = gaussian(images[0],sigma=15,multichannel=True)
            for point in range((points.shape[0])):
                c,r = int(points[point,0]),int(points[point,1])
                print(r,c)
                value = (segments[r,c])
                print(value)
                g[segments==value] = img[segments==value]
            f,a = plt.subplots()
            a.imshow(g)
            f.savefig("teams-blurr.jpg")
                
        else:
            print('Too many regions to display!')

    