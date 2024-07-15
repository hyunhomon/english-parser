from nltk.chunk import RegexpParser

class FormatAnalyzer():
    def __init__(self):
        grammar = r"""
            NP: {<DT|PRP.*>?<RB.*>*<JJ.*>*<NN.*>*}  # 명사구: 관사 or 대명사 뒤에 부사 0개 이상 형용사 0개 이상, 명사 0개 이상
            VP: {<MD>?<VB.*>+<PP>*}                # 동사구: 조동사 뒤에 동사 1개 이상, 전치사구 0개 이상
            PP: {<IN><NP|PRP.*>+}               # 전치사구: 전치사 뒤에 명사구 or 동사구 or 대명사 1개 이상
            # todo: TO, VBG만 예외처리
        """
        self.parser = RegexpParser(grammar)

    def analyze(self, tagged_tokens):
        parsed_sentence = self.parser.parse(tagged_tokens)
        result = '\n'.join([''.join(str(item)) for item in list(parsed_sentence)])
        
        return result
