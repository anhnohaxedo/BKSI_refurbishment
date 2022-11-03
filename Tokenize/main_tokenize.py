import underthesea
import math
import numpy as np
import pandas as pd

import re
import nltk
import sklearn
from Tools.scripts.dutree import display
from sklearn.datasets import load_iris
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
dataset = [
    "Tôi yêu Google. Tôi ghét Bing. Google là số một",
    "Tôi yêu Pushkin. Pushkin là số một"
]
# dataset = [
#     "this is a sample",
#     "this is another example"
# ]
# dataset = [
#     "Tôi yêu Google",
#     "Tôi ghét Bing",
#     "Google là số một",
#     "Tôi yêu Puskin",
#     "Puskin là số một",
# ]


# dic = {1: "a new car used car car review", 2: "a friend in need is a friend indeed"}

dic = {1: "Tôi yêu Google", 2: "Tôi ghét Bing", 3: "Google là số một", 4: "Tôi yêu Puskin", 5: "Puskin là số một"}
dic1 = {1: "Tôi yêu, Google. Tôi ghét Bing. Google là số một", 2: "Tôi yêu Pushkin. Pushkin là số một"}
# dic2 = {1: "this is a sample", 2: "this is another example"}
# dic = {}

# for i in range(45, 77):
#     try:
#         article = open("D:/BKSI_refurbishment/scrapping/articles/article_" + str(i) + ".txt", "r", encoding='utf-8')
#         data = article.read()
#         dic[str(i)] = data
#     except IOError:
#         print("file is yeeted")
#     finally:
#         article.close()

# for i in range(0, 228):
#     try:
#         article = open("D:/BKSI_refurbishment/scrapping/ussh/new_" + str(i) + ".txt", "r", encoding='utf-8')
#         data = article.read()
#         dic[str(i)] = data
#     except IOError:
#         print("file is yeeted")
#     finally:
#         article.close()

# calculate tf
corpus = {}
docFreq = {}
for dic_key in dic.keys():
    data = dic[dic_key].lower()
    data = re.sub(r'(\. )|(\, )', ' ', data)
    data = underthesea.word_tokenize(data)
    # Not handle blacklist
    freq = {}
    # iterate through the doc to create a dic of tokens and their tf
    for token in data:
        if token in freq.keys():
            freq[token] += 1
        else:
            freq[token] = 1
    for key in freq.keys():
        freq[key] /= len(data)
    docFreq[dic_key] = freq

# calculate tf-idf
for record in docFreq.values():
    for token in record:
        count = 0
        for dictionary in docFreq.values():
            if token in dictionary:
                count += 1
        idf = math.log10((len(docFreq))/count)
        record[token] *= idf


def cosine_sim(a, b):
    cos_sim = np.dot(a, b)/(np.linalg.norm(a)*np.linalg.norm(b))
    np.zeros()
    return cos_sim


# print the record
for key in docFreq.keys():
    print(key)
    print(docFreq[key])
    print('\n')
# convert to lower case
# data = dic['45'].lower()
# data = underthesea.word_tokenize(data)
# print(data)

data_query = "car is indeed"

# try:
#     query = open("D:/BKSI_refurbishment/scrapping/articles/query.txt", "r", encoding='utf-8')
#     data_query = query.read()
# except IOError:
#     print("query is yeeted")
# finally:
#     query.close()

data_query = data_query.lower()
data_query_list = underthesea.word_tokenize(data_query)

print(data_query_list)

query_weights = {}

for token in data_query_list:
    # print("this is a token:" + token)
    for key in docFreq.keys():
        # print("this is a key:" + str(key))
        if key not in query_weights:
            query_weights[key] = 0
        if token in docFreq[key]:
            # print(token + " " + str(docFreq[key][token]))
            query_weights[key] += docFreq[key][token] + 1

sorted_weights = {k: v for k, v in sorted(query_weights.items(), key=lambda item: item[1], reverse=True)}

# print(sorted_weights)

print("scikit learn result:")
tfIdfTransformer = TfidfTransformer(use_idf=True)
countVectorizer = CountVectorizer()
wordCount = countVectorizer.fit_transform(dataset)
newTfIdf = tfIdfTransformer.fit_transform(wordCount)
df = pd.DataFrame(newTfIdf[0].T.todense(), index=countVectorizer.get_feature_names(), columns=["TF-IDF"])
df = df.sort_values('TF-IDF', ascending=False)
print(df)
df = pd.DataFrame(newTfIdf[1].T.todense(), index=countVectorizer.get_feature_names(), columns=["TF-IDF"])
df = df.sort_values('TF-IDF', ascending=False)
print("---")
print(df)
df = pd.DataFrame(newTfIdf[2].T.todense(), index=countVectorizer.get_feature_names(), columns=["TF-IDF"])
df = df.sort_values('TF-IDF', ascending=False)
print("---")
print(df)
df = pd.DataFrame(newTfIdf[3].T.todense(), index=countVectorizer.get_feature_names(), columns=["TF-IDF"])
df = df.sort_values('TF-IDF', ascending=False)
print("---")
print(df)
df = pd.DataFrame(newTfIdf[4].T.todense(), index=countVectorizer.get_feature_names(), columns=["TF-IDF"])
df = df.sort_values('TF-IDF', ascending=False)
print("---")
print(df)

