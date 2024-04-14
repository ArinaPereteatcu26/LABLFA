class Grammar():
    def __init__(self):
        self.P = {
            'S': ['aB', 'bA', 'A'],
            'A': ['B', 'Sa', 'bBA', 'b'],
            'B': ['b', 'bS', 'aD', 'eps'],
            'D': ['AA'],
            'C': ['Ba']
        }
        self.V_N = ['S', 'A', 'B', 'C', 'D']
        self.V_T = ['a', 'b']

    def Remove_Epsilon(self):
        # 1. remove epsilon productions
        # find non-terminal symbols that derive into empty string
        nt_epsilon = []
        for key, value in self.P.items():
            s = key
            productions = value
            for p in productions:
                if p == 'eps':
                    nt_epsilon.append(s)

        for key, value in self.P.items():
            for ep in nt_epsilon:
                for v in value:
                    prod_copy = v
                    if ep in prod_copy:
                        for c in prod_copy:
                            # delete epsilon prod and add new prod
                            if c == ep:
                                value.append(prod_copy.replace(c, ''))
        # initialize a copy with added prod
        P1 = self.P.copy()
        # remove eps prod from copy
        for key, value in self.P.items():
            if key in nt_epsilon and len(value) < 2:
                del P1[key]
            else:
                for v in value:
                    if v == 'eps':
                        P1[key].remove(v)

        print(f"1. After removing epsilon productions:\n{P1}")
        self.P = P1.copy()
        return P1

