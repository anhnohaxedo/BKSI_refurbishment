import underthesea
import math
import pandas as pd
import nltk
import numpy as np
from sklearn.decomposition import TruncatedSVD

documents = {}

# get document & pre-processing
for i in range(227):
    article = open("D:/project/BKSI/BKSI_refurbishment/scrapping/ussh/new_" + str(i) + ".txt", "r", encoding='utf-8')
    data = article.read()
    data = data.lower()
    documents[str(i)] = underthesea.word_tokenize(data)
    article.close()

corpus = []
dictionary = {}

# calculate corpus vocabulary
for article in documents.values():
    flags = []
    for token in article:
        if token not in dictionary.keys():
            corpus.append(1)
            dictionary[token] = len(corpus) - 1
        else:
            if token not in flags:
                corpus[dictionary[token]] += 1
                flags.append(token)

# calculate tf
def tf_idf(article):
    # iterate through the doc to create a dic of tokens and their tf
    freq = np.zeros(len(corpus))
    #tf
    for token in article:
        if token in dictionary.keys():
            freq[dictionary[token]] += 1
    #idf
    for token in dictionary.keys():
        freq[dictionary[token]] /= corpus[dictionary[token]]
    return freq

documents_vector = []
for article in documents.values():
    documents_vector.append(tf_idf(article=article))
# svd = TruncatedSVD(n_components=256)
# svd.fit(documents_vector)
# documents_vector = svd.transform(documents_vector)

