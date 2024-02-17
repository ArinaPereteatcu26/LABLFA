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

    def generateString(self):
        def generateFromSymbol(symbol):
            if symbol in self.VT:
                return symbol
            else:
                production = random.choice(self.P[symbol])
                return ''.join(generateFromSymbol(s) for s in production)

        generated_word = generateFromSymbol(self.S)
        while generated_word in self.generated_strings:  # Ensure uniqueness
            generated_word = generateFromSymbol(self.S)
        self.generated_strings.add(generated_word)  # Add to the set of generated strings
        return generated_word

    def generate5Words(self):
        for _ in range(5):
            w = self.generateString()
            print("Generated string:", w)

    def toFiniteAutomaton(self):
        return FiniteAutomaton()

class FiniteAutomaton:
    def __init__(self):
        self.states = {'S', 'A', 'B', 'C'}  # Set of states
        self.alphabet = {'a', 'b', 'c', 'd'}  # Set of input symbols
        self.transitions = {
            ('S', 'd'): 'A',
            ('A', 'd'): 'A',
            ('A', 'a'): 'B',
            ('B', 'b'): 'C',
            ('C', 'c'): 'A',
            ('C', 'a'): 'S'
        }  # Dictionary representing transition function
        self.initial_state = 'S'  # Initial state
        self.accepting_states = {'S', 'A'}  # Set of accepting states

    def accepts_string(self, input_string):
        current_state = self.initial_state
        for symbol in input_string:
             if (current_state, symbol) in self.transitions:
                current_state = self.transitions[(current_state, symbol)]
             else:
                 return False
        return current_state in self.accepting_states

    # Create an instance of the Grammar class
grammar = Grammar()

grammar.generate5Words()

