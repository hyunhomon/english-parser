from modules.tokenizer import Tokenizer
from modules.pos_tagger import POSTagger
from modules.format_analyzer import FormatAnalyzer

class NLPPipeline:
    def __init__(self):
        self.tokenizer = Tokenizer()
        self.pos_tagger = POSTagger()
        self.analyzer = FormatAnalyzer()

    def pos_tagging(self, text):
        tokens = self.tokenizer.tokenize(text)
        pos_tags = self.pos_tagger.tag(tokens)

        pos_tags_korean = [(word, self.pos_tagger.pos_tag_mapping.get(tag, tag)) for word, tag in pos_tags]
        translated_tags = ' / '.join([f'{word}({tag})' for word, tag in pos_tags_korean])

        return translated_tags
    
    def format_analysis(self, text):
        tokens = self.tokenizer.tokenize(text)
        pos_tags = self.pos_tagger.tag(tokens)
        format = self.analyzer.analysis(pos_tags)

        return format
