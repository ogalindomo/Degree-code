# -*- coding: utf-8 -*-
"""
Created on Sun Feb 10 19:36:12 2019

@author: oscargalindo
"""
import plaidml.keras
plaidml.keras.install_backend()
import os
#os.environ["GPU_SINGLE_ALLOC_PERCENT"] = "100"
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
from data_creation import data_creation
from keras import layers
from keras import models
from keras.preprocessing.image import ImageDataGenerator
from keras import optimizers
from keras import regularizers
KERAS_BACKEND=plaidml.keras.backend
####################################Cats and Dogs######################################################
#original_dataset_dir = '/Users/oscargalindo/Desktop/Classes/CS 4371/Lab 1 (Ch.5)/dogs-vs-cats/train'
#base_dir = '/Users/oscargalindo/Desktop/Classes/CS 4371/Lab 1 (Ch.5)/sets'
#data = data_import(original_dataset_dir, base_dir,train=10000,validation=1000,test=1000)
#train_datagen = ImageDataGenerator(rescale = 1./255)
#validation_datagen = ImageDataGenerator(rescale = 1./255)
#t_gen = train_datagen.flow_from_directory(data.train_dir, target_size=(150,150), batch_size=20, class_mode='binary')
#v_gen = train_datagen.flow_from_directory(data.validation_dir, target_size=(150,150), batch_size=20, class_mode='binary')
#data = data_import(original_dataset_dir, base_dir)
#####################################Dogs Breeds########################################################
base_dir = '/Users/oscargalindo/Desktop/Classes/CS 4371/Lab 1 (Ch.5)/stanford-dogs-dataset'
original_dataset_dir = '/Users/oscargalindo/Desktop/Classes/CS 4371/Lab 1 (Ch.5)/stanford-dogs-dataset/Images'
rename_dir = os.path.join(base_dir,"Renamed")
sets_dir = os.path.join(base_dir, "sets")
data = data_creation(original_dataset_dir, sets_dir, rename_dir, 0.7, 0.2, 0.1)

train_datagen = ImageDataGenerator(rescale = 1./255, horizontal_flip=True)
validation_datagen = ImageDataGenerator(rescale = 1./255)
testing_datagen = ImageDataGenerator(rescale = 1./255)
t_gen = train_datagen.flow_from_directory(data.train, target_size=(128,128), batch_size=32, shuffle=True, class_mode='categorical',color_mode="rgb")
print(t_gen.class_indices)
v_gen = validation_datagen.flow_from_directory(data.validation, target_size=(128,128), class_mode='categorical', color_mode="rgb", shuffle=False, batch_size=128)
test_g = testing_datagen.flow_from_directory(data.test, target_size=(128,128), class_mode='categorical', color_mode='rgb')
#######################################################################################################
model = models.Sequential()
model.add(layers.Conv2D(32, (3,3), activation='relu', input_shape=(128,128,3), kernel_initializer='he_uniform'))
model.add(layers.MaxPooling2D((2,2)))
model.add(layers.BatchNormalization())
model.add(layers.Dropout(0.2))
model.add(layers.Conv2D(32, (3,3), activation='relu', kernel_initializer='he_uniform'))
model.add(layers.MaxPooling2D((2,2)))
model.add(layers.Dropout(0.2))
model.add(layers.Conv2D(64, (3,3), activation='relu', kernel_initializer='he_uniform'))
model.add(layers.MaxPooling2D((2,2)))
model.add(layers.BatchNormalization())
model.add(layers.Dropout(0.2))
model.add(layers.Conv2D(64, (3,3), activation='relu', kernel_initializer='he_uniform'))
model.add(layers.BatchNormalization())
model.add(layers.Conv2D(128, (3,3), activation='relu', kernel_initializer='he_uniform'))
model.add(layers.MaxPooling2D((2,2)))
model.add(layers.Dropout(0.2))
model.add(layers.Conv2D(256, (3,3), activation='relu', kernel_initializer='he_uniform'))
model.add(layers.MaxPooling2D((2,2)))
model.add(layers.Flatten())
model.add(layers.BatchNormalization())
model.add(layers.Dropout(0.2))
model.add(layers.Dense(512, activation='relu', kernel_initializer='he_uniform'))
model.add(layers.BatchNormalization())
model.add(layers.Dense(120, activation='softmax'))

model.compile(optimizer = optimizers.Adam(lr=0.01), loss = "categorical_crossentropy", metrics=["accuracy"])
model.summary()
history = model.fit_generator(generator=t_gen, steps_per_epoch = 512, epochs = 100, validation_steps = 32, validation_data = v_gen, verbose = 1)
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

img = cv.imread('/Users/oscargalindo/Desktop/stanford-dogs-dataset/sets/test/affenpinscher/affenpinscher5.jpg')
arr = np.asarray(img)
resized = cv.resize(arr, None, fx = 128/arr.shape[1], fy = 128/arr.shape[0], interpolation = cv.INTER_CUBIC)
i = np.expand_dims(resized, 0)

print(model.predict_classes(i, verbose=1))
