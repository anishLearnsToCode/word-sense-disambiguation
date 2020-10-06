# We will compare the 6th document from our resume with the first 5 and see which document it matches most closely to
# in the resume

# importing required packages
import nltk
import pickle
import pprint
from nltk.corpus import wordnet
# nltk.download('wordnet')
import pandas as pd
import numpy as np
from scipy import stats


infinity = float('inf')


# define the path length similarity metric
def path_similarity(hypernym_path1: list, hypernym_path2: list) -> float:
    """":returns the shortest path similarity metric between 2 hypernym paths"""
    count = 0
    for index, synset in enumerate(hypernym_path1):
        if len(hypernym_path2) <= index or synset != hypernym_path2[index]:
            break
        count += 1
    return -np.log(len(hypernym_path1) + len(hypernym_path2) - 2 * count)


# Define a method return maximum path similarity score given 2 synsets in wordnet
def max_similarity_path(synset_1, synset_2) -> float:
    """:returns the highest path similarity metric score between 2 synsets"""
    max_similarity = -float('inf')
    for hypernym_path_1 in synset_1.hypernym_paths():
        for hypernym_path_2 in synset_2.hypernym_paths():
            max_similarity = max(max_similarity, path_similarity(hypernym_path_1, hypernym_path_2))
    return max_similarity


# Defining a method which returns the closest synsets given 2 string words, the resulting synsets may be nouns,
# verbs etc.
def closest_synsets(word_1: str, word_2: str):
    """:returns the closest synsets for 2 given words based on path similarity metric"""
    word_1 = wordnet.synsets(word_1.lower())
    word_2 = wordnet.synsets(word_2.lower())
    max_similarity = -float('inf')
    try:
        synset_1_optimal = word_1[0]
        synset_2_optimal = word_2[0]
    except:
        return None, None, -infinity

    for synset_1 in word_1:
        for synset_2 in word_2:
            similarity = max_similarity_path(synset_1, synset_2)
            if max_similarity < similarity:
                max_similarity = similarity
                synset_1_optimal = synset_1
                synset_2_optimal = synset_2

    return synset_1_optimal, synset_2_optimal, max_similarity


# loading in the 6 documents from the resume
documents = pickle.load(open('../assets/documents.p', 'rb'))
print('The documents are:')
pprint.pprint(documents)

# We will now find the similarity between the 6th document and every other document
similarity_mat = np.zeros((len(documents) - 1, len(documents[0])))

for column, keyword in enumerate(documents[len(documents) - 1]):
    for row in range(len(documents) - 1):
        similarity_mat[row][column] = closest_synsets(keyword, documents[row][column])[2]

print('\nThe similarity coefficients are:\n')
similarity = pd.DataFrame(similarity_mat, columns=documents[5])
print(similarity.to_string())

# saving the similarity coefficient matrix in text file
results = open('../assets/path_similarity_matrix.txt', 'w')
results.write(similarity.to_string())
results.close()

# We now select the highest and lowest similarity document for each word in the 6th document
min = similarity_mat.argmin(axis=0)
max = similarity_mat.argmax(axis=0)

# document with least/maximum similarity
document_min_similarity = stats.mode(min).mode[0]
document_max_similarity = stats.mode(max).mode[0]

print('\nDocument with Minimum Similarity to 6th document:', documents[document_min_similarity])
print('Document with Maximum Similarity to 6th document:', documents[document_max_similarity])
