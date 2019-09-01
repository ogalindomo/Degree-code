#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 20:18:30 2019

@author: oscargalindo
"""
import plaidml.keras
plaidml.keras.install_backend()
import os
import keras
import pydot
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
from keras import layers, applications, Input, models, optimizers, regularizers
from keras.utils import plot_model
from data_creation import data_creation
from keras.models import Model
from keras.preprocessing.image import ImageDataGenerator
KERAS_BACKEND=plaidml.keras.backend
#####################################Dogs Breeds########################################################
base_dir = '/Users/oscargalindo/Desktop/Classes/CS 4371/Lab 3 (Ch.7)/stanford-dogs-dataset'
original_dataset_dir = '/Users/oscargalindo/Desktop/Classes/CS 4371/Lab 3 (Ch.7)/stanford-dogs-dataset/Images'
rename_dir = os.path.join(base_dir,"Renamed")
sets_dir = os.path.join(base_dir, "sets")
data = data_creation(original_dataset_dir, sets_dir, rename_dir, 0.7, 0.2, 0.1)
train_datagen = ImageDataGenerator(rescale = 1./255, horizontal_flip=True, height_shift_range = 1, width_shift_range = 1) #, height_shift = 1, width_shift = 1)
validation_datagen = ImageDataGenerator(rescale = 1./255)
testing_datagen = ImageDataGenerator(rescale = 1./255)
t_gen = train_datagen.flow_from_directory(data.train, target_size=(128,128), batch_size=32, shuffle=True, class_mode='categorical',color_mode="rgb")
#print(t_gen.class_indices)
v_gen = validation_datagen.flow_from_directory(data.validation, target_size=(128,128), class_mode='categorical', color_mode="rgb", shuffle=False, batch_size=128)
test_g = testing_datagen.flow_from_directory(data.test, target_size=(128,128), class_mode='categorical', color_mode='rgb')
#######################################################################################################

##################New Network####################################
##########################First Branch##############################
input_images_1 = Input(shape = (128,128,3), dtype='float32', name = 'dogs_1')

x = layers.Conv2D(32, (3,3), activation='relu', kernel_initializer='he_uniform', dtype='float32')(input_images_1)
x = layers.MaxPooling2D((2,2))(x)
x = layers.BatchNormalization()(x)
x = layers.Dropout(0.5)(x)

x = layers.Conv2D(32, (3,3), activation='relu', kernel_initializer='he_uniform', dtype='float32')(x)
x = layers.MaxPooling2D((2,2))(x)
x = layers.BatchNormalization()(x)
x = layers.Dropout(0.5)(x)

x = layers.Conv2D(64, (3,3), activation='relu', kernel_initializer='he_uniform')(x)
x = layers.MaxPooling2D((2,2))(x)
x = layers.BatchNormalization()(x)
x = layers.Dropout(0.5)(x)

x = layers.Conv2D(64, (3,3), activation='relu', kernel_initializer='he_uniform')(x)
x = layers.MaxPooling2D((2,2))(x)
x = layers.BatchNormalization()(x)
x = layers.Dropout(0.5)(x)

#x = layers.Conv2D(128, (3,3), activation='relu', kernel_initializer='he_uniform')(x)
#x = layers.MaxPooling2D((2,2))(x)
#x = layers.BatchNormalization()(x)
#x = layers.Dropout(0.2)(x)

#x = layers.Conv2D(256, (3,3), activation='relu', kernel_initializer='he_uniform')(x)
#x = layers.MaxPooling2D((2,2))(x)
#x = layers.Dropout(0.2)(x)
#x = layers.BatchNormalization()(x)
x = layers.Flatten()(x)

#x = layers.Dense(512, activation='relu', kernel_initializer='he_uniform')(x)
#x = layers.Dropout(0.3)(x)
#x = layers.Dense(120, activation='relu', dtype='float32', kernel_initializer='he_uniform')(x)
##########################Second Branch############################
y = layers.Conv2D(32, (3,3), activation='relu', kernel_initializer='he_uniform', dtype='float32')(input_images_1)
y = layers.AveragePooling2D((2,2))(y)
y = layers.BatchNormalization()(y)
y = layers.Dropout(0.5)(y)

y = layers.Conv2D(32, (3,3), activation='relu', kernel_initializer='he_uniform', dtype='float32')(y)
y = layers.AveragePooling2D((2,2))(y)
y = layers.BatchNormalization()(y)
y = layers.Dropout(0.5)(y)

y = layers.Conv2D(64, (3,3), activation='relu', kernel_initializer='he_uniform', dtype='float32')(y)
y = layers.AveragePooling2D((2,2))(y)
y = layers.BatchNormalization()(y)
y = layers.Dropout(0.5)(y)

y = layers.Conv2D(64, (3,3), activation='relu', kernel_initializer='he_uniform', dtype='float32')(y)
y = layers.AveragePooling2D((2,2))(y)
y = layers.BatchNormalization()(y)
y = layers.Dropout(0.5)(y)

y = layers.Flatten()(y)
#y = layers.Dense(120, activation='relu', dtype='float32', kernel_initializer='he_uniform')(y)
##########################Third Branch#############################
z = layers.SeparableConv2D(32, (3,3), activation='relu', kernel_initializer='he_uniform', dtype='float32')(input_images_1)
z = layers.AveragePooling2D((2,2))(z)
z = layers.BatchNormalization()(z)
z = layers.Dropout(0.5)(z)

z = layers.SeparableConv2D(32, (3,3), activation='relu', kernel_initializer='he_uniform', dtype='float32')(z)
z = layers.AveragePooling2D((2,2))(z)
z = layers.BatchNormalization()(z)
z = layers.Dropout(0.5)(z)

z = layers.SeparableConv2D(64, (3,3), activation='relu', kernel_initializer='he_uniform', dtype='float32')(z)
z = layers.AveragePooling2D((2,2))(z)
z = layers.BatchNormalization()(z)
z = layers.Dropout(0.5)(z)

z = layers.SeparableConv2D(64, (3,3), activation='relu', kernel_initializer='he_uniform', dtype='float32')(z)
z = layers.AveragePooling2D((2,2))(z)
z = layers.BatchNormalization()(z)
z = layers.Dropout(0.5)(z)
#z = layers.GlobalAveragePooling2D()(z)

z = layers.Flatten()(z)
##########################Fourth Branch################################
w = layers.SeparableConv2D(32, (3,3), activation='relu', kernel_initializer='he_uniform', dtype='float32')(input_images_1)
w = layers.MaxPooling2D((2,2))(w)
w = layers.BatchNormalization()(w)
w = layers.Dropout(0.5)(w)

w = layers.SeparableConv2D(32, (3,3), activation='relu', kernel_initializer='he_uniform', dtype='float32')(w)
w = layers.MaxPooling2D((2,2))(w)
w = layers.BatchNormalization()(w)
w = layers.Dropout(0.5)(w)

w = layers.SeparableConv2D(64, (3,3), activation='relu', kernel_initializer='he_uniform', dtype='float32')(w)
w = layers.MaxPooling2D((2,2))(w)
w = layers.BatchNormalization()(w)
w = layers.Dropout(0.5)(w)

w = layers.SeparableConv2D(64, (3,3), activation='relu', kernel_initializer='he_uniform', dtype='float32')(w)
w = layers.MaxPooling2D((2,2))(w)
w = layers.BatchNormalization()(w)
w = layers.Dropout(0.5)(w)
#z = layers.GlobalAveragePooling2D()(z)

w = layers.Flatten()(w)
######################################################################
concatenated = layers.concatenate([x, y, z, w], axis = -1)
result = layers.Dense(120, activation='softmax', dtype='float32')(concatenated)

model = Model(inputs = (input_images_1) , outputs = result)

model.compile(optimizer = optimizers.Adam(lr=0.01), loss = "categorical_crossentropy", metrics=["accuracy"])
model.summary()

callbacks_list = [
        keras.callbacks.EarlyStopping(monitor='acc', patience = 10),
        keras.callbacks.ModelCheckpoint(filepath = '/Users/oscargalindo/Desktop/model_weights', monitor='val_loss', save_best_only=True)
        ]

history = model.fit_generator(generator=t_gen, steps_per_epoch = 512, epochs = 50, validation_steps = 32, validation_data = v_gen, verbose = 1, callbacks=callbacks_list)
plot_model(model, to_file= '/Users/oscargalindo/Desktop/model.png')

######################################Old Network########################################################
#model = models.Sequential()
#model.add(layers.Conv2D(32, (3,3), activation='relu', input_shape=(128,128,3), kernel_initializer='he_uniform'))
#model.add(layers.MaxPooling2D((2,2)))
#model.add(layers.BatchNormalization())
#model.add(layers.Dropout(0.2))
#model.add(layers.Conv2D(32, (3,3), activation='relu', kernel_initializer='he_uniform'))
#model.add(layers.MaxPooling2D((2,2)))
#model.add(layers.Dropout(0.2))
#model.add(layers.Conv2D(64, (3,3), activation='relu', kernel_initializer='he_uniform'))
#model.add(layers.MaxPooling2D((2,2)))
#model.add(layers.BatchNormalization())
#model.add(layers.Dropout(0.2))
#model.add(layers.Conv2D(64, (3,3), activation='relu', kernel_initializer='he_uniform'))
#model.add(layers.BatchNormalization())
#model.add(layers.Conv2D(128, (3,3), activation='relu', kernel_initializer='he_uniform'))
#model.add(layers.MaxPooling2D((2,2)))
#model.add(layers.Dropout(0.2))
#model.add(layers.Conv2D(256, (3,3), activation='relu', kernel_initializer='he_uniform'))
#model.add(layers.MaxPooling2D((2,2)))
#model.add(layers.Flatten())
#model.add(layers.BatchNormalization())
#model.add(layers.Dropout(0.2))
#model.add(layers.Dense(512, activation='relu', kernel_initializer='he_uniform'))
#model.add(layers.BatchNormalization())
#model.add(layers.Dense(120, activation='softmax'))
#
#model.compile(optimizer = optimizers.Adam(lr=0.01), loss = "categorical_crossentropy", metrics=["accuracy"])
#model.summary()
#history = model.fit_generator(generator=t_gen, steps_per_epoch = 512, epochs = 100, validation_steps = 32, validation_data = v_gen, verbose = 1)
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

#img = cv.imread('/Users/oscargalindo/Desktop/stanford-dogs-dataset/sets/test/affenpinscher/affenpinscher5.jpg')
#arr = np.asarray(img)
#resized = cv.resize(arr, None, fx = 128/arr.shape[1], fy = 128/arr.shape[0], interpolation = cv.INTER_CUBIC)
#i = np.expand_dims(resized, 0)

#print(model.predict_classes(i, verbose=1))