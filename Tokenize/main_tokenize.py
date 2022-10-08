import underthesea
import pandas as pd
import nltk

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
    for token in data:
        if token in freq.keys():
            freq[token] += 1
        else:
            freq[token] = 1
    for key in freq.keys():
        freq[key] /= len(data)
    docFreq.append(freq)

print(len(docFreq))
# convert to lower case
# data = dic['45'].lower()
# data = underthesea.word_tokenize(data)
# print(data)