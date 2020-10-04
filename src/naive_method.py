# Method 1
# Implementing a Naive method that simply retuns the first sense found in the wordnet synsets as the disambiguated
# sense

import pprint
import nltk
from nltk.corpus import wordnet
# nltk.download('wordnet')

word = input('Enter word for disambiguation:\t')
synsets = wordnet.synsets(word)
sense = synsets[0]

print('Definition:', sense.definition())
print('Examples:')
pprint.pprint(sense.examples())
