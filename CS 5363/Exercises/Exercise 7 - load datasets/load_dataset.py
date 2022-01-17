#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  2 11:42:44 2021

@author: oscargalindo
"""

import csv, numpy as np
import matplotlib.pyplot as plt
from keras.datasets import mnist
import matplotlib.image as mpimg
import tarfile
import os
from urllib.request import urlretrieve
import numpy as np

def cifar10(path=None):
    r"""Return (train_images, train_labels, test_images, test_labels).

    Args:
        path (str): Directory containing CIFAR-10. Default is
            /home/USER/data/cifar10 or C:\Users\USER\data\cifar10.
            Create if nonexistant. Download CIFAR-10 if missing.

    Returns:
        Tuple of (train_images, train_labels, test_images, test_labels), each
            a matrix. Rows are examples. Columns of images are pixel values,
            with the order (red -> blue -> green). Columns of labels are a
            onehot encoding of the correct class.
    """
    url = 'https://www.cs.toronto.edu/~kriz/'
    tar = 'cifar-10-binary.tar.gz'
    files = ['cifar-10-batches-bin/data_batch_1.bin',
             'cifar-10-batches-bin/data_batch_2.bin',
             'cifar-10-batches-bin/data_batch_3.bin',
             'cifar-10-batches-bin/data_batch_4.bin',
             'cifar-10-batches-bin/data_batch_5.bin',
             'cifar-10-batches-bin/test_batch.bin']

    if path is None:
        # Set path to /home/USER/data/mnist or C:\Users\USER\data\mnist
        path = os.path.join(os.path.expanduser('~'), 'data', 'cifar10')

    # Create path if it doesn't exist
    os.makedirs(path, exist_ok=True)

    # Download tarfile if missing
    if tar not in os.listdir(path):
        urlretrieve(''.join((url, tar)), os.path.join(path, tar))
        print("Downloaded %s to %s" % (tar, path))

    # Load data from tarfile
    with tarfile.open(os.path.join(path, tar)) as tar_object:
        # Each file contains 10,000 color images and 10,000 labels
        fsize = 10000 * (32 * 32 * 3) + 10000

        # There are 6 files (5 train and 1 test)
        buffr = np.zeros(fsize * 6, dtype='uint8')

        # Get members of tar corresponding to data files
        # -- The tar contains README's and other extraneous stuff
        members = [file for file in tar_object if file.name in files]

        # Sort those members by name
        # -- Ensures we load train data in the proper order
        # -- Ensures that test data is the last file in the list
        members.sort(key=lambda member: member.name)

        # Extract data from members
        for i, member in enumerate(members):
            # Get member as a file object
            f = tar_object.extractfile(member)
            # Read bytes from that file object into buffr
            buffr[i * fsize:(i + 1) * fsize] = np.frombuffer(f.read(), 'B')

    # Parse data from buffer
    # -- Examples are in chunks of 3,073 bytes
    # -- First byte of each chunk is the label
    # -- Next 32 * 32 * 3 = 3,072 bytes are its corresponding image

    # Labels are the first byte of every chunk
    labels = buffr[::3073]

    # Pixels are everything remaining after we delete the labels
    pixels = np.delete(buffr, np.arange(0, buffr.size, 3073))
    images = pixels.reshape(-1, 3072).astype('float32') / 255

    # Split into train and test
    train_images, test_images = images[:50000], images[50000:]
    train_labels, test_labels = labels[:50000], labels[50000:]

    def _onehot(integer_labels):
        """Return matrix whose rows are onehot encodings of integers."""
        n_rows = len(integer_labels)
        n_cols = integer_labels.max() + 1
        onehot = np.zeros((n_rows, n_cols), dtype='uint8')
        onehot[np.arange(n_rows), integer_labels] = 1
        return onehot

    return train_images, _onehot(train_labels), \
        test_images, _onehot(test_labels)
        
def load_cifar10():
    train_data,train_labels,test_data,test_labels = cifar10()
    train_data = train_data.reshape(-1,3,32,32)
    train_data=np.swapaxes(train_data,1,3)
    train_data=np.swapaxes(train_data,1,2)
    test_data = test_data.reshape(-1,3,32,32)
    test_data = np.swapaxes(test_data,1,3)
    test_data = np.swapaxes(test_data,1,2)
    return train_data,train_labels,\
        test_data,test_labels
    
def load_mnist():
    train,test = mnist.load_data()
    return train[0],train[1],test[0],test[1]

def get_id(name):
    parts = name.split("__")
    idx = parts[0][3:]
    return int(idx)
    
def load_coil():
    files = '/Users/oscargalindo/Desktop/Classes/CS 5363/Exercises/Exercise 7/coil/coil-100/coil-100/'
    size = len(os.listdir(files))
    idxs = np.zeros((size)).astype(np.int)
    i = 0
    dataset = np.zeros((size,128,128,3)).astype(np.float32)
    for file in os.listdir(files):
        if file[-4:] == '.png':
            idx = get_id(file)
            idxs[i] = idx
            p = mpimg.imread(files+file)
            dataset[i] = p
            i+=1
    return dataset,idxs
    
if __name__=="__main__":
    data,idx = load_coil()
    plt.imshow(data[0x131])
    # mnist_dataset = load_mnist()
    # cifar_dataset = load_cifar10()
    # train_mnist,train_mnist_labels,\
    #     test_mnist,test_mnist_labels = mnist_dataset
    # train_cifar,train_cifar_labels,\
    #     test_cifar,test_cifar_labels = cifar_dataset
    