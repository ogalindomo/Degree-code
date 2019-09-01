#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 29 14:10:46 2018

@author: oscargalindo
"""

import cv2
import os
from urllib.request import urlretrieve
import numpy as np
import random
from sklearn.neural_network import MLPClassifier


#def download(filename, source='http://yann.lecun.com/exdb/mnist/'):
#    print("Downloading %s" % filename)
#    urlretrieve(source + filename, filename)

# We then define functions for loading MNIST images and labels.
# For convenience, they also download the requested files if needed.
import gzip
#
def load_mnist_images(filename):
    if not os.path.exists(filename):
        download(filename)
    # Read the inputs in Yann LeCun's binary format.
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
    if not os.path.exists(filename):
        download(filename)
    # Read the labels in Yann LeCun's binary format.
    with gzip.open(filename, 'rb') as f:
        data = np.frombuffer(f.read(), np.uint8, offset=8)
    # The labels are vectors of integers now, that's exactly what we want.
    return data

#def knn (test_x, training_x, training_y):
#    for x in range (test_x.shape[0]):
       
train_ex = 1000
test_ex = 1000 
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
y_train = load_mnist_labels('train-labels-idx1-ubyte.gz')
X_test = load_mnist_images('t10k-images-idx3-ubyte.gz')
y_test = load_mnist_labels('t10k-labels-idx1-ubyte.gz')

X_train = X_train.reshape((60000, 784))
X_test = X_test.reshape((10000,784))

#p = k_nn(X_train, y_train, X_test, 1)
#accuracy = np.sum(p==y_test)/train_ex
#print('Accuracy', accuracy)

classifier = MLPClassifier(hidden_layer_sizes=(20,20), verbose=True)
classifier.fit(X_train, y_train)
p = classifier.predict(X_test)
accuracy = np.sum(p==y_test)/y_test.shape[0]
print('MLP accuracy = ', accuracy )