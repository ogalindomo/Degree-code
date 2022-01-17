# Implementation of disjoint set forest (or union/find data structure)
# Programmed by Olac Fuentes
# Last modified July 19, 2020

from scipy.interpolate import interp1d
from scipy.signal import correlate2d
import numpy as np
import matplotlib.pyplot as plt
from numpy.random import default_rng
import cv2

class DSF:
    # Constructor
    def __init__(self, n_sets):
        # Creates forest with 'n_sets' root nodes
        self.parent = [-1 for i in range(n_sets)]

    def find(self,i):
        # Returns root of tree that i belongs to
        if self.parent[i]<0:
            return i
        p = self.find(self.parent[i])
        self.parent[i] = p
        return p

    def union(self,i,j):
        # Joins i's tree and j's tree if they are different
        # Returns 1 if a parent reference was changed, 0 otherwise
        root_i = self.find(i)
        root_j = self.find(j)
        if root_i == root_j: # i and j already belong to the same set
            return 0
        if root_i < root_j:
            self.parent[root_j] = root_i
        else:
            self.parent[root_i] = root_j
        return 1

    def set_list(self):
        # Returns a list of lists containing the elements of each set
        set_list = [ [] for i in range(len(self.parent))]
        for i in range(len(self.parent)):
            set_list[self.find(i)].append(i)
        set_list = [s for s in set_list if len(s)>0] # Remove empty lists
        return set_list

    def draw(self,title=''):
        scale = 30
        figsize = [6.4, 3.4]
        if len(self.parent)>8:
            figsize[0] = 6.4*len(self.parent)/8
        fig, ax = plt.subplots(figsize=figsize)

        for i in range(len(self.parent)):
            if self.parent[i]<0:
                ax.plot([i*scale,i*scale],[0,scale*3/4],linewidth=1,color='k')
                ax.plot([i*scale-1,i*scale,i*scale+1],[scale*3/4-2,scale*3/4,scale*3/4-2],linewidth=1,color='k')
            else:
                x = np.linspace(i*scale,self.parent[i]*scale)
                x0 = np.linspace(i*scale,self.parent[i]*scale,num=5)
                diff = np.abs(self.parent[i]-i)
                if diff == 1:
                    y0 = [0,0,0,0,0]
                else:
                    y0 = [0,-6*diff,-8*diff,-6*diff,0]
                f = interp1d(x0, y0, kind='cubic')
                y = f(x)
                ax.plot(x,y,linewidth=1,color='k')
                ax.plot([x0[2]+2*np.sign(i-self.parent[i]),x0[2],x0[2]+2*np.sign(i-self.parent[i])],[y0[2]-1,y0[2],y0[2]+1],linewidth=1,color='k')
            ax.text(i*scale,0, str(i), size=20,ha="center", va="center",
             bbox=dict(facecolor='w',boxstyle="circle"))
        ax.axis('off')
        ax.set_aspect(1.0)
        plt.tight_layout()
        fig.suptitle(title, fontsize=16)
        fig.savefig(title+'.png')
        
def connected_components(img,diff):
    d = DSF(img.shape[0]*img.shape[1])
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            if len(img.shape) < 3:
                if i+1 < img.shape[0] and abs(img[i+1,j] - img[i,j]) < diff:
                    d.union(i*img.shape[0]+j,(i+1)*img.shape[0]+j)
                if j+1 < img.shape[1] and abs(img[i,j+1] - img[i,j]) < diff:
                    d.union(i*img.shape[0]+j,i*img.shape[0]+j+1)
            else:
                if i+1 < img.shape[0] and np.mean(np.absolute(img[i+1,j] - img[i,j])) < diff:
                    d.union(i*img.shape[0]+j,(i+1)*img.shape[0]+j)
                if j+1 < img.shape[1] and np.mean(np.absolute(img[i,j+1] - img[i,j])) < diff:
                    d.union(i*img.shape[0]+j,i*img.shape[0]+j+1)
    return d

def get_motion(frame,row,col):
    columns = np.zeros((frame.shape[:-1])) + np.arange(frame.shape[1])
    rows = np.zeros((frame.shape[:-1])).T + np.arange(frame.shape[0])
    rows = rows.T
    r = np.sqrt(np.power(rows-row,2)+np.power(columns-col,2))
    e = np.exp(-0.025*r.astype(np.float32))
    e[row,col] = 0
    e[row,col] = np.amax(e)
    return e

def track(frames,frames_single):
    frame_c = 1
    print(len(frames))
    plt.close('all')
    cv2.destroyAllWindows()
    frame = frames[50]
    cv2.imshow("Feed",frame)
    ##############Tracking Container####################
    # fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    # out = cv2.VideoWriter('tracking.mp4',fourcc, 20.0, (frame.shape[0],frame.shape[1]))
    ##################################
    bbox = cv2.selectROI(frame, False)
    print(f"Selected {bbox[0]} and {bbox[1]}")
    max_r,min_r = bbox[1]+bbox[3],bbox[1]
    max_c,min_c = bbox[0]+bbox[2],bbox[0]
    obj = frame[min_r:max_r,min_c:max_c,::-1]
    obj_single = np.mean(obj,axis=2)
    previous_c,previous_r = min_c,min_r
    
    for i in range(51,len(frames)):
        print(f'Processing Frame {frame_c}')
        frame2 = frames[i]
        corr = correlate2d(frames_single[i], obj_single, mode='valid')
        motion = get_motion(frame,previous_r,previous_c)
        motion = motion[:corr.shape[0],:corr.shape[1]]
        tracker = motion*corr
        f,a = plt.subplots(nrows = 2,ncols = 2)
        a[0,0].imshow(corr,cmap='gray')
        a[0,1].imshow(motion,cmap='gray')
        a[1,0].imshow(tracker,cmap='gray')
        y, x = np.unravel_index(np.argmax(tracker), tracker.shape)
        frame2_copy = frame2.copy()
        p1 = (x,y)
        p2 = (x+bbox[2],y+bbox[3])
        cv2.rectangle(frame2_copy, p1, p2, (255,0,0), 2, 1)
        # out.write(frame)
        plt.imshow(frame2_copy[:,:,::-1])
        plt.show()
        frame = frame2
        previous_c,previous_r = x,y
        if frame_c%60 == 0: 
            obj = frame2[y:y+bbox[3],x:x+bbox[2],:]
        frame_c += 1
    # out.release()
    
def watch():
    cv2.destroyAllWindows()
    video = cv2.VideoCapture('/Users/oscargalindo/Downloads/tesvor1.avi')
    ok, frame = video.read()
    # cv2.imshow("Feed",frame)
    count = 1
    v = []
    v_s = []
    while ok:
        ok,frame = video.read()
        count +=1
        # cv2.imshow("Feed",frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        if ok:
            v.append(frame)
            v_s.append(np.mean(frame,axis=2))
    return v,v_s

def observe():
    cv2.destroyAllWindows()
    video = cv2.VideoCapture('/Users/oscargalindo/Downloads/practice exam images/q6.avi')
    ok, frame = video.read()
    cv2.imshow("Feed",frame)
    count = 0
    while count < 1000:
        ok,frame = video.read()
        print(frame)
        if ok:
            cv2.imshow("Feed",frame)
    

if __name__ == "__main__":
    # This code was used to generate the images in the 'segmentation with connected components.pdf' file
    
    # img = (np.random.rand(1200,1200,3)).astype(np.float32)
    # dsf = connected_components(img,0.3)
    # roots = dsf.parent
    # roots = np.array(roots).reshape(img.shape[0],img.shape[1])
    # roots[roots == -1] = 0
    # roots[roots > 0] = 1
    # plt.imshow(roots,cmap='gray')
    # f,f_s = watch()
    # track(f,f_s)
    observe()
    
    
    
