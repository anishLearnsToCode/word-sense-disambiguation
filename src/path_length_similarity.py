# Method 3 (Path Length Similarity)
# The Path length similarity computes the similarity between 2 synsets based on the hop length between the nodes
# in the Hypernym Path in the wordnet corpus

# importing required packages
import numpy as np
from nltk.corpus import wordnet
# nltk.download('wordnet')


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
    synset_1_optimal = word_1[0]
    synset_2_optimal = word_2[0]

    for synset_1 in word_1:
        for synset_2 in word_2:
            similarity = max_similarity_path(synset_1, synset_2)
            if max_similarity < similarity:
                max_similarity = similarity
                synset_1_optimal = synset_1
                synset_2_optimal = synset_2

    return synset_1_optimal, synset_2_optimal, max_similarity


word_1 = input('Enter first word:\t')
word_2 = input('Enter second word:\t')
word_1_synset, word_2_synset, similarity = closest_synsets(word_1, word_2)

print(word_1.capitalize() + ' Definition:', word_1_synset.definition())
print(word_2.capitalize() + ' Definition:', word_2_synset.definition())
print('similarity:', similarity)
