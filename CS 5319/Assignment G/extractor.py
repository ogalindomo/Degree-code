#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 18:49:53 2020

@author: oscargalindo
"""
# Nigel Ward, September 2018
# Code Skeleton for SLP  Assignment D: Sentiment Analysis

import numpy as np    # might instead use scipy or scikit-learn
import re, sys

interestingWords = {'great', 'good', 'bad', 'still'}
interestingPairs = {'not bad', 'not good'}
interestingClasses = {'JJ', 'NN', '8L'}

def featurizeReview(reviewString):
  words = reviewString.split()  # lazily, don't properly tokenize or lemmatize
  feats = np.zeros(6)
  feats[0] = 1     # a constant term, for lstsq
  feats[1] = len(re.findall(' good ', reviewString, re.IGNORECASE))
  feats[2] = len(re.findall(' bad ', reviewString, re.IGNORECASE))
  feats[3] = len(re.findall(' still ', reviewString, re.IGNORECASE))
  # lazy way to do bigrams
  feats[4] = len(re.findall(' not bad ', reviewString, re.IGNORECASE))
  # lazy way to do a word class
  feats[5] = len(re.findall('( the )|( a )|( an )', reviewString, re.IGNORECASE))
  return feats

def readReviewSet(directory):
   reviewsFileName = '%s/subj.%s' % (directory, directory)
   labelsFileName = '%s/rating.%s' % (directory, directory)  
   reviewsFp = open(reviewsFileName, 'r')
   labelsFp = open(labelsFileName, 'r')
   featureMatrix = []
   for review in reviewsFp.readlines():
       feats = featurizeReview(review)
       featureMatrix.append(feats)
   labelVec = [] 
   for label in labelsFp.readlines():
     labelVec.append(float(label))
   return featureMatrix, labelVec

def buildModel(features, targets):  # least squares
    f = np.array(features)
    t = np.array(targets)
    model, residuals, rank, svs = np.linalg.lstsq(f, t)
    print('the model is')
    print(model)
    return model

def applyModel(model, features):
   predictions = np.matmul(features, model)
   return predictions

def printInfo(index, label, pred, data):
   print ('   for story #%d: label= %.2f, pred= %.2f' % (index, label, pred))
   print ('      features: ')
   print (data)

def evalPredictions(predictions, targets, data, descriptor):
   deltas = predictions - targets
   mse = np.matmul(deltas, deltas) / len(predictions)
   print ('\nfor %s, mse is %.3f' % (descriptor, mse))
   mae = sum(abs(deltas)) / len(predictions)
   print ('  (and the mae is %.3f)' %  mae)

def showWorst(predictions, targets, data):
   deltas = predictions - targets
   worstUnder = np.argmin(deltas)
   worstOver = np.argmax(deltas)
   print('worst underestimate and worst overestimate:')
   printInfo(worstUnder, targets[worstUnder], predictions[worstUnder], data[worstUnder])
   printInfo(worstOver, targets[worstOver], predictions[worstOver], data[worstOver])

def read(directory):
   reviewsFileName = '%s/subj.%s' % (directory, directory)
   labelsFileName = '%s/rating.%s' % (directory, directory)  
   reviewsFp = open(reviewsFileName, 'r')
   labelsFp = open(labelsFileName, 'r')
   featureMatrix = []
   for review in reviewsFp.readlines():
       featureMatrix.append(review)
   return featureMatrix 

def countUniqueWords(directory):
    sentences = read(directory)
    d = dict()
    for sentence in sentences:
        sentence = re.findall(r'[a-z|A-Z]+\'*[a-z|A-Z]*', sentence)
        for word in sentence:
            if not word in d:
                d[word] = 1
            else:
                d[word] += 1
    return d

#=== main ========================================================

trData, trLabels = readReviewSet('Dennis+Schwartz') # lazily omit Dennis 
model = buildModel(trData, trLabels)
sentences = read('James+Berardinelli')
unique = countUniqueWords('Dennis+Schwartz')
unique = {k: v for k, v in sorted(unique.items(), key=lambda item: item[1],reverse = True)}
# if len(sys.argv) >= 2 and (sys.argv[1] == 'yesThisReallyIsTheFinalRun'):
#   testData, testLabels = readReviewSet('Steve+Rhodes')
# else:
#   testData, testLabels = readReviewSet('Scott+Renshaw')  # devtest

# predictions = applyModel(model, testData)
# evalPredictions(predictions, testLabels, testData, 'dummy model')
# showWorst(predictions, testLabels, testData)

# baselinePredictions = np.ones(len(testLabels)) * np.average(testLabels)
# evalPredictions(baselinePredictions, testLabels, testData, 'baseline (average)')


# output

#the model is
#[ 0.60081999 -0.01981207 -0.08698933 -0.00183384  0.07853322  0.00191875]
#
#for dummy model, mse is 0.042
#  (and the mae is 0.164)
#worst underestimate and worst overestimate:
#   for story #272: label= 0.50, pred= -0.13
#      features:  [  1.   1.   9.   1.   0.  36.]
# understandable since the name of the movie is "very bad things"
#   for story #2: label= 0.00, pred= 0.66
#      features:  [  1.   1.   0.   0.   0.  40.]
# understandable since the word "good" appears, and not much else that's informative 

#for baseline (average), mse is 0.038
#  (and the mae is 0.157)