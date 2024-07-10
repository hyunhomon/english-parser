import nltk
from nltk.tokenize import word_tokenize

class Tokenizer:
    def __init__(self):
        nltk.download('punkt', quiet=True)

    def tokenize(self, text):
        return word_tokenize(text)
