import nltk
from nltk.tag import pos_tag

class POSTagger:
    def __init__(self):
        nltk.download('averaged_perceptron_tagger', quiet=True)

    def tag(self, tokens):
        return pos_tag(tokens)
