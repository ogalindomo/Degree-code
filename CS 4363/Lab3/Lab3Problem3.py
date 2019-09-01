"""
Backward warping example using a single point
Progammed by Olac Fuentes
Last modified October 1, 2018
"""

import numpy as np
import pylab as plt
from PIL import Image
import time

source_im = np.array(Image.open('tennis.jpg'), dtype=np.uint8)
plt.figure(1)
plt.imshow(source_im)
plt.show()

print("Click source and destination of warp point")
p = np.asarray(plt.ginput(n=2), dtype=np.float32)
print(p)
print(p[0]-p[1])
plt.plot(p[:,0], p[:,1], color="blue")
plt.plot(p[0][0], p[0][1],marker='x', markersize=3, color="red")
plt.plot(p[1][0], p[1][1],marker='x', markersize=3, color="red")
plt.show()
start = time.time()

#Generate pixels coordinates in the destination image       
dest_im = np.zeros(source_im.shape, dtype=np.uint8)                 
max_row = source_im.shape[0]-1
max_col = source_im.shape[1]-1
dest_rows = dest_im.shape[0]
dest_cols = dest_im.shape[1]

#Painting outline of source image black, so out of bounds pixels can be painted black  
source_im[0]=0
source_im[max_row]=0         
source_im[:,0]=0
source_im[:,max_col]=0 
         
#Generate pixel coordinates in the destination image         
ind = np.arange(dest_rows*dest_cols )
row_vect = ind//dest_cols
col_vect = ind%dest_cols
coords = np.vstack((row_vect,col_vect))

#Computing pixel weights, pixels close to p[1] will have higher weights    
dist = np.sqrt(np.square(p[1][1] - row_vect) + np.square(p[1][0] - col_vect))
weight = np.exp(-dist/100)         #Constant needs to be tweaked depending on image size

#Computing pixel weights, pixels close to p[1] will have higher weights    
source_coords = np.zeros(coords.shape, dtype=np.int)
disp_r = (weight*(p[0][1]-p[1][1])).astype(int)
disp_c = (weight*(p[0][0]-p[1][0])).astype(int)
source_coords[0] = coords[0] + disp_r
source_coords[1] = coords[1] + disp_c
             
#Fixing out-of-bounds coordinates               
source_coords[source_coords<0] = 0
source_coords[0,source_coords[0]>max_row] = max_row             
source_coords[1,source_coords[1]>max_col] = max_col      
      
dest_im = source_im[source_coords[0],source_coords[1],:].reshape(dest_rows,dest_cols,3)

plt.figure(2)
plt.imshow(dest_im)
plt.show()

elapsed_time = time.time()-start
print('Elapsed time: {0:.2f} '.format(elapsed_time))   
