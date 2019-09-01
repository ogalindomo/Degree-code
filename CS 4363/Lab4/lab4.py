import cv2
import os
from urllib.request import urlretrieve
import numpy as np
import random
from sklearn.neural_network import MLPClassifier
from sklearn.neural_network import MLPRegressor
from sklearn.linear_model import SGDClassifier
from sklearn.linear_model import OrthogonalMatchingPursuit
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.decomposition import PCA
from sklearn.neighbors import KNeighborsClassifier
import time

# Some code related to feature computation
# Programmed by Olac Fuentes
# Last modified Ocotber 23, 2018

import math

def integral_image(I):
    S = np.zeros((I.shape[0]+1,I.shape[1]+1))
    S[1:,1:] = np.cumsum(I,axis =1)
    S = np.cumsum(S,axis = 0)
    return S

def sum_region(I,r0,c0,r1,c1):
    return np.sum(I[r0:r1+1,c0:c1+1])

def sum_region_integral(S,r0,c0,r1,c1):
    return S[r1+1,c1+1] - S[r1+1,c0] - S[r0,c1+1] + S[r0,c0]

def hor_grad(I):
    kernel = np.ones((1,2))
    kernel[0,0]=-1
    return cv2.filter2D(I,-1,kernel,borderType=cv2.BORDER_REPLICATE)

def ver_grad(I):    
    kernel = np.ones((2,1)) 
    kernel[0,0]=-1
    return cv2.filter2D(I,-1,kernel,borderType=cv2.BORDER_REPLICATE)

def grad_mag(vg,hg):    
    return np.sqrt(vg*vg+hg*hg)

def grad_angle(vg,hg): 
    t = np.arctan2(vg,hg)*180/math.pi
    t[t<0] = t[t<0] + 360
    return t

def hog(gm,ga,bars): 
    hist = np.zeros(bars)
    assigned_bar = (ga//(360/bars)+.5).astype(np.int)
    for b in range(bars):
        hist[b] = np.sum(gm[assigned_bar==b])
    return hist

#I = np.arange(24).reshape((4,6)).astype(np.float)
I = np.random.randint(10, size=24).reshape((4,6)).astype(np.float)

S = integral_image(I)

print(I)
print(S)

print(sum_region(I,1,2,2,4))
print(sum_region_integral(S,1,2,2,4))

hg = hor_grad(I)
vg = ver_grad(I)
print(hg)
print(vg)

gm = grad_mag(vg,hg)
ga = grad_angle(vg,hg)

print(gm)
print(ga)

h = hog(gm,ga,8)
print(h)
print(np.sum(h))
print(np.sum(gm))


#def download(filename, source='http://yann.lecun.com/exdb/mnist/'):
#    print("Downloading %s" % filename)
#    urlretrieve(source + filename, filename)

# We then define functions for loading MNIST images and labels.
# For convenience, they also download the requested files if needed.
import gzip
#
def load_mnist_images(filename):
#    if not os.path.exists(filename):
#        download(filename)
#    # Read the inputs in Yann LeCun's binary format.
    with gzip.open(filename, 'rb') as f:
        data = np.frombuffer(f.read(), np.uint8, offset=16)
    # The inputs are vectors now, we reshape them to monochrome 2D images,
    # following the shape convention: (examples, channels, rows, columns)
    data = data.reshape(-1, 1, 28, 28)
    # The inputs come as bytes, we convert them to float32 in range [0,1].
    # (Actually to range [0, 255/256], for compatibility to the version
    # provided at http://deeplearning.net/data/mnist/mnist.pkl.gz.)
    return data / np.float32(256)

def load_mnist_labels(filename):
#    if not os.path.exists(filename):
#        download(filename)
#    # Read the labels in Yann LeCun's binary format.
    with gzip.open(filename, 'rb') as f:
        data = np.frombuffer(f.read(), np.uint8, offset=8)
    # The labels are vectors of integers now, that's exactly what we want.
    return data

#def knn (test_x, training_x, training_y):
#    for x in range (test_x.shape[0]):
       
train_ex = 1000
test_ex = 2000 
def k_nn(X_train,y_train, X_test, k):
    pred = np.zeros(y_test.shape).astype(np.uint8)
    n_classes = np.max(y_train)+1
    for i in range(X_test.shape[0]):
        if i%100 == 0:
            print(i, 'examples processed')
        D = X_train-X_test[i]
        D = D*D
        Sd = np.sum(D,axis=1)
        nn = np.argsort(Sd)[:k]
        w = 1/(Sd[nn]+1e-10)
        vote = np.zeros(n_classes)
        for j in range(k):
            vote [y_train[nn[j]]] += w[j]
        pred[i] = np.argmax(vote)
    return pred

X_train = load_mnist_images('train-images-idx3-ubyte.gz')
X_train = X_train[:train_ex,:,:,:]
y_train = load_mnist_labels('train-labels-idx1-ubyte.gz')
y_train = y_train[:train_ex]
X_test = load_mnist_images('t10k-images-idx3-ubyte.gz')
X_test = X_test[:test_ex,:,:,:]
y_test = load_mnist_labels('t10k-labels-idx1-ubyte.gz')
y_test = y_test[:test_ex]

X_train = X_train.reshape((train_ex, 784))
X_test = X_test.reshape((test_ex,784))

new_X_test = np.zeros((test_ex, 16))
new_X_train = np.zeros((train_ex, 16))

#for x in range (0, new_X_test.shape[0]):
#    hg = hor_grad(X_test[x,0,:,:])
#    vg = ver_grad(X_test[x,0,:,:])
#    
#    gm = grad_mag(vg,hg)
#    ga = grad_angle(vg,hg)
#    new_X_test[x,:] = hog(gm,ga,new_X_test.shape[1])
#
#for x in range (0, new_X_train.shape[0]):
#    hg = hor_grad(X_train[x,0,:,:])
#    vg = ver_grad(X_train[x,0,:,:])
#
#    gm = grad_mag(vg,hg)
#    ga = grad_angle(vg,hg)
#    new_X_train[x,:] = hog(gm,ga,new_X_train.shape[1])
    

'''Algorithm 1'''
#pca = PCA(n_components=30)
#pca.fit(X_train)
#
#X_train = pca.transform(X_train)
#X_test = pca.transform(X_test)
#start_time = time.time()
#classifier = KNeighborsClassifier(n_neighbors=3, algorithm = 'brute')
##p = k_nn(X_train, y_train, X_test, 3) #Without HOG
##p = k_nn(new_X_train, y_train, new_X_test, 3)
##classifier.fit(new_X_train, y_train) #HOG
#classifier.fit(X_train, y_train) #HOG
##p = classifier.predict(new_X_test)
#p = classifier.predict(X_test)
#accuracy = np.sum(p==y_test)/test_ex
#print('Time take', time.time() - start_time)
#print('Accuracy', accuracy)



'''Algorithm 2'''
#pca = PCA(n_components=30)
#pca.fit(X_train)
#
#X_train = pca.transform(X_train)
#X_test = pca.transform(X_test)
#start_time = time.time()
#classifier = MLPClassifier(hidden_layer_sizes=(100, 1000), verbose=True, learning_rate = 'adaptive', 
#                          max_iter = 1000, n_iter_no_change = 100)
##classifier.fit(new_X_train, y_train)
#classifier.fit(X_train, y_train) #Without HOG 
##p = classifier.predict(new_X_test)
#p = classifier.predict(X_test)
#p = (p%10).astype(np.uint8)
#print('Time take', time.time() - start_time)
#print('accuracy = ', accuracy_score(y_test, p))



'''Algorithm 3'''
#pca = PCA(n_components=30)
#pca.fit(X_train)
#
#X_train = pca.transform(X_train)
#X_test = pca.transform(X_test)
#start_time = time.time()
#classifier =  MLPRegressor(hidden_layer_sizes=(100, 1000), verbose=True)
#classifier.fit(X_train, y_train)#Without Hog
##classifier.fit(new_X_train, y_train)
#p = classifier.predict(X_test)#Without Hog
##p = classifier.predict(new_X_test)
#p = (p%10).astype(np.uint8)
#print('Time take', time.time() - start_time)
#print('accuracy = ', accuracy_score(y_test, p))

'''Algorithm 4'''
#pca = PCA(n_components=30)
#pca.fit(X_train)
#
#X_train = pca.transform(X_train)
#X_test = pca.transform(X_test)
#start_time = time.time()
#classifier =  SGDClassifier(verbose = 1)
#classifier.fit(X_train, y_train)#Without HOG
##classifier.fit(new_X_train, y_train)
#p = classifier.predict(X_test)
##p = classifier.predict(new_X_test)
#p = (p%10).astype(np.uint8)
#print('Time take', time.time() - start_time)
#print('accuracy = ', accuracy_score(y_test, p))

'''Algorithm 5'''
#pca = PCA(n_components=30)
#pca.fit(X_train)
#
#X_train = pca.transform(X_train)
#X_test = pca.transform(X_test)
#start_time = time.time()
#classifier =  DecisionTreeClassifier()
#classifier.fit(X_train, y_train)
##classifier.fit(new_X_train, y_train)
#p = classifier.predict(X_test)
##p = classifier.predict(new_X_test)
#p = (p%10).astype(np.uint8)
#print('Time take', time.time() - start_time)
#print('MLP accuracy = ', accuracy_score(y_test, p))
