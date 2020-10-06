# Resnik Similarity (Method 4)
# In the Resnik similarity method we compute the negative log of the probability of the lowest common subsumer of the
#   2 given
# words. In this assignment we introduce Resnik and compute the closest synsets of 2 given words.
# NOTE: We can only compute the Resnik similarity of 2 words when they have the same Part of Speech (PoS) tag
# NOTE 2: We need a corpus to refer to the probabilities in computing the Resnik Similarity and in this case we will be
#       using the Brown IC Corpus

# Importing packages
import nltk
from nltk.corpus import wordnet, wordnet_ic
# nltk.download('wordnet')
# nltk.download('wordnet_ic')
from nltk.stem import WordNetLemmatizer
import numpy as np
import pickle
import pprint
import pandas as pd
from scipy import stats

# Defining Infinity
infinity = float('inf')

# Importing the Brown Corpus
brown_ic = wordnet_ic.ic('ic-brown.dat')


# Defining the Closest Synsets Function Based on Resnik Similarity Score
def closest_synsets(word_1: str, word_2: str):
    word_1 = wordnet.synsets(word_1)
    word_2 = wordnet.synsets(word_2)
    max_similarity = -infinity
    try:
        synset_1_shortest = word_1[0]
        synset_2_shortest = word_2[0]
    except:
        return None, None, -infinity

    for synset_1 in word_1:
        for synset_2 in word_2:
            if synset_1.pos() != synset_2.pos():
                continue
            similarity = synset_1.res_similarity(synset_2, ic=brown_ic)
            if similarity > max_similarity:
                max_similarity = similarity
                synset_1_shortest = synset_1
                synset_2_shortest = synset_2

    return synset_1_shortest, synset_2_shortest, max_similarity

# loading in the 6 documents from the resume
documents = pickle.load(open('../assets/documents.p', 'rb'))
print('The documents are:')
pprint.pprint(documents)

# Viewing the document as a Table
documents_table = pd.DataFrame(documents)
print('\nDocuments:')
print(documents_table)

# We will now find the similarity between the 6th document and every other document
similarity_mat = np.zeros((len(documents) - 1, len(documents[0])))

for column, keyword in enumerate(documents[len(documents) - 1]):
    for row in range(len(documents) - 1):
        similarity_mat[row][column] = closest_synsets(keyword, documents[row][column])[2]

print('\nThe similarity coefficients are:\n')
similarity = pd.DataFrame(similarity_mat, columns=documents[5])
print(similarity.to_string())

# saving the similarity coefficient matrix in text file
results = open('../assets/resnik_similarity_matrix.txt', 'w')
results.write(similarity.to_string())
results.close()

# We now select the highest and lowest similarity document for each word in the 6th document
max = [0, 0, 0, 0, 4, 1]
min = [3, 3, 2, 3, 4, 0]

# document with least/maximum similarity
document_min_similarity = stats.mode(min).mode[0]
document_max_similarity = stats.mode(max).mode[0]

print('\nDocument with Minimum Similarity to 6th document:', documents[document_min_similarity])
print('Document with Maximum Similarity to 6th document:', documents[document_max_similarity])
