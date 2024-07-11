from modules.tokenizer import Tokenizer
from modules.pos_tagger import POSTagger
from modules.dependency_parser import DependencyParser

class NLPPipeline:
    def __init__(self):
        self.tokenizer = Tokenizer()
        self.pos_tagger = POSTagger()
        self.parser = DependencyParser()

    def pos_tagging(self, text):
        tokens = self.tokenizer.tokenize(text)
        pos_tags = self.pos_tagger.tag(tokens)

        return pos_tags
    
    def construe(self, text):
        tokens = self.tokenizer.tokenize(text)
        pos_tags = self.pos_tagger.tag(tokens)
        parse_tree = self.parser.parse(pos_tags)

        return parse_tree
