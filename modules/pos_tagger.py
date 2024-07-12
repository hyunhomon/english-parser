from nltk.tag import pos_tag

class POSTagger:
    def __init__(self):
        self.pos_tag_mapping = {
            'CC': '접속사',  # Coordinating conjunction (and, but, or)
            'CD': '기수',  # Cardinal number (one, two, 1, 2)
            'DT': '관형사',  # Determiner (the, a, an)
            'EX': '존칭 대명사',  # Existential there (there)
            'FW': '외래어',  # Foreign word (d'accord, esprit)
            'IN': '전치사',  # Preposition or subordinating conjunction (in, of, like)
            'JJ': '형용사',  # Adjective (big, old, green)
            'JJR': '비교급 형용사',  # Adjective comparative (bigger, older)
            'JJS': '최상급 형용사',  # Adjective superlative (biggest, oldest)
            'LS': '리스트 마커',  # List item marker (1., A., *)
            'MD': '법조동사',  # Modal (can, could, will)
            'NN': '명사',  # Noun singular or mass (dog, cat, truth)
            'NNS': '복수형 명사',  # Noun plural (dogs, cats)
            'NNP': '단수형 고유명사',  # Proper noun singular (John, London)
            'NNPS': '복수형 고유명사',  # Proper noun plural (Americans, Germans)
            'PDT': '관사 대명사',  # Predeterminer (all, both, half)
            'POS': '소유격 마커',  # Possessive ending ('s)
            'PRP': '인칭 대명사',  # Personal pronoun (I, you, he)
            'PRP$': '소유형 대명사',  # Possessive pronoun (my, your, his)
            'RB': '부사',  # Adverb (quickly, silently)
            'RBR': '비교급 부사',  # Adverb comparative (faster, harder)
            'RBS': '최상급 부사',  # Adverb superlative (fastest, hardest)
            'RP': '미리 주어진 형태',  # Particle (up, off)
            'SYM': '기호',  # Symbol ($, %, &)
            'TO': 'to',  # to (to)
            'UH': '감탄사',  # Interjection (oh, wow, hey)
            'VB': '동사',  # Verb base form (run, eat, sleep)
            'VBD': '과거형 동사',  # Verb past tense (ran, ate, slept)
            'VBG': '현재분사',  # Verb gerund or present participle (running, eating)
            'VBN': '과거분사',  # Verb past participle (run, eaten)
            'VBP': '현재형 동사',  # Verb non-3rd person singular present (run, eat)
            'VBZ': '현재 3인칭 단수 동사',  # Verb 3rd person singular present (runs, eats)
            'WDT': '관계 대명사',  # Wh-determiner (which, that)
            'WP': '관계 대명사',  # Wh-pronoun (who, what)
            'WP$': '소유형 관계 대명사',  # Possessive wh-pronoun (whose)
            'WRB': '관계 부사',  # Wh-adverb (where, when)
        }

    def tag(self, tokens):
        pos_tags = pos_tag(tokens)
        return pos_tags
