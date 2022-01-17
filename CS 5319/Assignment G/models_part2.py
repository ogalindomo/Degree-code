#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 18 08:51:50 2020

@author: oscargalindo
"""


import math,re,numpy as np

def get_data(package):
    f = open("/Users/oscargalindo/Desktop/Classes/CS 5319/Assignment G/"+package+"/subj."+package,"r",encoding='utf-8')
    f = f.read().split("\n")
    f = f[:len(f)-1]
    r = open("/Users/oscargalindo/Desktop/Classes/CS 5319/Assignment G/"+package+"/rating."+package,"r",encoding='utf-8')
    r = r.read().split("\n")
    r = r[:len(r)-1]
    r = [float(e) for e in r]
    return f,r

def count_in_class(R,lower,upper):
    count = 0
    for review in R:
        if review > lower and review <=upper:
            count+=1
    return count

def get_words(sentence):
    return re.findall(r'[a-z|A-Z]+\'*[a-z|A-Z]*', sentence)

def get_vocab(D):
    words = {}
    for document in D:
        for word in get_words(document):
            if not word in words:
                words[word]=1
            words[word] += 1
    return words

def get_documents_class(D,R,lower,upper):
    d = []
    for document in range(len(D)):
        if R[document] > lower and R[document] <= upper:
            d.append(D[document])
    return d

def dictionary_class_prob(V,class_number):
    probability_term = {}
    for term in V.keys():
        if not term in probability_term:
            probability_term[term] = [0]*class_number
    return probability_term

def get_add_class_terms(collection_vocab):
    s = 0
    for k in collection_vocab.keys():
        s += collection_vocab[k]
    return s
            
def trainNaiveBayes(D,R,threshold=0.5,class_number = 2):
    log_prior = [0]*class_number
    V = get_vocab(D)
    probability_term = dictionary_class_prob(V,class_number)
    for class_num in range(class_number):
        class_documents = count_in_class(R, threshold*class_num, threshold*(class_num+1))
        total_documents = len(D)
        log_prior[class_num] = abs(math.log(class_documents/total_documents,10))
        class_collection = get_documents_class(D,R,threshold*class_num,threshold*(class_num+1))
        collection_vocab = get_vocab(class_collection)
        total_counts_class = get_add_class_terms(collection_vocab)
        for term in V.keys():
            numerator = collection_vocab[term] if term in collection_vocab else 0
            probability_term[term][class_num] = (numerator+1)/(total_counts_class+len(V))
    return log_prior,probability_term,V

def test_naive_bayes(test_doc,log_prior,probability_term,class_num,V):
    s = [0]*class_num
    for c in range(class_num):
        s[c] = log_prior[c]
        for term in get_words(test_doc):
            if term in V:
                s[c] *= probability_term[term][c]
    print(s)
    return np.argmax(s)

def get_class(value,threshold):
    return int(math.floor(value/threshold))

def test_naive_bayes_model(package,threshold,log_prior,probability_term,class_num,V):
    docs,reviews = get_data(package)
    classification  = [[0,0],[0,0]] #TP,FP,FN,TN
    for i in range(len(docs)):
        ground_truth = get_class(reviews[i], threshold)
        predicted = test_naive_bayes(docs[i], log_prior, probability_term, class_num, V)
        classification[predicted,ground_truth] += 1
    return classification
        
if __name__=="__main__":
    classes_threshold = 1/2
    classes = 2
    reviews,scores = get_data("Dennis+Schwartz")
    reviews_1,scores_1 = get_data("James+Berardinelli")
    log_prior,probability_term,V = trainNaiveBayes(reviews+reviews_1,scores+scores_1,classes_threshold,classes)
    results = test_naive_bayes_model("Steve+Rhodes",classes_threshold,log_prior, probability_term, classes, V)
    
    