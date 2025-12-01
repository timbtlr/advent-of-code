from collections import defaultdict

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
    patterns_found = defaultdict(lambda: 0)
    total_mappings = defaultdict(lambda: 0)

    def test_substring(original_string, substring, tested_string="", tested=None):
        if tested is None:
            tested = []

        tested_patterns = tested
        if substring in tested_patterns and substring not in patterns_found.keys():
            print(1)
            return False
        
        if substring == "":
            print(2)
            return 1
        
        if substring in patterns_found:
            print("can be made", original_string, substring)
            total_mappings[original_string] += 1
            return True
        
        tested_patterns += [substring]
        
        for pattern in patterns_available:
            if substring[:len(pattern)] == pattern:
                print("Substring", substring, "pattern", pattern)
                matched_substring = f"{tested_string}{substring[:len(pattern)]}"
                new_substring = substring[len(pattern):]
                patterns_foundmatched_substring)
                
                can_be_made = test_substring(original_string, new_substring, matched_substring, tested)
                if can_be_made:
                    print("can be made", original_string, matched_substring)
                    total_mappings[original_string] += 1

                # return can_be_made
        
        return False
    
    can_make = []
    for pattern in patterns_desired:
        if test_substring(pattern, pattern):
            can_make += [pattern]
        input()

    

    return len(can_make), sum([i for i in total_mappings.values()])
    

print("Example", solve("example.txt"))
#print("Puzzle", solve("input.txt"))