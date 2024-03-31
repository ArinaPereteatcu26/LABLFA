import random
# Function to generate a string that matches the given regex pattern
def generate_string_regex(regex_pattern):
    generated_string = ''
    for char in regex_pattern:
        if char.isalpha():
            generated_string += char
        elif char == '|':
            generated_string += random.choice(char)
        elif char == '(' or char == ')' or char == '?' or char == '^' or char == '+' or char == '{' or char == '}' or char == '*':
            continue
        elif char.isdigit():
            for _ in range(int(char)):
                generated_string += random.choice('0123456789')
    return generated_string


# Function to explain the regex pattern processing sequence
def show_processing_sequence(regex_pattern):
    sequence = []
    for char in regex_pattern:
        if char.isalpha():
            sequence.append(f"Match '{char}'")
        elif char == '|':
            sequence.append("Match one of the alternatives")
        elif char == '(':
            sequence.append("Start of a group")
        elif char == ')':
            sequence.append("End of a group")
        elif char == '?':
            sequence.append("Match zero or one occurrence of the preceding element")
        elif char == '^':
            sequence.append("Start of the line")
        elif char == '+':
            sequence.append("Match one or more occurrences of the preceding element")
        elif char == '*':
            sequence.append("Match zero or more occurrences of the preceding element")
        elif char == '{':
            sequence.append("Start of a range")
        elif char == '}':
            sequence.append("End of a range")
    return sequence


# Function to generate and explain regex patterns
def generate_and_explain(regex_patterns):
    for regex in regex_patterns:
        generated_str = generate_string_regex(regex)
        print(f"String matching the regex '{regex}': {generated_str}")
        sequence = show_processing_sequence(regex)
        for step, explanation in enumerate(sequence, start=1):
            print(f"Phase {step}: {explanation}")
        print()

# List of regex patterns
regex_patterns = [
    r'O(P|Q|R)^+ 2(3|4)',
    r'A*B(C|D|E) E(G|H|i)^2',
    r'J^+K(L|M|N)*O? (P|Q)^3'
]

# Generate and explain regex patterns
generate_and_explain(regex_patterns)
