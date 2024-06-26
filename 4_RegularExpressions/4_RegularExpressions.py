import re
import random

def generate_strings_for_regex(regex_list):
    generated_strings_list = []
    for regex_list_item in regex_list:
        regex = random.choice(regex_list_item)
        print("Processing regex:", regex)
        try:
            # Compile the regular expression pattern
            pattern = re.compile(regex)
            # Initialize an empty set to store already generated strings for this regex
            generated_set = set()
            # Initialize an empty list to store valid strings for this regex
            generated_strings = []
            # Generate strings until we reach the limit
            attempts = 0
            while len(generated_strings) < 3 and attempts < 100:
                generated_string, steps = generate_string(regex)
                # Check if the generated string matches the regular expression and is not already generated
                if pattern.fullmatch(generated_string) and generated_string not in generated_set:
                    generated_set.add(generated_string)
                    generated_strings.append((generated_string, steps))
                attempts += 1
            generated_strings_list.append(generated_strings)
        except re.error:
            print("Invalid regex:", regex)
    return generated_strings_list

def generate_string(regex):
    string = ""
    steps = []
    i = 0
    while i < len(regex):
        if regex[i] == "(" and regex.find(")", i) == len(regex) - 1 or (regex[i] == "(" and regex[regex.find(")", i) + 1] not in ["*", "+", "?", "{"]):
            char = random.choice(options(re.findall(r'\((.*?)\)', regex[i:])[0]))
            string += char
            steps.append(f"Adding {char} to string - {string}")
            i = regex.find(")", i)
        elif regex[i] == "(" and regex[regex.find(")", i) + 1] == "+":
            times = random.randint(1, 5)
            for _ in range(times):
                char = random.choice(options(re.findall(r'\((.*?)\)', regex[i:])[0]))
                string += char
                steps.append(f"Adding {char} to string - {string}")
            i = regex.find(")", i) + 1
        elif regex[i] == "(" and regex[regex.find(")", i) + 1] == "*":
            for _ in range(random.randint(0, 5)):
                char = random.choice(options(re.findall(r'\((.*?)\)', regex[i:])[0]))
                string += char
                steps.append(f"Adding {char} to string - {string}")
            i = regex.find(")", i) + 1
        elif regex[i] == "(" and regex[regex.find(")", i) + 1] == "{":
            for _ in range(int(regex[regex.find("{", i) + 1])):
                char = random.choice(options(re.findall(r'\((.*?)\)', regex[i:])[0]))
                string += char
                steps.append(f"Adding {char} to string - {string}")
            i = regex.find("}", i) + 1
        elif regex[i] == "(" and regex[regex.find(")", i) + 1] == "?":
            if random.randint(0, 1):
                char = random.choice(options(re.findall(r'\((.*?)\)', regex[i:])[0]))
                string += char
                steps.append(f"Adding {char} to string - {string}")
            i = regex.find(")", i) + 1
        elif i < len(regex) - 2 and regex[i + 1] == "?":
            if random.randint(0, 1):
                string += regex[i]
                steps.append(f"Adding {regex[i]} to string - {string}")
            i += 2
        elif regex[i] in '(){|+*?}':
            i += 1
        else:
            string += regex[i]
            steps.append(f"Adding {regex[i]} to string - {string}")
            i += 1
    return string, steps

def options(sequence):
    return sequence.split("|")

regex_list = [
    ["O(P|Q|R)+ 2(3|4)", "O(P|Q|R)+ 2(3|4)", "O(P|Q|R)+ 2(3|4)"],
    ["A*B(C|D|E) F(G|H|i){2}", "A*B(C|D|E) F(G|H|i){2}", "A*B(C|D|E) F(G|H|i){2}"],
    ["J^+K(L|M|N)*O? (P|Q){3}", "J^+K(L|M|N)*O? (P|Q){3}", "J^+K(L|M|N)*O? (P|Q){3}"]
]





generated_strings_list = generate_strings_for_regex(regex_list)
print("Generated strings for each regex:")
for i, regex_strings in enumerate(generated_strings_list):
    print(f"For regex list {i + 1}:")
    for string, steps in regex_strings:
        print(f"  Generated string: {string}")
        print("  Processing steps:")
        for step in steps:
            print(f"    - {step}")
