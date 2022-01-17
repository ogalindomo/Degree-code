# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 18:37:12 2020

@author: Aaron
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 09:57:25 2020

@author: Aaron
"""

# Nigel Ward, UTEP, October 2018
# Updated by Angel Garcia, UTEP, July 2020
# Speech and Language Processing
# Assignment E: Information Retrieval

# This is just a skeleton that needs to be fleshed out.
# It is not intended as an example of good Python style

import numpy as np
import sys
import re 
import math

def parseAlternatingLinesFile(file):
    """ read a sequence of pairs of lines
    e.g. text of webpage(s), name/URL
    """
    sequenceA = []
    sequenceB = []

    with open(file, mode="r", encoding="utf-8") as f:
        for i,line in enumerate(f):
            if i % 2:
                sequenceB.append(line.strip())
            else:
                sequenceA.append(line.strip())

    return sequenceA, sequenceB

def generateCharTrigrams(text):
    """Generate Character Trigrams from Text"""
    for i in range(len(text)-3+1):
        yield text[i:i+3]

def computeFeatures(text, trigramInventory):        
    """Computes the count of trigrams.
    Trigrams can catch some similarities
    (e.g. between  "social" and "societal" etc.)
    
    But really should be replaced with something better
    """
    counts = {}
    for trigram in generateCharTrigrams(text):
        if trigram in trigramInventory:
            counts[trigram] = (1 if trigram not in counts
                     else counts[trigram] + 1)   
    return counts
   

def computeSimilarity(dict1, dict2):
    """Compute the similarity between 2 dictionaries of trigtrams

    Ad-hoc and inefficient.
    """
    
    keys_d1 = set(dict1.keys())
    keys_d2 = set(dict2.keys())
    matches = keys_d1 & keys_d2
    
    similarity = len(matches) / len(dict2)
    #print(f"Similarity: {similarity:.3f}")

    return similarity

def retrieve(queries, trigramInventory, archive):     
    """returns an array: for each query, the top 3 results found"""
    top3sets = []
    for query in queries:
        #print(f"query is {query}")
        
        q = computeFeatures(query, trigramInventory)
        #print(f"query features are \n{q}")

        similarities = [computeSimilarity(q, d) for d in archive] 
        
        #print(similarities)
        top3indices = np.argsort(similarities)[0:3]
        #print(f"top three indices are {top3indices}")
        
        top3sets.append(top3indices)  
    return top3sets

def valueOfSuggestion(result, position, targets):
    weight = [1.0, .5, .25]
    if result in targets:
        return weight[max(position, targets.index(result))]
    else:
        return 0


def scoreResults(results, targets):   #-----------------------------
    merits = [valueOfSuggestion(results[i], i, targets) 
            for i in range(3)]
    return sum(merits)


def scoreAllResults(queries, results, targets, descriptor,verbose=False):   
    print()
    print(f"Scores for {descriptor}")
    scores = [(q, r, t, scoreResults(r, t)) 
            for q, r, t in zip(queries, results, targets)]
    if verbose:
        for q, r, t, s in scores:
            print(f"for query: {q}")
            print(f"  results = \n{r}")
            print(f"  targets = \n{t}")
            print(f"  score = {s:.3f}")

    all_scores = [s for _,_,_,s in scores]
    overallScore = np.mean(all_scores)
    print(f"All Scores:\n{all_scores}")
    print(f"Overall Score: {overallScore:.3f}")

    return overallScore

def pruneUniqueNgrams(ngrams):
    twoOrMore = {} 
    print("Before pruning: " +
            f"{len(ngrams)} ngrams across all documents")

    twoOrMore = {k:v for k,v in ngrams.items() if ngrams[k] > 1}

    print("After pruning: " +
            f"{len(twoOrMore)} ngrams across all documents")
    
    return twoOrMore

def targetNumbers(targets, nameInventory):
    """targets is a list of strings, each a sequence of names"""
    targetIDs = []
    for target in targets:
      threeNumbers = [] 
      for name in target.split():
          threeNumbers.append(nameInventory.index(name))
      targetIDs.append(threeNumbers)
    return targetIDs

######################## Added Code ###########################
######################## TF-IDF ######################
def findWordsByDoc(doc):
    return re.findall(r'[a-z|A-Z]+\'*[a-z|A-Z]*', doc)

def findWords(contents):
    expression = re.compile("[a-z|A-Z]+\'*[a-z|A-Z]*")
    words = {}
    for document in range(len(contents)):
        w = re.findall(expression, contents[document])
        for word in w:
            if not word in words:
                words[word] = [0]*len(contents)
        for word in w:
            words[word][document] += 1
    return words

def findUniqueWords(words):
    unique_words = []
    for w in words:
        if not w in unique_words:
            unique_words.append(w)
    return unique_words

def findWordCountsByDoc(contents):
    expression = re.compile("[a-z|A-Z]+\'*[a-z|A-Z]*")
    words = {}
    for document in range(len(contents)):
        w = re.findall(expression, contents[document])
        unique = findUniqueWords(w)
        for word in unique:
            if not word in words:
                words[word] = [0]*len(contents)
        for word in unique:
            words[word][document] += 1
    
    return words

def findAllNgrams(contents):
    allTrigrams = {}
    for text in contents:
        for tri in generateCharTrigrams(text):
            allTrigrams[tri] = (1 if tri not in allTrigrams
                    else allTrigrams[tri] + 1)
    return allTrigrams   

def retrieveTFIDF(queries,word_frequency,term_document_frequency,archive):
    top3sets = []
    for query in queries:
        q = findWordsByDoc(query)
        similarities = [similaritiesTDIDF(len(archive),q,word_frequency,term_document_frequency,archive[doc],doc) 
                        for doc in range(len(archive))]
        top3indices = np.argsort(similarities)[::-1][:3]
        top3sets.append(top3indices)
    return top3sets

def similaritiesTDIDF(archive_size,query,word_frequency,term_document_frequency,doc,doc_index):
    value = 0
    for word in query:
        if word in doc:
            query_weight = math.log(1 + (archive_size/sum(term_document_frequency[word])))
            term_weight = 1 + math.log(word_frequency[word][doc_index])
            value += term_weight * query_weight
    return value

######################## Cosine Similarity ######################
def cosine_similarity(query,doc):
    numerator = 0
    denominator = 0
    for key in query.keys():
        if key in doc:
            numerator += query[key]*doc[key]
    s = 0
    for key in query.keys():
        s+=query[key]**2
    denominator = math.sqrt(s)
    s = 0
    for key in doc.keys():
        s+=doc[key]**2
    denominator *= s
    return (numerator/denominator)

def getSimilarities(query,contents, option):
    s = []
    for doc in contents:
        if option == "Cosine":
            r = cosine_similarity(query, doc)
        else:
            r = Tanimoto_sim(query, doc)
        s.append(r)
    normalize(s)
    return s

def getWordsOfDocument(doc):
    words = findWordsByDoc(doc)
    w = dict()
    for word in words:
        if not word in w:
            w[word] = 1
        else:
            w[word] += 1
    return w

def getWordsOfDocumentSW(doc):
    words = findWordsByDoc(doc)
    w = dict()
    for word in words:
        if not inStopWords(word):
            if not word in w:
                w[word] = 1
            else:
                w[word] += 1
    return w
        
def getWordsOfDocInCollection(contents,stop_words=False):
    docs =[]
    for doc in contents:
        if not stop_words:
            docs.append(getWordsOfDocument(doc))
        else:
            docs.append(getWordsOfDocumentSW(doc))
    return docs

def normalize(vector):
    s = sum(vector)
    if s > 0:
        for i in range(len(vector)):
            vector[i] = vector[i]/s
        

def retrieveCosSim(queries,docs,stop_words = False, option = "Cosine"):
    top3sets = []
    docs_words = getWordsOfDocInCollection(docs)
    for q in queries:
        if not stop_words:
            q_words = getWordsOfDocument(q)
        else:
            q_words = getWordsOfDocumentSW(q)
        similarities=getSimilarities(q_words,docs_words, option)
        top3indices = np.argsort(similarities)[::-1][:3]
        top3sets.append(top3indices)
    return top3sets

######################## Stop List ######################
def inStopWords(word):
    stop_words,_ = parseAlternatingLinesFile('./stopwords.txt')
    #List taken from: https://www.lextek.com/manuals/onix/stopwords1.html
    return word in stop_words

######################## 
#Tanimoto Similarity 

def Tanimoto_sim(query, doc):
    in_common = 0
    not_in_common = 0
    for key in query.keys():
        if key in doc:
            not_in_common  += abs(query[key] - doc[key])
            in_common += min(query[key], doc[key])
        else:
            not_in_common += query[key]
    for label, value in doc.items():
        if label not in query.keys():
            not_in_common += value
    if not_in_common == in_common: 
        not_in_common +=1
    return (in_common/(not_in_common - in_common))

######## TF #########
def termFrequenciesScore(query,contents):
  scores = [0]*len(contents)
  q = getWordsOfDocument(query)
  for doc in range(len(contents)):
    words = getWordsOfDocument(contents[doc])
    for term in q.keys():
        if term in words:
          scores[doc] += words[term]
  return scores

def retrieveTF(queries,contents):
    top3sets = []
    for q in queries:
        similarities = termFrequenciesScore(q, contents)
        top3indices = np.argsort(similarities)[::-1][:3]
        top3sets.append(top3indices)
    return top3sets
  

#Ideas: Implement a direct comparison of term counts of the query words, take out words that are too simple with the stop word list

#Implement a combination of the cosine similarity with TF by computing the denominator of cosine similiarity and dividing by the total term counts of the words.


##########################################################
if __name__ == "__main__":

    # if len(sys.argv) != 3:
    #     print("Usage: python irStub.py " +
    #           "<document file>" +
    #           "<queries file>")
    #     sys.exit()
    
    document_file = "./csFaculty.txt"
    queries = './trainingQueries.txt'
    sys.argv = ['']*3
    sys.argv[1] = document_file
    sys.argv[2] = queries
    print("......... irStub .........")
    contents, names =  parseAlternatingLinesFile(sys.argv[1]) 
    
    print(f"read in pages for {names}")
    # #################################
    # trigramInventory = pruneUniqueNgrams(findAllNgrams(contents))    
    # archive = [computeFeatures(line, trigramInventory) 
    #         for line in contents]

    # queries, targets = parseAlternatingLinesFile(sys.argv[2])
    
    # targetIDs = targetNumbers(targets, names)
    # results = retrieve(queries, trigramInventory, archive)
    # modelName = "silly character trigram model"
    
    # scoreAllResults(queries, results, targetIDs, 
    #         f"{modelName} on {sys.argv[1]}")
    ############# TF Similarities #############
    queries, targets = parseAlternatingLinesFile(sys.argv[2])
    print(termFrequenciesScore(queries[0],contents))
    targetIDs = targetNumbers(targets, names)
    results = retrieveTF(queries, contents)
    modelName = "Simple Term Frequency Model"
    scoreAllResults(queries, results, targetIDs, 
            f"{modelName} on {sys.argv[1]}")
    ############ TF-IDF #############
    word_frequency = findWords(contents)
    term_document_frequency = findWordCountsByDoc(contents)
    word_frequencies = findAllNgrams(contents)    
    archive = [findUniqueWords(findWordsByDoc(line)) 
            for line in contents]
    queries, targets = parseAlternatingLinesFile(sys.argv[2])
    targetIDs = targetNumbers(targets, names)
    results = retrieveTFIDF(queries,word_frequency,term_document_frequency,archive)
    modelName = "TF-IDF Model"
    scoreAllResults(queries, results, targetIDs, 
            f"{modelName} on {sys.argv[1]}")
    ########## Cosine Similarity ###########
    docs_words = getWordsOfDocInCollection(contents)
    queries, targets = parseAlternatingLinesFile(sys.argv[2])
    results = retrieveCosSim(queries,contents,False) #Change to True to Use Stop List
    targetIDs = targetNumbers(targets, names)
    modelName = "Cosine Similarity Model"
    scoreAllResults(queries, results, targetIDs, 
            f"{modelName} on {sys.argv[1]}")
    ######### Tanimoto Similarity##########
    results = retrieveCosSim(queries,contents,True,option = "Tanimoto") #Change to True to Use Stop List
    targetIDs = targetNumbers(targets, names)
    modelName = "Tanimoto Similarity Model"
    scoreAllResults(queries, results, targetIDs, 
            f"{modelName} on {sys.argv[1]}")    