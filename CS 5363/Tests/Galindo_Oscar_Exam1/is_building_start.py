import matplotlib.pyplot as plt
import numpy as np
from scipy import signal

def histogram_of_gradients(img,bins=12):
    hog = []
    gray_conv = np.array([0.2989,0.5870,0.1140]).reshape(1,1,3)
    im = np.sum(img*gray_conv,axis=2)
    f1 = np.array([[-1,0,1],[-2,0,2],[-1,0,1]])
    gh = signal.correlate2d(im, f1, mode='same')
    gv = signal.correlate2d(im, f1.T, mode='same')
    g_mag = np.sqrt(gv**2+gh**2)
    g_dir = np.arctan2(gv,gh)
    bin_size = 2*np.pi/bins
    g_dir_bin = ((g_dir+np.pi+bin_size/2)/bin_size).astype(np.int)%bins
    for i in range(bins):
        hog.append(np.sum(g_mag[g_dir_bin==i]))
    return np.array(hog)/im.shape[0]/im.shape[1]

if __name__ == "__main__":
    plt.close('all')

    files = ['new york.jpg', 'toronto.jpg', 'buildings.jpg','toronto3.jpg']
    files = files+['landscape1.jpg','landscape2.jpg','landscape3.jpg','landscape4.jpg']
    bins = 8
    for file in files:
        img = plt.imread(file)
        hog = histogram_of_gradients(img,bins=bins)
        man_angles = np.sum(hog[0::2],axis=0)
        non_man_angles = np.sum(hog[1::2],axis=0)
        if(man_angles > 2*non_man_angles):
            print(f"Man made shape is {file}")
        fig, ax = plt.subplots(2,figsize=(8,8))
        ax[0].imshow(img)
        ax[1].plot(np.arange(bins)*360/bins,hog)
        ax[1].set_ylim([0,np.amax(hog)*1.1])
        


'''
Output:
Image new york.jpg contains buildings
Image toronto.jpg contains buildings
Image buildings.jpg contains buildings
Image toronto3.jpg contains buildings
Image landscape1.jpg contains a nature scene
Image landscape2.jpg contains a nature scene
Image landscape3.jpg contains a nature scene
Image landscape4.jpg contains a nature scene
'''