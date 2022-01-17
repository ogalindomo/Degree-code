import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

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
    return x,y

if __name__ == "__main__":

    plt.close('all')
    reg_rows,reg_cols = 100,80
    f = np.arange(1,16)
    files = ['stop'+str(i)+'.jpg' for i in f]

    for file in  files[:]:
        img = plt.imread(file)/255

        red_img = 2*img[:,:,0] - img[:,:,1] - img[:,:,2]
        x,y = compute_brightest_area(red_img,reg_cols,reg_rows)
        fig, ax = plt.subplots(1)
  
        # Display the image
        ax.imshow(red_img,cmap='gray')
          
        # Create a Rectangle patch
        rect = patches.Rectangle((x, y), reg_cols, reg_rows, linewidth=1,
                                 edgecolor='r', facecolor="none")
          
        # Add the patch to the Axes
        ax.add_patch(rect)
        # Find reddest region and draw box around it

        # plt.figure()
        # plt.imshow(red_img,cmap='gray')
        # plt.show()
        # plt.imshow(red_img[x:x+int(img.shape[0]*0.1),y:y+int(img.shape[1]*0.1)],cmap='gray')
        # plt.show()

