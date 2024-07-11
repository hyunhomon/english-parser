from nltk.tag import pos_tag

class POSTagger:
    def tag(self, tokens):
        return pos_tag(tokens)
