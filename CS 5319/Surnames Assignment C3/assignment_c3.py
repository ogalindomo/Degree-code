# Angel F. Garcia Contreras, UTEP, July 2020
# Speech and Language Processing
# Assignment C3: Introduction to Sequence Modeling

import itertools
import math
import string
import sys
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

def read_data(fname):
    """Read names from file (one name per line)"""
    data = []
    with open(fname, mode="r", encoding="utf-8") as input_file:
        data = [line.lower().strip() for line in input_file]
    return data

def generate_bigrams(word):
    """Generator for bigrams in word
    Includes starting (@) and ending (#) symbols
    """
    lower = "@" + word
    upper = word + "#"
    
    bigram_gen = map(lambda l,u: l+u, lower, upper)

    for bigram in bigram_gen:
        yield bigram

def compute_frequencies(data):
    """data is an iterable.
    Frequency counts for both Bigrams and Unigrams.
    """
    all_chars = "@" + string.ascii_lowercase + " #"
    bigram_freqs = {a+b:0 for (a,b) in itertools.product(
            all_chars[:-1], all_chars[1:])}
    unigram_freqs = {a:0 for a in all_chars}

    for name in data:
        for letter in "@" + name + "#":

            if letter in unigram_freqs:
                unigram_freqs[letter] += 1
            else: 
                unigram_freqs[letter] = 1
        for bigram in generate_bigrams(name):
            if bigram in bigram_freqs:
                bigram_freqs[bigram] += 1
            else:
                bigram_freqs[bigram] = 1

    return bigram_freqs, unigram_freqs

def compute_probabilities_add_k(bigram_freq, letter_freq, k=1.0):
    """Compute bigram conditional probabilities,
    using add-k smoothing.

    Basic formula:
        P(b | a) = C(ab) / C(a)
    With add-k:
        P(b | a) = (C(ab) + k) / (C(a) + k*N)
    """
    probs = {a+b:0 for (a,b) in itertools.product(
            string.ascii_lowercase + " @", 
            string.ascii_lowercase + " #")}

    for bigram in bigram_freq.keys():
        a = bigram[0]
        b = bigram[1]
        C_ab = bigram_freq[bigram]
        C_a = letter_freq[a]
        probs[a+b] = (C_ab + k)/(C_a  + k * len(letter_freq))

    return probs

def get_name_probabilities(model_probs, test_data):
    """Compute the probabilities for all names in test_data,
    based on the bigram-based model model_probs
    """
    # It is possible that test_data has unknown bigrams.
    # This sets a default value for unknown bigrams 
    min_p = min(model_probs.values())

    for name in test_data:
        p = 1
        for bigram in generate_bigrams(name):
            p *= model_probs.get(bigram, min_p)
        
        yield name, p

# Create auto-completed names for each name in test_data
def get_name_predictions(model_probs, test_data):
    """Auto-complete predictor for names.
    Find the next letters for each name in test_data,
    based on the higest-probability bigrams
    """
    # It is possible that test_data has unknown bigrams.
    # This sets a default value for unknown bigrams 
    min_p = min(model_probs.values())

    char_list = string.ascii_lowercase + " #"
    for name in test_data:
        p = 1
        for bigram in generate_bigrams(name):
            p *= model_probs[bigram] if bigram in model_probs else min_p
        
        new_name = name
        while new_name[-1] != "#":
            possible_bigrams = (new_name[-1] + n for n in char_list)
            
            max_prob = min_p
            best_bigram = ""

            # Generator of (bigram, prob) tuples
            all_bigrams = ((b, model_probs.get(b, min_p))
                    for b in possible_bigrams)

            (best_bigram, max_prob) = max(all_bigrams, 
                    key=lambda t: t[1]) # Compare by probability

            # Update name, probability
            p *= max_prob
            new_name += best_bigram[-1]
        
        yield name, new_name[:-1], p
    
def get_cross_entropy(p_probs, m_probs):
    """Compute cross-entropy between a predicted & actual models
    """
    return -sum((p*math.log2(m) for (p, m)
            in zip(p_probs.values(), m_probs.values())))/len(p_probs)

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
    return vector

def vectorize_single_country(list_of_pairs,label):
    y = np.zeros((len(list_of_pairs),))
    x = np.zeros((len(list_of_pairs),27 * 27))
    xlabels = []
    i = 0
    for pair in list_of_pairs:
        vector = encode(pair[0].lower())
        y_label = label
         
        #setting variables 
        y[i] = y_label
        x[i] += vector
        xlabels.append(pair[0])
        i+=1
    return np.array(xlabels),x,y

def train(model,x_train,y_train):
    model.fit(x_train,y_train)

def predict(model,x):
    return model.predict(x)

def classify(predicted,threshold):
    predicted[predicted < threshold] = 0
    predicted[predicted >= threshold] = 1
    
def get_predicted(y_predicted,x):
    predicted = []
    for i in range(y_predicted.shape[0]):
        if y_predicted[i] == 1:
            predicted.append(x[i])
    return predicted

if __name__ == "__main__":
    # if len(sys.argv) != 3:
    #     print("Usage: python3 linear_classifier.py training_file test_file" )
    #     sys.exit()

    # # # Load files
    # # train_data = read_data(sys.argv[1])

    # # m_bigram_freq, m_letter_freq = compute_frequencies(train_data)

    language = 'Russian'
    threshold = 0.5
    p = 10
    ################ Train Same File ###################
    src = './surnames-eng-train.csv'
    l = read_file(src)
    x_labels_tr,x,y_actual = vectorize_single_country(l,1)
    model = LinearRegression()
    train(model,x,y_actual)
    y_predicted = predict(model, x)
    classify(y_predicted, threshold)
    weights = model.coef_
    x_actual = x_labels_tr.copy()
    x_predicted = get_predicted(y_predicted,x_labels_tr)
    
    m_bi, m_letter = compute_frequencies(x_actual)
    p_bi, p_letter = compute_frequencies(x_predicted)
    m = compute_probabilities_add_k(m_bi, m_letter)
    p = compute_probabilities_add_k(p_bi, p_letter)
    c_e = get_cross_entropy(p, m)
    print("Cross-entropy:",c_e)
    
    ################ Train Dev File ###################
    src = './surnames-eng-train.csv'
    second_src = './surnames-eng-dev.csv'
    l = read_file(src)
    l_1 = read_file(second_src)
    x_labels_tr,x,y_actual = vectorize_single_country(l,1)
    x_labels_tr_1,x_1,y_actual_1 = vectorize_single_country(l_1,1)
    model = LinearRegression()
    train(model,x,y_actual)
    y_predicted = predict(model, x_1)
    classify(y_predicted, threshold)
    weights = model.coef_
    x_actual = x_labels_tr_1.copy()
    x_predicted = get_predicted(y_predicted,x_labels_tr_1)
    
    m_bi, m_letter = compute_frequencies(x_labels_tr)
    p_bi, p_letter = compute_frequencies(x_predicted)
    m = compute_probabilities_add_k(m_bi, m_letter)
    p = compute_probabilities_add_k(p_bi, p_letter)
    print("Cross-entropy:",get_cross_entropy(p, m))
    
    ################ Train Russian File ###################
    src = './surnames-eng-train.csv'
    second_src = './surnames-rus-dev.csv'
    l = read_file(src)
    l_1 = read_file(second_src)
    x_labels_tr,x,y_actual = vectorize_single_country(l,1)
    x_labels_tr_1,x_1,y_actual_1 = vectorize_single_country(l_1,0)
    model = LinearRegression()
    train(model,x,y_actual)
    y_predicted = predict(model, x_1)
    classify(y_predicted, threshold)
    weights = model.coef_
    x_actual = x_labels_tr_1.copy()
    x_predicted = get_predicted(y_predicted,x_labels_tr_1)
    
    m_bi, m_letter = compute_frequencies(x_labels_tr)
    p_bi, p_letter = compute_frequencies(x_predicted)
    m = compute_probabilities_add_k(m_bi, m_letter)
    p = compute_probabilities_add_k(p_bi, p_letter)
    print("Cross-entropy:",get_cross_entropy(p, m))
    
    
    

