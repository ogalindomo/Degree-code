# Simple program to read images dataset

import numpy as np
import matplotlib.pyplot as plt
import utils
from scipy.stats import rankdata
import cv2 as cv 

data_dir = './' # Use your own path here
data_files =  ['image_set_ag.npz','image_set_gl.npz','image_set_mc.npz']

plt.close('all')

def show_image(image,title='',save_im=True,filename=None):
    # Display image in new window
    fig, ax = plt.subplots()
    ax.imshow(image,cmap='gray')
    ax.axis('off')
    ax.set_title(title)
    if save_im:
        if filename==None:
            filename=title
        fig.savefig(filename+'.png',bbox_inches='tight', pad_inches=0.1,dpi=200)
    return fig, ax
    
def compute_integral(img):
    integral = np.zeros((img.shape[0]+1,img.shape[1]+1))
    if len(img.shape) == 2:
        integral[1:,1:] = img
    else:
        integral[1:,1:] = np.mean(img,axis=2)
    integral = np.cumsum(np.cumsum(integral,axis=0),axis=1)
    return integral

def compute_brightest_area(img,l,w):
    integral = compute_integral(img)
    brightest = np.zeros((integral.shape[0]-l,integral.shape[1]-w))
    brightest = integral[l:,w:] + integral[:integral.shape[0]-l,:integral.shape[1]-w] - integral[l:,:integral.shape[1]-w] - integral[:integral.shape[0]-l,w:]
    y,x = np.unravel_index(np.argmax(brightest, axis=None), brightest.shape)
    x = [x,x,x+w,x+w,x] 
    y = [y,y+l,y+l,y,y]
    return x,y

def select_best(dataset):
    elements = {}
    fractions = []
    for img in range(len(dataset)):
        x,y = compute_brightest_area(dataset[img],80,80)
        c,r = x[0],y[0]
        sub_image_sum = np.sum(dataset[img,r:r+80,c:c+80])
        x,y = compute_brightest_area(dataset[img,r:r+80,c:c+80],40,40)
        c,r = x[0],y[0]
        smaller_sum = np.sum(dataset[img,r:r+40,c:c+40])
        x,y = compute_brightest_area(dataset[img,r:r+40,c:c+40],20,20)
        c,r = x[0],y[0]
        focus = np.sum(dataset[img,r:r+20,c:c+20])
        result = focus/smaller_sum/sub_image_sum
        elements[result] = img
        fractions.append(result)
    return fractions,elements

def equalize_historgram(img):
    im_h = rankdata(img.reshape(-1),method='max').reshape(img.shape)
    im_h = im_h/np.amax(im_h)
    return im_h

def gamma_correction(img,gamma):
    return img**gamma

def log_correction(img,k=1):
    return np.log((img**k)+1)/np.log(k+1)

def sigmoid(img,k=1):
    img = 1/(1 + np.exp(k*(0.5-img)))
    img = img-np.amin(img)
    img = img/np.amax(img)
    return img

def align(images, coordinates_average,size=100):
    print(images.shape)
    container = np.zeros((images.shape[1],images.shape[2]))
    x_avg,y_avg = coordinates_average
    print(coordinates_average)
    count=0
    for i in range(len(images)):
        x,y = compute_brightest_area(images[i],size,size)
        diff_x, diff_y = x_avg[0]-x[0],y_avg[0]-y[0]
        if diff_x == 0 : 
            diff_x -= 1
        if diff_y == 0: 
            diff_y -= 1
        if abs(diff_x) > 35 or abs(diff_y) > 35:
            continue
        if diff_x < 0 and diff_y < 0:
            container[:diff_y,:diff_x] += images[i,abs(diff_y):,abs(diff_x):]
            count+=1
        elif diff_x > 0 and diff_y > 0:
            container[diff_y:,diff_x:] += images[i,:-diff_y,:-diff_x]
            count+=1
        elif diff_x < 0 and diff_y > 0:
            container[diff_y:,:diff_x] += images[i,:-diff_y,abs(diff_x):]
            count+=1
        else: #diff_x >0 and diff_y < 0 
            container[:diff_y,diff_x:] += images[i,abs(diff_y):,:-diff_x]
            count+=1
    print(f'Aligned {count} Images')
    plt.show()
    return container/np.amax(container)

def get_collection(dataset):
    frac,elements = select_best(dataset)
    frac.sort(reverse=True)
    indeces = np.array([elements[value] for value in frac[0:size]])
    collection = dataset[indeces]
    return  collection
       
    
for d, data_file in enumerate(data_files):
    for size in [400]:#,400,600,1000]:
        if data_file == 'image_set_mc.npz': size+=600
        dataset = np.load(data_dir+data_file)['images']
        collection = get_collection(dataset)
        rand_choice = np.sort(np.random.randint(0,dataset.shape[0],3))
        image_list = [dataset[i] for i in rand_choice]
        titles = ['images[{}]'.format(i) for i in rand_choice]
        fig_title= 'Random images from '+data_file
        average = np.mean(dataset,axis=0)
        image_list.append(average)
        titles.append("Average")
        best = np.mean(collection,axis=0)
        image_list.append(best)
        titles.append("Best Images")
        utils.show_images(image_list, titles, fig_title) # Show some images
        ###################################################################
        image_list = []
        titles = []
        
        x_avg,y_avg = compute_brightest_area(average,10,10)
        log = log_correction(best)
        gamma = gamma_correction(log,4)
        container = (align(collection,(x_avg,y_avg),10))
        sig = sigmoid(container,2)
        
        titles.append('Brightest regions Average')
        titles.append('Brightest regions Best')
        titles.append('Log correction Best')
        titles.append('Histogram Equa. Best')
        image_list.append(average)
        image_list.append(best)
        image_list.append(log)
        image_list.append(gamma)
        fig_title = f'GroundTruths_{data_file}'
        utils.show_images(image_list, titles, fig_title)
        ####################################################################
        image_list = []
        titles = []

        titles.append('Aligned')
        titles.append('Aligned-Log')
        titles.append('Gamma-Log-Container')
        titles.append('Sigmoid')
        titles.append('Log-Sigmoid')
        image_list.append(container)
        image_list.append(log_correction(container,3))
        image_list.append(gamma_correction(log_correction(container),2))
        image_list.append(gamma)
        image_list.append(log_correction(sig))
        fig_title = f'Transformations_{data_file}'
        utils.show_images(image_list, titles, fig_title)
        #########################Extra Images###########################################
        show_image(average,f'Average_{data_file}')
        show_image(container,f'Aligned_{data_file}')
        show_image(log_correction(container), f'Aligned-Log_{data_file}')
        show_image(best, f'Best_{data_file}')
        show_image(sig, f'Sigmoid_{data_file}')
        plt.show()
    