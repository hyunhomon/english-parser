from nltk.corpus import stopwords

class SentenceOptimizer():
    def __init__(self):
        self.stop_words = set(stopwords.words('english'))

    def optimize(self, tokens):
        optimized_words = [token for token in tokens if token.lower() not in self.stop_words]
        optimized_sentence = ' '.join(optimized_words)

        return optimized_sentence
