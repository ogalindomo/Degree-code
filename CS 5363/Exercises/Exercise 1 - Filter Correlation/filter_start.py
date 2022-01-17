from scipy import signal
import numpy as np
import matplotlib.pyplot as plt
import os
import matplotlib.image as mpimg


def show_image(image,title='',save_im=False,filename=None):
    # Display image in new window
    fig, ax = plt.subplots()
    ax.imshow(image,cmap='gray')
    ax.axis('off')
    ax.set_title(title)
    if save_im:
        if filename==None:
            filename=title
        fig.savefig(filename+'.jpg',bbox_inches='tight', pad_inches=0.1)
    return fig, ax

def sub_image(I,r0,c0,rows,cols):
    return I[r0:r0+rows,c0:c0+cols]

def correlate2d(image,filt):
    if len(image.shape) == 2:
        r,c = filt.shape
        result = np.zeros((image.shape[0]-r + 1, image.shape[1]-c + 1))
        for i in range(result.shape[0]):
            for j in range(result.shape[1]):
                result[i,j] = np.sum(image[i:i+r,j:j+c]*filt) # Dot product of image region and filter
        return result
    else:
        r,c = filt.shape
        result = np.zeros((image.shape[0]-r + 1, image.shape[1]-c + 1, 3))
        for i in range(result.shape[0]):
            for j in range(result.shape[1]):
                for channel in range(image.shape[2]):
                    result[i,j,channel] = np.sum(image[i:i+r,j:j+c,channel]*filt) # Dot product of image region and filter
        result = result/255
        return result.astype(np.float32)

def gaussian_filter(size, sigma):
    d = ((np.arange(size) - (size-1)/2)**2).reshape(-1,1)
    f = np.exp(-(d+d.T)/2/sigma/sigma)
    return f/np.sum(f)

def correlate2d_scipy(image,filt):
    if len(image.shape) == 2:
        return signal.correlate2d(image, filt,mode='valid')
    else:
        r,c = filt.shape
        img = np.zeros((image.shape[0]-r + 1, image.shape[1]-c + 1, 3))
        for channel in range(image.shape[2]):
            img[...,channel] = signal.correlate2d(image[...,channel], filt,mode='valid')
        return (img/255).astype(np.float32)
    
def edge_finding(img):
    filt = np.array([[-1,0,1],[-2,0,2],[-1,0,1]])
    v_e = correlate2d_scipy(img, filt)
    h_e = correlate2d_scipy(img, filt.T)
    r,c = filt.shape
    image = np.zeros((img.shape[0]-r + 1, img.shape[1]-c + 1, 3))
    for channel in range(img.shape[2]):
        image[...,channel] = ((np.power(v_e[...,channel],2)+np.power(h_e[...,channel],2)))
    return np.sqrt(np.sum(image,axis=2))
    
if __name__ == "__main__":
    plt.close("all")

    image = mpimg.imread('eiffel.jpg').astype(np.float32)
    # image = np.mean(image,axis=2)
    
    f1 = np.array([[-1,0,1],[-2,0,2],[-1,0,1]])
    f2 = f1.T
    # f3 = np.ones((3,3))/9
    f3 = gaussian_filter(3, sigma=0.85)
    f4 = np.zeros((3,3))
    f4[1,1]=1
    f5 = 2*f4-f3
    f6 = gaussian_filter(15, 3)
    titles=['Filter','Result','Close-up']
    k=1
    for f in [f1,f2,f3,f4,f5,f6]:
        print(f)
        print(np.sum(f))
        image_f = correlate2d_scipy(image,f)
        # image_f = correlate2d(image,f)
        show_image(image_f)
        show_image(sub_image(image_f,62,325,50,25))
        k+=1
    show_image(edge_finding(image))
    show_image(sub_image(edge_finding(image),62,325,50,25))