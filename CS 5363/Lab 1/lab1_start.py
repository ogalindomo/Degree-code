import numpy as np
import matplotlib.pyplot as plt
import os
import matplotlib.image as mpimg

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

def show_images(images,titles=None,save_im=True,filename=None):
    if titles==None:
        titles = ['' for i in range(len(images))]
    # Display image in new window
    fig, ax = plt.subplots(1,len(images),figsize=(12, 4))
    for i in range(len(images)):
        ax[i].imshow(images[i],cmap='gray')
        ax[i].axis('off')
        ax[i].set_title(titles[i])
    if save_im:
        if filename==None:
            filename='show_images'
        fig.savefig(filename+'.jpg',bbox_inches='tight', pad_inches=0.1,dpi=200)
    return fig, ax

def color_index(image,index):
    if index == 0:
        return 2*image[:,:,0] - (image[:,:,1]+image[:,:,2])
    elif index == 1:
        return 2*image[:,:,1] - (image[:,:,2]+image[:,:,0])
    else:
        return 2*image[:,:,2] - (image[:,:,0]+image[:,:,1])

def get_channels(image):
    return [image[:,:,0], image[:,:,1], image[:,:,2]]

def subsample(image,r,c):
    return image[::2,::2]

def gray_level(image):
    return 0.299*image[:,:,0]+0.587*image[:,:,1]+0.114*image[:,:,2]

def negative_gray_level(image):
    return np.absolute(1-(0.299*image[:,:,0]+0.587*image[:,:,1]+0.114*image[:,:,2]))

def vert_edges(gray_image):
    right = np.copy(gray_image)
    right[:,:-1] = right[:,1:]
    right[:,-1] = 0
    return (gray_image-right)

def hor_edges(gray_image):
    right = np.copy(gray_image)
    right[:-1] = right[1:]
    right[-1,:] = 0
    return (gray_image-right)

def mirror(image):
    return image[:,::-1]

def upside_down(image):
    return image[::-1]

def brightest_region(image,reg_rows,reg_cols):
    if len(image.shape) > 2:
        sum_img = np.zeros((image.shape[0]+1,image.shape[1]+1,image.shape[2]))
        result = np.zeros((image.shape[0],image.shape[1],image.shape[2]))
    else: 
        sum_img = np.zeros((image.shape[0]+1,image.shape[1]+1))
        result = np.zeros((image.shape[0],image.shape[1]))
    sum_img[1:,1:] = image
    sum_img = np.cumsum(np.cumsum(sum_img,axis=1),axis=0)
    result = sum_img[:image.shape[0]-reg_rows+1,:image.shape[1]-reg_cols+1]+sum_img[reg_rows:,reg_cols:]- sum_img[reg_rows:,:image.shape[1]-reg_cols+1] - sum_img[:image.shape[0]-reg_rows+1,reg_cols:]
    if len(result.shape) > 2: result = np.mean(result,axis=2)  
    y,x = np.unravel_index(np.argmax(result, axis=None), result.shape)
    print(x,y)
    x = [x,x,x+reg_cols,x+reg_cols,x]
    y = [y,y+reg_rows,y+reg_rows,y,y]
    return x,y,result

if __name__ == "__main__":

    plt.close("all")
    image_dir = '/Users/oscargalindo/Desktop/Classes/CS 5363/Lab 1/images/'

    image_files = os.listdir(image_dir)

    for image_file in image_files[:]:
        if image_file == '.DS_Store': continue
        image = mpimg.imread(image_dir+image_file)
        print('Image shape',image.shape)
        if np.amax(image)>1:
            image = (image/255).astype(np.float32)
            print('Converted image to float')

        show_image(image,'Original image')

        show_image(subsample(image,2,2),'Subsampled image')

        show_images(get_channels(image),['Red','Green','Blue'],filename='channels')

        col_ind = [color_index(image,index) for index in range(3)]
        show_images(col_ind,['Red','Green','Blue'],filename='color indices')

        show_image(gray_level(image),'Gray-level image')

        show_image(negative_gray_level(image),'Negative gray-level image')

        show_image(mirror(image),'Mirrored image')

        show_image(upside_down(image),'Upside-down image')

        show_image(vert_edges(negative_gray_level(image)),'Vertical edges')

        show_image(hor_edges(negative_gray_level(image)),'Horizontal edges')

        show_image(np.sqrt(hor_edges(negative_gray_level(image))**2+vert_edges(negative_gray_level(image))**2),'Edge magnitudes')

        fig, ax = show_image(image,'Brightest regions',save_im=False)

        reg_rows, reg_cols = 500,500
        x,y,s = brightest_region(image,reg_rows, reg_cols)
        ax.plot(x,y,color='k')

        x,y,s = brightest_region(-image,reg_rows, reg_cols)
        ax.plot(x,y,color='w')

        c = 'rgb'
        for i in range(3):
            x,y,s = brightest_region(color_index(image,i),reg_rows, reg_cols)
            ax.plot(x,y,color=c[i])

        fig.savefig('brightest_regions.jpg',bbox_inches='tight', pad_inches=0.1)