# This script wil load in the resume and divide it into 6 documents and save the docuemnts so that they can be loaded
# into other files and we can test the keywords against our word sense disambiguation

import pickle
import pprint
from collections import Counter

import nltk
from nltk.corpus import stopwords

# loading the document
resume = open('../assets/resume.txt', 'r')
document = resume.read().lower()
resume.close()

# tokenizing the document
tokenizer = nltk.RegexpTokenizer(r'\w+')
tokens = tokenizer.tokenize(document)

# removing stop words from tokens
stopwords_en = set(stopwords.words('english'))
tokens = [token for token in tokens if token not in stopwords_en and token.isalpha()]

# divide the document into n parts
documents = []
n = 6
k = len(tokens) // n
for i in range(n):
    documents.append(tokens[k * i: len(tokens) if i == n - 1 else (i + 1) * k])

# extracting top m words from each document
m = 6

most_common = []
for document in documents:
    frequencies = Counter(document)
    bag = []
    for word, frequency in frequencies.most_common(m):
        bag.append(word)
    most_common.append(bag)

# saving these tokens so they we can extract them later on and use them for training and testing purposes
pickle.dump(most_common, open('../assets/documents.p', 'wb'))

# print the most common tokens
pprint.pprint(most_common)

# adding the first 5 documents to create a training set
training_set_tokens = set()
for i in range(5):
    for token in most_common[i]:
        training_set_tokens.add(token)

# seeing the training data
print('\ntraining data')
pprint.pprint(training_set_tokens)

# saving the training data tokens
pickle.dump(training_set_tokens, open('../assets/training_set_tokens.p', 'wb'))

# saving the last document (6th document) as the testing set
pickle.dump(most_common[5], open('../assets/testing_set_tokens.p', 'wb'))

# seeing the testing data
print('\nTesting Data')
pprint.pprint(most_common[5])
