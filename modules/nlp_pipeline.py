import modules

class NLPPipeline:
    def __init__(self):
        self.tokenizer = modules.Tokenizer()
        self.pos_tagger = modules.POSTagger()
        self.analyzer = modules.FormatAnalyzer()
        self.optimizer = modules.SentenceOptimizer()
        self.translator = modules.SentenceTranslator()
        self.recognizer = modules.ImageRecognizer()

    def pos_tagging(self, text):
        tokens = self.tokenizer.tokenize(text)
        pos_tags = self.pos_tagger.tag(tokens)

        pos_tags_korean = [(word, self.pos_tagger.pos_tag_mapping.get(tag, tag)) for word, tag in pos_tags]
        translated_tags = ' / '.join([f'{word}({tag})' for word, tag in pos_tags_korean])

        return translated_tags
    
    def format_analysis(self, text):
        tokens = self.tokenizer.tokenize(text)
        pos_tags = self.pos_tagger.tag(tokens)
        format = self.analyzer.analyze(pos_tags)

        return format
    
    def sentence_optimize(self, text):
        tokens = self.tokenizer.tokenize(text)
        optimized = self.optimizer.optimize(tokens)

        return optimized
    
    def sentence_translate(self, text):
        translated = self.translator.translate(text)
        
        return translated
    
    def image_recognition(self, path):
        recognized = self.recognizer.recognize(path)

        return recognized
