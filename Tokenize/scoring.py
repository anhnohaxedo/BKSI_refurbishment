import re
import vectorize as main_tokenize
from underthesea import word_tokenize
import math
from sklearn.decomposition import TruncatedSVD
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np


query = "lễ khai giảng năm học"
documents = main_tokenize.documents_vector
#Second approach
def sim_func2(query):
    tfidf_vector = main_tokenize.tf_idf(query)
    tfidf_vector = np.reshape(tfidf_vector, (1,-1))
    # svd = TruncatedSVD(n_components=256)
    # svd.fit(tfidf_vector) 
    # query_vector = svd.transform(tfidf_vector)
    # sim_maxtrix = cosine_similarity(query_vector, documents)
    sim_maxtrix = cosine_similarity(tfidf_vector, documents)
    sim_maxtrix = np.reshape(sim_maxtrix, (-1,))
    sim_list = (-sim_maxtrix).argsort()[:5]
    return sim_list

print(sim_func2(query= word_tokenize(query)))

