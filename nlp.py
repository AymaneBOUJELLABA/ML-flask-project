import nltk
from nltk.tokenize import word_tokenize
from nltk import pos_tag as pos_tag_

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')


def tokenize(text):
    # This function takes a text and returns a list of tokens.
    return word_tokenize(text)


def pos_tag(tokens):
    # This functions takes a list of tokens and pos_tags each of them
    return pos_tag_(tokens)
