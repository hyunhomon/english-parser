import nltk

class DependencyParser:
    def parse(self, tagged_tokens):
        return nltk.ne_chunk(tagged_tokens)
