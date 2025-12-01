import itertools
from copy import copy

def parse_input(file_input):
    available = []
    desired = []
    for line in file_input:
        line = line.replace("\n", "").strip()
        if not line:
            continue

        if "," in line:
            available = line.split(", ")

        else:
            desired += [line]
        

    return available, desired


def solve(file_location):
    file_input = None
    with open(file_location) as f:
        file_input = f.readlines()

    patterns_available, patterns_desired = parse_input(file_input)
    patterns_found = set(patterns_available)

    def test_substring(substring, tested_string="", tested=None):
        if tested is None:
            tested = []

        tested_patterns = tested

        if substring in tested_patterns and substring not in patterns_found:
            return False
        
        if substring == "":
            return True
        
        if substring in patterns_found:
            return True
        
        tested_patterns += [substring]
        
        for pattern in patterns_available:
            if substring[:len(pattern)] == pattern:
                matched_substring = f"{tested_string}{substring[:len(pattern)]}"
                new_substring = substring[len(pattern):]
                patterns_found.add(matched_substring)
                
                can_be_made = test_substring(new_substring, matched_substring, tested)
                if not can_be_made:
                    continue

                return can_be_made
                
        return False
    
    can_make = []
    for pattern in patterns_desired:
        if test_substring(pattern):
            can_make += [pattern]

    return len(can_make)
    

print("Example", solve("example.txt"))
print("Puzzle", solve("input.txt"))