import nltk
from nltk import pos_tag as pos_tag_
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('stopwords')


def tokenize(text):
    # This function takes a text and returns a list of tokens.
    return word_tokenize(text)


def pos_tag(tokens):
    # This functions takes a list of tokens and pos_tags each of them
    return pos_tag_(tokens)


def rm_stop_words(text):
    # this function removes the stop words from a text and return a list of tokens
    tokens = word_tokenize(text)
    tokens_without_sw = [word for word in tokens if not word in stopwords.words()]
    return tokens_without_sw


def bag_of_words(texts):
    words = []
    for i in range(len(texts)):
        for word in texts[i].split():
            if word.lower() not in words:
                words.append(word.lower())

    bow = [dict().fromkeys(words, 0) for x in range(len(texts))]
    for i, sentence in enumerate(texts):
        sentence_words = word_tokenize(sentence.lower())
        # frequency word count
        bag = bow[i]
        for sw in sentence_words:
            for word in words:
                if word == sw:
                    bag[word] += 1
    return bow
