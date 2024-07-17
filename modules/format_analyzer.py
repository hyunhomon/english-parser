from nltk.tree import Tree
from nltk.chunk import RegexpParser

class FormatAnalyzer:
    def __init__(self):
        grammar = r"""
            PP: {<TO><VB>}                                                # 전치사구: to 1개, 동사 원형 1개
            NP: {<DT|PRP\$|PDT|POS>+<VB.*>+<NN.*|FW|CD>?}                 # 명사구: 관사 or 대명사 or 전치한정사 or 소유격 마커 1개 이상, 동사 1개 이상, 명사 or 외래어 or 기수 0 or 1개 (명사구 내에 동사가 있는 경우를 위해 분리)
            VP: {<MD>?<VB[^G].*>+<VBG>?}                                  # 동사구: 조동사 0 or 1개, 동사(현재분사 제외) 1개 이상, 현재분사 0 or 1개
            NP: {<DT|PRP.*|EX|PDT>*<VBG>?<RB.*|JJ.*|NN.*|FW|CD|POS|NP>*}  # 명사구: 관사 or 대명사 or 전치한정사 0개 이상, 동명사 0 or 1개, 부사 or 형용사 or 명사 or 외래어 or 기수 or 소유격 마커 or 명사구 0개 이상
            PP: {<IN|TO>+<NP>?}                                           # 전치사구: 전치사 1개 이상, 명사구 0 or 1개
            RC: {<W.*><NP|VP>+}                                           # 관계대명사절: 관계대명사 or 관계부사 1개, 명사구 or 동사구 1개 이상
        """
        self.parser = RegexpParser(grammar)
        self.be_verb_list = ['am', '\'m', 'is', '\'s', 'are', '\'re', 'was', 'were', 'be', 'been']
        self.grammar_mapping = {
            'NP': '명사구',
            'VP': '동사구',
            'PP': '전치사구',
            'RC': '관계대명사절',
        }
    
    def process_tree(self, tree):
        processed_tree = []

        # 동명사 예외 처리를 위해 트리 순회 (be 동사 뒤는 무조건 현재 분사, 그 외는 모두 동명사로 처리)
        for subtree in tree:
            if type(subtree) == Tree:
                temp = None
                if subtree.label() == 'VP':
                    vp_leaves = subtree.leaves()
                    for idx in range(len(vp_leaves)):
                        if vp_leaves[idx][1].startswith('VB') and vp_leaves[idx][0] not in self.be_verb_list \
                            and idx < len(vp_leaves) - 1 and vp_leaves[idx + 1][1] == 'VBG':
                            if tree.index(subtree) < len(tree) - 1 and tree[tree.index(subtree) + 1].label() == 'NP':
                                tree[tree.index(subtree) + 1].insert(0, vp_leaves[idx + 1])
                            else:
                                temp = vp_leaves[idx + 1]
                            vp_leaves.pop(idx + 1)
                            break
                    subtree = Tree('VP', vp_leaves)
                tag = subtree.label()
                mapped_tag = self.grammar_mapping.get(tag, tag)
                words = ' '.join(word for word, _ in subtree.leaves())
                processed_tree.append(f'{mapped_tag}: {words}')
                if temp: processed_tree.append(f'명사구: {temp}')
        
        return processed_tree

    def analyze(self, tagged_tokens):
        tree = self.process_tree(self.parser.parse(tagged_tokens))
        result = '\n'.join([''.join(str(item)) for item in list(tree)])

        return result
