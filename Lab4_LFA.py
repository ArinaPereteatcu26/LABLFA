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
