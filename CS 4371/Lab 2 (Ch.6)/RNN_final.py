#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 10 17:58:49 2019

@author: oscargalindo
"""

import matplotlib.pyplot as plt
from data import data
import plaidml.keras
import os
plaidml.keras.install_backend()
os.environ["GPU_SINGLE_ALLOC_PERCENT"] = "100"
from keras.datasets import imdb
from keras.preprocessing.text import Tokenizer
from keras import preprocessing
from keras.preprocessing.sequence import pad_sequences
from keras.models import Sequential
from keras.layers import Flatten, Dense, Embedding, LSTM, SimpleRNN, GRU
KERAS_BACKEND=plaidml.keras.backend

test, validation = 0.7, 0.3
main_dir = '/Users/oscargalindo/Desktop/spam.csv'
data = data(basedir = main_dir, test = test, validation = validation)
print(data.y)
tokenizer = Tokenizer()
tokenizer.fit_on_texts(data.x)
sequences = tokenizer.texts_to_sequences(data.x)
word_index = tokenizer.word_index
print('Found %s unique tokens.' % len(word_index))
###############Datasets###############################
x = preprocessing.sequence.pad_sequences(sequences, maxlen = 10)
x_train = x[:int(len(sequences)*test),:]
y_train = data.y[:int(len(sequences)*test)]

x_validation = x[int(len(sequences)*test):int(len(sequences)*(test + validation/2)),:]
y_validation = data.y[int(len(sequences)*test):int(len(sequences)*(test + validation/2))]

x_test = x[int(len(sequences)*(test + validation/2)):,:]
y_test = data.y[int(len(sequences)*(test + validation/2)):]
######################################################
print(tokenizer.word_counts)
#print(tokenizer.document_count)
#print(tokenizer.word_index)
#print(sequences[0])
#print(tokenizer.word_docs)
#print(data.y)

model = Sequential()
#model.add(Embedding(len(word_index), 50, input_length = 10))
model.add(Embedding(len(word_index), 12, input_length = 10))
model.add(LSTM(64, return_sequences = True, recurrent_dropout = 0.7, activation='tanh'))
model.add(LSTM(32, return_sequences = True, recurrent_dropout = 0.7, activation='tanh'))
model.add(Flatten())
model.add(Dense(32, activation='relu'))
model.add(Dense(1, activation='sigmoid'))
model.compile(optimizer='Adam', loss='binary_crossentropy', metrics=['acc'])
#model.add(Embedding(int(len(word_index)), 12, input_length = 10))
##model.add(SimpleRNN(32, return_sequences = True))
#model.add(LSTM(64, return_sequences = True, recurrent_dropout = 0.7, activation='tanh'))
#model.add(Flatten())
#model.add(Dense(32, activation='relu'))
#model.add(Dense(1, activation='sigmoid'))
#model.compile(optimizer='Adam', loss='binary_crossentropy', metrics=['acc'])
model.summary()

history = model.fit(x_train, y_train, epochs =  10, validation_data = (x_validation, y_validation))
acc = history.history['acc']

val_acc = history.history['val_acc']
loss = history.history['loss']
val_loss = history.history['val_loss']

epochs = range(1, len(acc) + 1)

plt.plot(epochs, acc, 'bo', label='Training acc')
plt.plot(epochs, val_acc, 'b', label='Validation acc')
plt.title('Training and validation accuracy')
plt.legend()

plt.figure()

plt.plot(epochs, loss, 'bo', label='Training loss')
plt.plot(epochs, val_loss, 'b', label='Validation loss')
plt.title('Training and validation loss')
plt.legend()
plt.show()

scores = model.evaluate(x_test, y_test, verbose = 1)
print(scores)