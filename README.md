# Word Sense Disambiguation

__Anish Sachdeva (DTU/2K16/MC/13)__

__Natural Language Processing (Dr. Seba Susan)__

[📘 Path Length Similarity](notebooks/path-similarity-metric.ipynb) |
[📘 Resnik Similarity](notebooks/resnik-similarity.ipynb) |
[📗 Naïve Disambiguation](notebooks/naive-disambiguation.ipynb) |
[📗 Simple LESK Algorithm](notebooks/simple-lesk-algorithm.ipynb) |
[✒ Report](assets)

![booster](assets/booster.png)

## Overview
- [Introduction](#introduction)
- [Naïve Disambiguation](#nave-disambiguation)
- [Simple LESK Algorithm Disambiguation](#simple-lesk-similarity-disambiguation)
- [Path Length Similarity Disambiguation](#path-length-similarity-disambiguation)
- [Resnik Similarity Disambiguation](#resnik-similarity-disambiguation)
- [Bibliography](#bibliography)

## Introduction
We explore 4 different metrics to compare similarity and disambiguate words. For the 4 different 
methods refer to the Notebooks Below:

### Notebooks
1. [Naive Disambiguation](notebooks/naive-disambiguation.ipynb)
1. [Simple LESK Algorithm Disambiguation](notebooks/simple-lesk-algorithm.ipynb) 
1. [Path Length Similarity Metric](notebooks/path-similarity-metric.ipynb)
1. [Resnik Similarity Metric](notebooks/resnik-similarity.ipynb)

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

```bash
git clone https://github.com/anishLearnsToCode/word-sense-disambiguation.git
pip install -r requirements.txt
```

Navigate to `simple_lesk_algorithm.py` file and test with sample gloss and word token

```bash
cd src
python simple_lesk_algorithm.py
>> Enter the Gloss (document):	i like a hot cup of java in the morning 
>> Enter word for disambiguation:	java
>> The disambiguated meaning is: a beverage consisting of an infusion of ground coffee beans
>> The weight vector is: [0, 0.28768207245178085, 0]
```

## Path length Similarity Disambiguation
The Path Length Similarity computes the minimum hop path between any 2 words in the wordnet 
corpus using the Hypernym Paths available and then computes the similarity score as __-log (pathlen(w1, w2))__.

To compute the Path Score and closest synsets between any 2 english words run the `path_length_similarity.py`
file as 

```bash
git clone https://github.com/anishLearnsToCode/word-sense-disambiguation.git
cd word-sense-disambiguation
pip install -r requirements.txt
cd src
python path_length_similarity.py
>> Enter first word:	dog
>> Enter second word:	wolf
>> Dog Definition: a member of the genus Canis (probably descended from the common wolf) that has been domesticated by man since prehistoric times; occurs in many breeds
>> Wolf Definition: any of various predatory carnivorous canine mammals of North America and Eurasia that usually hunt in packs
>> similarity: -0.6931471805599453
```

Then to compute the similarity between 6th document with other documents (keywords) in the resume run the
`path_similarity_resume.py` file as:

```bash
cd src
python path_similarity_resume.py
```

See [results here](assets/path_similarity_matrix.txt). See the explanation and results in 
[Jupyter Notebook](notebooks/path-similarity-metric.ipynb).

## Resnik Similarity Disambiguation
To compute the similarity between 2 words and find closest possible synsets 
run `resnik_similarity.py` as:

```bash
git clone https://github.com/anishLearnsToCode/word-sense-disambiguation.git
cd word-sense-disambiguation
pip install -r requirements.txt
cd src
python resnik_similarity.py
>> Enter the first word:	java
>> Enter the second word:	language
>> Java Definition: a platform-independent object-oriented programming language
>> Language Definition: a systematic means of communicating by the use of sounds or conventional symbols
>> similarity: 5.792086967391197
```

To run this metric on the Resume and see the similarity between 6th document and other documents
run the `resnik_similarity_resume.py` file.

See resnik similarity coefficient [matrix here](assets/resnik_similarity_matrix.txt) and
see explanation and results in [this Notebook](notebooks/resnik-similarity.ipynb). 

## Bibliography
1. [Speech & Language Processing ~Jurafsky](https://web.stanford.edu/~jurafsky/slp3/)
1. [nltk](https://www.nltk.org/)
1. [pickle](https://docs.python.org/3/library/pickle.html)
1. [pandas](https://pandas.pydata.org/)
1. [pandas.DataFrames](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html)
1. [Indexing and Slicing on Pandas DataFrames](https://datacarpentry.org/python-ecology-lesson/03-index-slice-subset/index.html)
1. [numpy](https://numpy.org/)
1. [wordnet interface](https://www.nltk.org/howto/wordnet.html)
