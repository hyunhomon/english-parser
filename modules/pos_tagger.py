from nltk.tag import pos_tag

class POSTagger:
    def __init__(self):
        self.pos_tag_mapping = {
            'CC': '접속사',  # Coordinating conjunction
            'CD': '기수',    # Cardinal number
            'DT': '관형사',  # Determiner
            'EX': '존칭 대명사',  # Existential there
            'FW': '외래어',  # Foreign word
            'IN': '전치사',  # Preposition or subordinating conjunction
            'JJ': '형용사',  # Adjective
            'JJR': '형용사(비교급)',  # Adjective, comparative
            'JJS': '형용사(최상급)',  # Adjective, superlative
            'LS': '리스트 마커',  # List item marker
            'MD': '법조동사',  # Modal
            'NN': '명사',  # Noun, singular or mass
            'NNS': '명사(복수형)',  # Noun, plural
            'NNP': '고유명사(단수형)',  # Proper noun, singular
            'NNPS': '고유명사(복수형)',  # Proper noun, plural
            'PDT': '관사 대명사',  # Predeterminer
            'POS': '소유격 마커',  # Possessive ending
            'PRP': '인칭 대명사',  # Personal pronoun
            'PRP$': '소유형 대명사',  # Possessive pronoun
            'RB': '부사',  # Adverb
            'RBR': '부사(비교급)',  # Adverb, comparative
            'RBS': '부사(최상급)',  # Adverb, superlative
            'RP': '미리 주어진 형태',  # Particle
            'SYM': '기호',  # Symbol
            'TO': 'to',  # to
            'UH': '감탄사',  # Interjection
            'VB': '동사',  # Verb, base form
            'VBD': '동사(과거형)',  # Verb, past tense
            'VBG': '동사(현재분사)',  # Verb, gerund or present participle
            'VBN': '동사(과거분사)',  # Verb, past participle
            'VBP': '동사(현재형)',  # Verb, non-3rd person singular present
            'VBZ': '동사(현재 3인칭 단수)',  # Verb, 3rd person singular present
            'WDT': '관계 대명사',  # Wh-determiner
            'WP': '관계 대명사',  # Wh-pronoun
            'WP$': '소유형 관계 대명사',  # Possessive wh-pronoun
            'WRB': '관계 부사'  # Wh-adverb
        }
        self.excluded_chars = set('.,!?~-()')

    def tag(self, tokens):
        pos_tags = []
        for _, tag in pos_tag(tokens):
            if tag[0] not in self.excluded_chars:
                pos_tags.append(self.pos_tag_mapping.get(tag, 'Unknown'))
        pos_tags_korean = ', '.join(pos_tags)
        return pos_tags_korean
