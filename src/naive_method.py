# Method 1
# Implementing a Naive method that simply retuns the first sense found in the wordnet synsets as the disambiguated
# sense

import pprint
import pickle
import random
import nltk
from nltk.corpus import wordnet
# nltk.download('wordnet')


def naive_disambiguation(word: str):
    synsets = wordnet.synsets(word)
    try:
        return synsets[0]
    except:
        return 'no sense found'


word = input('Enter word for disambiguation:\t')
sense = naive_disambiguation(word)
if isinstance(sense, str):
    print('No sense found')
else:
    print('Definition:', sense.definition())
    print('Examples:')
    pprint.pprint(sense.examples())
    print('\n\n')

# We now load in the keywords we extracted from resume that have been divided into 6 documents and we will randomly
# disambiguate one keyword from each document

print('\n\nWe now disambiguate a few keywords from the resume')
documents = pickle.load(open('../assets/documents.p', 'rb'))
for document in documents:
    document = list(document)
    word = document[random.randint(0, len(document) - 1)]
    sense = naive_disambiguation(word)
    if isinstance(sense, str):
        print('No sense found')
    else:
        print(word.capitalize() + ':', sense.definition().capitalize())
