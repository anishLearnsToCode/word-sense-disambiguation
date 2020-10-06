import nltk
from nltk.corpus import stopwords
# nltk.download('stopwords')

stopwords_en = set(stopwords.words('english'))


def tokenize(document: str, word: str) -> set:
    # obtaining tokens from the gloss
    tokenizer = nltk.RegexpTokenizer(r'\w+')
    tokens = tokenizer.tokenize(document)

    # removing stop words from tokens
    tokens = [token for token in tokens if token not in stopwords_en and token.isalpha()]

    # removing the word from the tokens
    tokens = [token for token in tokens if token != word]
    return set(tokens)
