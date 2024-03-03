class FiniteAutomaton:
    def __init__(self):
        self.Q = ['q0','q1','q2','q3']
        self.Sigma = ['a','b','c']
        self.Delta = {
            ('q0', 'a'): ['q0', 'q1'],
            ('q1', 'b'): ['q2'],
            ('q2', 'c'): ['q3'],
            ('q3', 'c'): ['q3'],
            ('q2', 'a'): ['q2']
        }
        self.q0 = 'q0'
        self.F = ['q3']

