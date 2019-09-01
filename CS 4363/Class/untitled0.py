#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 14:08:14 2018

@author: oscargalindo
"""

from sklearn.neighbors import MLPClassifier

y_train = load_mnist_labels('train-labels-idx1-ubyte.gz')

classifier = MLPClassifier(hidden_layer_sizes=(20,20))
classifier.fir(X_train, y_train)
p = classsifier.predict(X_test)
accuracy = np.sum(p==y_test)/y_test.shape[0]
print('MLP accuracy = ', accuracy )
