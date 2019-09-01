#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 14 12:11:12 2019

@author: oscargalindo
"""

import keras
from keras import layers
from keras.preprocessing import image
import matplotlib.pyplot as plt
import numpy as np
import os 
latent_dim = 128
height = 128
width = 128 
channels = 3

generator_input = keras.Input(shape=(latent_dim,))
x = layers.Dense(128 * 64 * 64) (generator_input)
x = layers.LeakyReLU()(x)
x = layers.Reshape((64,64,128))(x)

x = layers.Conv2D(256, 5, padding='same')(x)
x = layers.LeakyReLU()(x)

x = layers.Conv2DTranspose(256, 4, strides=2, padding='same')(x)
x = layers.LeakyReLU()(x)

x = layers.Conv2D(256, 5, padding='same')(x)
x = layers.LeakyReLU()(x)
x = layers.Conv2D(256, 5, padding='same')(x)
x = layers.LeakyReLU()(x)

x = layers.Conv2D(channels, 7, activation='tanh', padding='same')(x)
generator = keras.models.Model(generator_input, x)
generator.summary()

discriminator_input = layers.Input(shape=(height, width, channels))
x = layers.Conv2D(128, 3)(discriminator_input)
x = layers.LeakyReLU()(x)
x = layers.Conv2D(128, 4, strides=2)(x)
x = layers.LeakyReLU()(x)
x = layers.Conv2D(128, 4, strides=2)(x)
x = layers.LeakyReLU()(x)
x = layers.Conv2D(128, 4, strides=2)(x)
x = layers.LeakyReLU()(x)
x = layers.Flatten()(x)

x = layers.Dropout(0.4)(x)

x = layers.Dense(1, activation='sigmoid')(x)
discriminator = keras.models.Model(discriminator_input, x)
discriminator.summary()
discriminator_optimizer = keras.optimizers.RMSprop(lr=0.0008, clipvalue=1.0, decay=1e-8)
discriminator.compile(optimizer = discriminator_optimizer, loss='binary_crossentropy')
discriminator.trainable = False

gan_input = keras.Input(shape = (latent_dim,))
gan_output = discriminator(generator(gan_input))
gan = keras.models.Model(gan_input, gan_output)

gan_optimizer = keras.optimizers.RMSprop(lr=0.0004, clipvalue=1.0, decay=1e-8)
gan.compile(optimizer=gan_optimizer, loss='binary_crossentropy')
 ########################################################################################
img_arr = np.zeros((326,128,128,3)).astype('float32')
images = []
for directory in os.listdir('/Users/oscargalindo/Desktop/Classes/CS 4371/Lab 4 (Ch.8)/data/'):
    if directory != '.DS_Store':
        print(directory)
        directory = os.path.join('/Users/oscargalindo/Desktop/Classes/CS 4371/Lab 4 (Ch.8)/data/', directory)
        x = image.load_img(directory, target_size=(128,128))
        x = image.img_to_array(x)
        x = x/255.0
        images.append(x)
        plt.imshow(x)

for x in (range(len(images))):
    img_arr[x] = images[x]        

 
#iterations = 10
#batch = 32
#save_dir = '/Users/oscargalindo/Desktop/Classes/CS 4371/Lab 4 (Ch.8)/produced_img'
# 
#start = 0
#for step in range(iterations):
#    random_latent_vectors = np.random.normal(size=(batch, latent_dim))
#    
#    generated_images = generator.predict(random_latent_vectors)
#    stop = start + batch
#    real_images = img_arr[start: stop]
#    combined_images = np.concatenate([generated_images, real_images])
#    
#    labels = np.concatenate([np.ones((batch,1)), np.zeros((batch,1))])
#    labels += 0.05 * np.random.random(labels.shape)
#    
#    d_loss = discriminator.train_on_batch(combined_images, labels)
#    
#    random_latent_vectors = np.random.normal(size=(batch, latent_dim))
#    misleading_targets = np.zeros((batch,1))
#    
#    a_loss = gan.train_on_batch(random_latent_vectors, misleading_targets)
#    
#    start+=batch
#    if start>len(images) - batch:
#        start = 0
#        
#    if step%2 == 0:
#        gan.save_weigths('gan.h5')
#        
#        print('disc. loss:', d_loss)
#        print('adver. loss:', a_loss)
#        
#        img = image.image_to_array(generated_images[0] * 255., scale=False)
#        img.save(os.path.join(save_dir,'fake_dog'+str(step)+'.png'))
#        
#        img = image.image_to_array(real_images[0] * 255., scale=False)
#        img.save(os.path.join(save_dir,'dog'+str(step)+'.png'))





