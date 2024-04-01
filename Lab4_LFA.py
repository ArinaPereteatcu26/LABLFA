import random

# Function to generate a string that matches the regex pattern: 'O(P|Q|R)^+ 2(3|4)'
def generate_string_regex_1():
    generated_string = ''.join('O' + random.choice(['P', 'Q', 'R']) * random.randint(1, 5) + ' 2' + random.choice(['3', '4']))
    return generated_string

# Function to generate a string that matches the regex pattern: 'A*B(C|D|E) E(G|H|i)^2'
def generate_string_regex_2():
    generated_string = ''.join('A' * random.randint(0, 5) + 'B' * random.randint(0, 5) + random.choice(['C', 'D', 'E']) + ' E' + random.choice(['G', 'H', 'i']) * 2)
    return generated_string

# Function to generate a string that matches the regex pattern: 'J^+K(L|M|N)*O? (P|Q)^3'
def generate_string_regex_3():
    generated_string = ''.join('J' * random.randint(1, 5) + 'K' + random.choice(['L', 'M', 'N']) * random.randint(0, 5) + 'O' * random.randint(0, 1) + ' ' + random.choice(['P', 'Q']) * 3)
    return generated_string

# Function to explain the regex pattern processing sequence
def show_processing_sequence(regex_pattern):
    sequence = []
    current_group = ''
    brackets = False

    for char in regex_pattern:
        if char == '[':
            brackets = True
            current_group = ''
        elif char == ']':
            brackets = False
            sequence.append(f"Match one element from '{current_group}' list")
            current_group = ''
        elif char == '*':
            sequence.append("Match zero or more occurrences of the preceding element")
        elif char == '+':
            sequence.append("Match one or more occurrences of the preceding element")
        elif char == '{':
            sequence.append("Specify a range of occurrences")
        elif char == '}':
            sequence.append("End of range specification")
        elif char == '(':
            sequence.append("Start of a group")
        elif char == ')':
            sequence.append("End of a group")
        elif char.isalnum() and not(brackets):
            sequence.append(f"Match '{char}'")
        else:
            if brackets:
                current_group += char

    return sequence

# Examples of generating and explaining regex patterns
regex_patterns = [r'O(P|Q|R)^+ 2(3|4)', r'A*B(C|D|E) E(G|H|i)^2', r'J^+K(L|M|N)*O? (P|Q)^3']
generators = [generate_string_regex_1, generate_string_regex_2, generate_string_regex_3]

for regex, generator in zip(regex_patterns, generators):
    generated_str = generator()
    print(f"String matching the regex '{regex}': {generated_str}")
    sequence = show_processing_sequence(regex)
    for step, explanation in enumerate(sequence, start=1):
        print(f"Phase {step}: {explanation}")
    print()
