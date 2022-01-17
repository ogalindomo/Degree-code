import matplotlib.pyplot as plt
import numpy as np
from skimage.segmentation import felzenszwalb, slic, quickshift, watershed, active_contour

def count_coins(img):
    return np.amax(felzenszwalb(img, scale=10000, sigma=0, min_size=40000))

if __name__ == "__main__":
    plt.close('all')
    src = '/Users/oscargalindo/Desktop/Classes/CS 5363/Tests/coins'
    files = ['coins_2.jpg', 'coins_3.jpg', 'coins_4.jpg']

    for file in files:
        img = plt.imread(file)
        plt.figure()
        plt.imshow(img)
        n = count_coins(img)
        print('The image in file',file,'contains',n,'coins')

'''
The image in file coins_2.jpg contains 2 coins
The image in file coins_3.jpg contains 3 coins
The image in file coins_4.jpg contains 4 coins
'''

