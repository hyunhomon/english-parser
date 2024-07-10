import nltk

class DependencyParser:
    def __init__(self):
        nltk.download('maxent_ne_chunker', quiet=True)
        nltk.download('words', quiet=True)

    def parse(self, tagged_tokens):
        return nltk.ne_chunk(tagged_tokens)
