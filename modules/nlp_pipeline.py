from modules.tokenizer import Tokenizer
from modules.pos_tagger import POSTagger
from modules.dependency_parser import DependencyParser

class NLPPipeline:
    def __init__(self):
        self.tokenizer = Tokenizer()
        self.pos_tagger = POSTagger()
        self.parser = DependencyParser()

    def process(self, text):
        tokens = self.tokenizer.tokenize(text)
        pos_tags = self.pos_tagger.tag(tokens)
        parse_tree = self.parser.parse(pos_tags)

        return tokens, pos_tags, parse_tree
