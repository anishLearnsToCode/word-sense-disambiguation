# Word Sense Disambiguation

**Anish Sachdeva (DTU/2K16/MC/13)**
**Natural Language Processing (Dr. Seba Susan)**

[📘 Path Length Similarity](notebooks/path-similarity-metric.ipynb) |
[📘 Resnik Similarity](notebooks/resnik-similarity.ipynb) |
[📗 Naïve Disambiguation](notebooks/naive-disambiguation.ipynb) |
[📗 Simple LESK Algorithm](notebooks/simple-lesk-algorithm.ipynb) |
[✒ Report](assets/nlp-wsd.pdf)

![booster](assets/booster.png)

---

## Overview

* [Introduction](#introduction)
* [Naïve Disambiguation](#naïve-disambiguation)
* [Simple LESK Algorithm Disambiguation](#simple-lesk-algorithm-disambiguation)
* [Path Length Similarity Disambiguation](#path-length-similarity-disambiguation)
* [Resnik Similarity Disambiguation](#resnik-similarity-disambiguation)
* [Bibliography](#bibliography)

---

## Introduction

We explore 4 different metrics to compare similarity and disambiguate words. For details, see the notebooks below:

### Notebooks

1. [Naive Disambiguation](notebooks/naive-disambiguation.ipynb)
2. [Simple LESK Algorithm Disambiguation](notebooks/simple-lesk-algorithm.ipynb)
3. [Path Length Similarity Metric](notebooks/path-similarity-metric.ipynb)
4. [Resnik Similarity Metric](notebooks/resnik-similarity.ipynb)

---

## Naïve Disambiguation

To see the disambiguation of any word using the naive method, clone the repository and install dependencies:

```bash
git clone https://github.com/anishLearnsToCode/word-sense-disambiguation.git
pip install -r requirements.txt
```

Run the naive method directly from the root directory:

```bash
python -m src.naive_method
>> Enter word for disambiguation:    bank
>> Definition: a large natural stream of water (larger than a creek)
>> Examples:
>> ['they pulled the canoe up on the bank',
>> 'he sat on the bank of the river and watched the currents']
```

See a running example with explanation in [this notebook](notebooks/naive-disambiguation.ipynb).

---

## Simple LESK Algorithm Disambiguation

The Simple LESK Algorithm uses tokens in the gloss surrounding the main word to disambiguate its meaning. Inverse Document Frequency (IDF) values are assigned as weights to all possible senses of the word.

Run directly from the root directory:

```bash
python -m src.simple_lesk_algorithm
>> Enter the Gloss (document):    i like a hot cup of java in the morning 
>> Enter word for disambiguation:    java
>> The disambiguated meaning is: a beverage consisting of an infusion of ground coffee beans
>> The weight vector is: [0, 0.28768207245178085, 0]
```

---

## Path Length Similarity Disambiguation

The Path Length Similarity computes the minimum hop path between any two words in WordNet using Hypernym Paths. The similarity score is computed as:

```
similarity = -log(path_length(w1, w2))
```

Run similarity between two words:

```bash
python -m src.path_length_similarity
>> Enter first word:    dog
>> Enter second word:    wolf
>> Dog Definition: a member of the genus Canis (probably descended from the common wolf) that has been domesticated by man since prehistoric times; occurs in many breeds
>> Wolf Definition: any of various predatory carnivorous canine mammals of North America and Eurasia that usually hunt in packs
>> similarity: -0.6931471805599453
```

Compute similarity between the 6th document and other documents:

```bash
python -m src.path_similarity_resume
```

See [results here](assets/path_similarity_matrix.txt) and explanation in [the notebook](notebooks/path-similarity-metric.ipynb).

---

## Resnik Similarity Disambiguation

The Resnik similarity computes the negative log probability of the lowest common subsumer of two words using the Brown IC Corpus.

Run similarity between two words:

```bash
python -m src.resnik_similarity
>> Enter the first word:    java
>> Enter the second word:    language
>> Java Definition: a platform-independent object-oriented programming language
>> Language Definition: a systematic means of communicating by the use of sounds or conventional symbols
>> similarity: 5.792086967391197
```

Run similarity between the 6th document and other documents:

```bash
python -m src.resnik_similarity_resume
```

See the [Resnik similarity matrix here](assets/resnik_similarity_matrix.txt) and explanation in [the notebook](notebooks/resnik-similarity.ipynb).

---

## Bibliography

1. [Speech & Language Processing \~ Jurafsky](https://web.stanford.edu/~jurafsky/slp3/)
2. [NLTK](https://www.nltk.org/)
3. [pickle](https://docs.python.org/3/library/pickle.html)
4. [pandas](https://pandas.pydata.org/)
5. [pandas.DataFrame](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html)
6. [Indexing and Slicing on Pandas DataFrames](https://datacarpentry.org/python-ecology-lesson/03-index-slice-subset/index.html)
7. [NumPy](https://numpy.org/)
8. [WordNet interface (NLTK)](https://www.nltk.org/howto/wordnet.html)
