#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  4 11:56:43 2020

@author: oscargalindo
"""
import numpy as np, matplotlib.pyplot as plt
import copy
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix

def read_file(src):
    f = open(src,encoding='utf-8').readlines()
    l = []
    for e in f:
        l.append(e.strip('\n').split(','))
    return l

def vectorize(list_of_pairs,country):
    y = np.zeros((len(list_of_pairs),))
    x = np.zeros((len(list_of_pairs),27))
    xlabels = []
    i = 0
    for pair in list_of_pairs:
        vector = encode(pair[0])
        y_label = 1 if pair[1] == country else 0
         
        #setting variables 
        y[i] = y_label
        x[i] += vector
        xlabels.append(pair[0])
        i+=1
    return xlabels,x,y

def train(model,x_train,y_train):
    model.fit(x_train,y_train)

def predict(model,x):
    return model.predict(x)

def classify(predicted,threshold):
    predicted[predicted < threshold] = 0
    predicted[predicted >= threshold] = 1

def print_weights(model):
    print("################### Weights #######################")
    print("Intercept:",model.intercept_)
    print("Weights:",model.coef_)
    print("###################################################")
    
def get_stats(actual,prediction,language,title):
    print("####################",title,"####################")
    conf_m = confusion_matrix(actual, prediction)
    print(classification_report(actual,prediction))
    print(conf_m)
    print("#################################################")
    fig, ax = plt.subplots(figsize=(8, 8))
    ax.set_title(title)
    ax.imshow(conf_m)
    ax.grid(False)
    ax.xaxis.set(ticks=(0, 1), ticklabels=('Actual '+language,'Actual Non-'+language))
    ax.yaxis.set(ticks=(0, 1), ticklabels=('Predicted '+language, 'Predicted Non-'+language))
    ax.set_ylim(1.5, -0.5)
    for i in range(2):
        for j in range(2):
            ax.text(i, j, conf_m[i-1, j-1], ha='center', va='center', color='red')
    plt.show()
    plt.close()
    
def print_to_file(y_pred, y_act, x_labels, title,language):
    results = open("{}DataResults.txt".format(title), "w", encoding = "utf-8")

    #setting up string holders for each category
    template = "{}\nName\tPrediction\n"
    true_pos = template.format("***************** True Positives *****************")
    true_neg = template.format("***************** True Negatives *****************")
    false_pos = template.format("***************** False Positives ***************")
    false_neg = template.format("***************** False Negatives ***************")
    
    lineformat = "{}, {}\n"
    for i in range(len(y_act)):
        line = lineformat.format(x_labels[i], y_pred[i])
        #determining which file to write to
        if y_act[i] != y_pred[i]:
            if y_pred[i] == 1:
                false_pos = false_pos + line
            else:
                false_neg = false_neg + line
        else:
            if y_pred[i] == 1:
                true_pos = true_pos + line
            else:
                true_neg = true_neg + line
    
    results.write(true_pos)
    results.write(true_neg)
    results.write(false_pos)
    results.write(false_neg)
    results.close()

#Takes in a name and inserts each character into its slot 
#and normalizes the vector 
def encode(name):
    vector = np.zeros(27, dtype = float)
    for character in name:
        index = ord(character.lower()) - ord('a')
        #For characters falling outside of normal range
        if index < 0 or index > 25:
            vector[-1] +=1
        else:
            vector[index]+=1
        #Normalize
        # vector = vector / len(name)
    return vector
    
def get_f(y_act, y_pred):
    pos_act = np.argwhere(y_act)
    pos_pred = np.argwhere(y_pred)
    
    true_pos = np.intersect1d(pos_act, pos_pred)
    try:
        precision = float(true_pos.shape[0]/pos_pred.shape[0])
    except: 
        precision = 0
    recall = float(true_pos.shape[0]/pos_act.shape[0])
    
    #print("Precision: %.2f\t Recall: %.2f" % (precision, recall))
    try:
        return 2 * ((precision * recall)/(precision + recall))
    except:
        return float("-inf")

def test_thresholds(model, y_act, y_pred):
    best_f = 0
    best_t = 0
    for ind  in range(1, 100, 1):
        threshold = .01  * ind
        y_pred_copy = copy.deepcopy(y_pred)
        y_pred_copy[y_pred_copy < threshold] = 0
        y_pred_copy[y_pred_copy >= threshold] = 1
        f_meas = get_f(y_act, y_pred_copy)
        if f_meas > best_f:
            best_f = f_meas
            best_t = threshold
    return best_t

if __name__=="__main__":
    language = 'Russian'
    model = LinearRegression()
    ################Train###################
    src = './surnames-dev.csv'
    l = read_file(src)
    x_labels_tr,x,y = vectorize(l,language)
    train(model,x,y)
    print_weights(model)
    y_p = predict(model, x)
    threshold = test_thresholds(model, y, y_p)
    print("Best Threshold:",threshold)
    classify(y_p, threshold)
    get_stats(y, y_p, language,"Train Set")
    print_to_file(y_p, y, x_labels_tr, "Training",language)
    #################Test####################
    src = './test_surnames.txt'
    l_t = read_file(src)
    x_labels_te,x_t,y_t = vectorize(l_t,language)
    y_p = predict(model,x_t)
    classify(y_p, threshold)
    get_stats(y_t,y_p,language,"Test Set")
    print_to_file(y_p, y_t, x_labels_te, "Testing",language)
    #########################################
    