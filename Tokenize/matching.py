import re
import main_tokenize
from underthesea import word_tokenize
import math

query = "thông tin về lễ khai giảng"
records = main_tokenize.docFreq

# First approach
def sim_func1(query):
    abstract = word_tokenize(query)
    print(abstract)
    match_list = []
    index = 0
    for record in records:
        score = 0
        for token in record.keys():
            for word in abstract:
                if word == token:
                    score += 1 * record[token]
                elif word in token:
                    score += len(word) / len(token) * record[token]
        match_list.append(
            {'index': index, 'score': score})
        index += 1
    match_list.sort(key= lambda d: d['score'], reverse=True)
    return match_list 

print(sim_func1(query=query))

