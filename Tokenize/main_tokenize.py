import underthesea
import math
import pandas as pd
import nltk

# dic = {1: "a new car used car car review", 2: "a friend in need is a friend indeed"}
dic = {}

for i in range(45, 77):
    try:
        article = open("D:/BKSI_refurbishment/scrapping/articles/article_" + str(i) + ".txt", "r", encoding='utf-8')
        data = article.read()
        dic[str(i)] = data
    except IOError:
        print("file is yeeted")
    finally:
        article.close()


# calculate tf
corpus = {}
docFreq = []
for article in dic.values():
    data = article.lower()
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
    docFreq.append(freq)

# calculate tf-idf
for record in docFreq:
    for token in record:
        count = 0
        for dictionary in docFreq:
            if token in dictionary:
                count += 1
        idf = math.log10(len(docFreq)/count)
        record[token] *= idf

# print the record
for record in docFreq:
    print(record)
    print('\n')
# convert to lower case
# data = dic['45'].lower()
# data = underthesea.word_tokenize(data)
# print(data)