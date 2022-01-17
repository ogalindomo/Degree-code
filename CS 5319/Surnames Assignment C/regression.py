# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 16:25:24 2020

@author: Aaron
"""

# -*- coding: utf-8 -*-
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
    x = np.zeros((len(list_of_pairs),27 * 27))
    xlabels = []
    i = 0
    for pair in list_of_pairs:
        vector = encode(pair[0].lower())
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

"""
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
"""

def encode(name):
    vector = np.zeros(27 * 27, dtype = float)
    for char_ind in range(len(name) -1):
        first_let = (ord(name[char_ind]) - ord('a')) 
        second_let = (ord(name[char_ind + 1]) - ord('a'))
        if first_let < 0 or first_let > 25: 
            first_let = 26
        if second_let < 0 or second_let > 25: 
            second_let = 26
        vector[(first_let * 27) + second_let] += 1
    #Normalize Regular
    # vector = vector / (len(name) - 1)
    #Normalize Smooth
    # vector += 1
    # vector = vector / (len(name)-1+vector.shape[0]-1)
    return vector


# def smooth(k,x)
#     for i in range(se)
    
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
    
def best_pairs(A, descending = 1, amount = 10):
    if descending:
        ind = np.argsort(A)[::-1][:amount]
    else: 
        ind = np.argsort(A)[:amount]
    for i in ind: 
        print(i)
        first_let, second_let = i//27, i%27
        if first_let ==26 or second_let == 26:
            print("Special Character\n")
            continue
        first_let += ord('a')
        second_let += ord('a')
        print("{}{}\n".format(chr(first_let), chr(second_let)))
        

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

def clean_for_binary_classification(l,origin1,origin2):
    clean = []
    for e in l:
        if e[-1] == origin1 or e[-1] == origin2:
            clean.append(e)
    return clean

def most_frequent_bigrams(label,x,y,k,p):
    print("############## Most Common Bigrams ##############")
    counts = np.zeros(27*27)
    for i in range(y.shape[0]):
        if label == y[i]:
            counts += x[i]
    pairs = []
    for _ in range(p):
        most_index = np.argmax(counts)
        print("Most frequent bigram: ",chr(ord('a')+most_index//27),chr(ord('a')+most_index%27),"with counts: ",counts[most_index])
        counts[most_index] = -1
        pairs.append(chr(ord('a')+most_index//27)+chr(ord('a')+most_index%27))
    for _ in range(p,k):
        most_index = np.argmax(counts)
        counts[most_index] = -1
        pairs.append(chr(ord('a')+most_index//27)+chr(ord('a')+most_index%27))

    return pairs,counts

def get_counts(label,x):
    counts = np.zeros(27*27)
    for i in range(y.shape[0]):
        if label == y[i]:
            counts += x[i]
    return counts

def compare_most_used(l1,l2):
    compared = []
    for e in l2: 
        if e in l1:
            compared.append(e)
    return compared

def add_to_list(data,l):
    for e in data:
        l.append(e)
        
def normalize_counts(x,k):
    for i in range(x.shape[0]):
        p = x[i].reshape((27,27))
        p += k
        for firstletter in range(27):
            total_c = np.sum(p[firstletter,:]) 
            if total_c > 0:
                p[firstletter] /= total_c
        p=p.reshape(27*27)
        x[i] = p
    return x

def use_k(x,y):
    m_final = None
    conf_m_f = np.zeros((2,2))
    y_p_f = None
    threshold_f = 0
    k_f = 0
    for k in range(0,100):
        x_original = x.copy()
        k /= 100
        model = LinearRegression()
        normalize_counts(x_original, k)
        train(model,x_original,y)
        y_p = predict(model, x)
        threshold = test_thresholds(model, y, y_p)
        classify(y_p, threshold)
        conf_m = confusion_matrix(y, y_p)
        if conf_m[-1,-1] > conf_m_f[-1,-1] or conf_m[0,0] > conf_m_f[0,0]:
            m_final = model
            conf_m_f = conf_m
            y_p_f = y_p
            threshold_f = threshold
            k_f = k
    return m_final,y_p_f,threshold_f,k_f  

def get_possible_next(name,x,k=6):
    for _ in range(k):
        i = np.argmax(x[ord(name[-1])-ord('a')])
        x[i] -= 1
        name += chr(i+ord('a')) if i < 26 else "<sc>"
        print(name)

if __name__=="__main__":
    language = 'Russian'
    other_language = 'English'
    k = 250
    p = 10
    ################Train###################
    src = './surnames-dev.csv'
    # extra_src = './english_surnames.txt'
    l = read_file(src)
    # l_1 = read_file(extra_src)
    # add_to_list(l_1[:len(l_1)//4],l)
    l = clean_for_binary_classification(l,language,other_language)
    x_labels_tr,x,y = vectorize(l,language)
    # print(x)
    # normalize_counts(x, k=0) 
    # bigrams,count = most_frequent_bigrams(1,x,y,k,p)
    # bigrams_1,count_1 = most_frequent_bigrams(0,x,y,k,p)
    # compared = compare_most_used(bigrams, bigrams_1)
    print(x)
    ############ Usual ###########
    model = LinearRegression()
    train(model,x,y)
    y_p = predict(model, x)
    threshold = test_thresholds(model, y, y_p)
    classify(y_p, threshold)
    # ############ K-smoothing #########
    # model,y_p,threshold,k = use_k(x,y)
    # print_weights(model)
    #################################
    # print("Best Threshold:",threshold)
    # print("Best k:",k)
    # get_stats(y, y_p, language,"Train Set")
    # print_to_file(y_p, y, x_labels_tr, "Training",language)
    # counts = get_counts(0,x)
    # counts = counts.reshape(27,27)
    # words = ['Lou','Ber','Cul','Ede','Zjo']
    # for w in words:
    #     print('################'+w+'###############')
    #     print('------------Counts for '+w+'-------------')
    #     get_possible_next(w,counts)
    #     print('------------Coefficients------------')
    #     get_possible_next(w,model.coef_)
    
    # print(model.coef_)
    # #################Test####################
    # src = './test_surnames.txt'
    # l_t = read_file(src)
    # l_t = clean_for_binary_classification(l_t, language, other_language)
    # x_labels_te,x_t,y_t = vectorize(l_t,language)
    # y_p = predict(model,x_t)
    # classify(y_p, threshold)
    # get_stats(y_t,y_p,language,"Test Set")
    # print_to_file(y_p, y_t, x_labels_te, "Testing",language)
    # ########################################
    
    