import random
class Grammar:
    def __init__(self):
        self.S = 'S'
        self.VN = ['S', 'A', 'B', 'C']
        self.VT = ['a', 'b', 'c', 'd']
        self.P = {
            'S': ['dA'],
            'A': ['d', 'aB'],
            'B': ['bC'],
            'C': ['cA', 'aS']
        }
        self.generated_strings = set()

