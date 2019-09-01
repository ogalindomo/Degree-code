#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 12:06:33 2019

@author: oscargalindo
"""
import matplotlib.pyplot as plt
import plaidml.keras
import os
plaidml.keras.install_backend()
os.environ["GPU_SINGLE_ALLOC_PERCENT"] = "100"
from keras.datasets import imdb
from keras import preprocessing
from keras.models import Sequential
from keras.layers import Flatten, Dense
from keras.layers import Embedding
KERAS_BACKEND=plaidml.keras.backend

max_features = 10000
maxlen = 20

(x_train, y_train), (x_test, y_test) = imdb.load_data()#num_words=max_features)
print(x_train[0])
x_train = preprocessing.sequence.pad_sequences(x_train, maxlen=maxlen)
print(x_train[0])
x_test = preprocessing.sequence.pad_sequences(x_test, maxlen=maxlen)

print(x_train[0])

model = Sequential()
model.add(Embedding(10000, 8, input_length=maxlen))
#model.add(SimpleRNN(32))

model.add(Flatten())

model.add(Dense(1, activation='sigmoid'))
model.compile('rmsprop', loss='binary_crossentropy', metrics=['acc','mse'])
model.summary()

history = model.fit(x_train, y_train, epochs = 10, batch_size = 32, validation_split = 0.2)

acc = history.history['acc']
val_acc = history.history['val_acc']
loss = history.history['loss']
val_loss = history.history['val_loss']

epochs = range(1,len(acc) + 1)

plt.plot(epochs, acc, 'bo', label='Training accuracy')
plt.plot(epochs, val_acc, 'b', label='Validation accuracy')
plt.title('Training and Validation Accuracy')
plt.legend()

plt.figure()

plt.plot(epochs, loss, 'bo', label='Training loss')
plt.plot(epochs, val_loss, 'b', label='Validation loss')
plt.title('Training and Validation loss')
plt.legend()

plt.show()