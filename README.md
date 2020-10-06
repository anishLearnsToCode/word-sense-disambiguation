# Word Sense Disambiguation

__Anish Sachdeva (DTU/2K16/MC/13)__

__Natural Language Processing (Dr. Seba Susan)__

[📘 Path Length Similarity]() |
[📘 Resnik Similarity]() |
[📗 Naïve Disambiguation](notebooks/naive-disambiguation.ipynb) |
[📗 Simple LESK Algorithm](notebooks/simple-lesk-algorithm.ipynb) |
[✒ Report]()

## Overview
- [Introduction]()
- [Naïve Disambiguation]()
- [Simple LESK Algorithm Disambiguation]()
- [Path Length Similarity Disambiguation]()
- [Resnik Similarity Disambiguation]()
- [Bibliography]()

## Introduction
### Notebooks
1. [Naive Disambiguation](notebooks/naive-disambiguation.ipynb)

## Naïve Disambiguation
To see the disambiguation of any given word using the naive method, pull this repository on your 
machine and install all dependencies.

```powershell
git clone https://github.com/anishLearnsToCode/word-sense-disambiguation.git
pip install -r requirements.txt
```

navigate to the `naive_method.py` file and run it and enter a word of your choice:

```powershell
cd src
python naive_method.py
>> Enter word for disambiguation:    bank
>> Definition: a large natural stream of water (larger than a creek)
>> Examples:
>> ['they pulled the canoe up on the bank',
>> 'he sat on the bank of the river and watched the currents']
```

See a running example with explanation in 
[this notebook](notebooks/naive-disambiguation.ipynb)

## Simple LESK Similarity Disambiguation
In the Simple LESK Algorithm we use the words present in the gloss surrounding the main token to 
disambiguate it's meaning and we assign Inverse Document Frequency (IDF) values and assign weights
to all possible senses of the given token.

To run locally, clone the repository and install dependencies

```powershell
git clone https://github.com/anishLearnsToCode/word-sense-disambiguation.git
pip install -r requirements.txt
```

Navigate to `simple_lesk_algorithm.py` file and test with sample gloss and word token

```powershell
cd src
python simple_lesk_algorithm.py
>> Enter the Gloss (document):	i like a hot cup of java in the morning 
>> Enter word for disambiguation:	java
>> The disambiguated meaning is: a beverage consisting of an infusion of ground coffee beans
>> The weight vector is: [0, 0.28768207245178085, 0]
```

## Path length Similarity Disambiguation

## Resnik Similarity Disambiguation

## Bibliography
1. [Speech & Language Processing ~Jurafsky](https://web.stanford.edu/~jurafsky/slp3/)
1. [nltk](https://www.nltk.org/)
1. [pickle](https://docs.python.org/3/library/pickle.html)
1. [pandas](https://pandas.pydata.org/)
1. [pandas.DataFrames](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html)
1. [Indexing and Slicing on Pandas DataFrames](https://datacarpentry.org/python-ecology-lesson/03-index-slice-subset/index.html)
1. [numpy](https://numpy.org/)
1. [wordnet interface](https://www.nltk.org/howto/wordnet.html)
