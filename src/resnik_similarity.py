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
import numpy as np

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


# Taking User Input
word_1 = input('Enter the first word:\t')
word_2 = input('Enter the second word:\t')
word_1_synset, word_2_synset, similarity = closest_synsets(word_1, word_2)

print(word_1.capitalize() + ' Definition:', word_1_synset.definition())
print(word_2.capitalize() + ' Definition:', word_2_synset.definition())
print('similarity:', similarity)
