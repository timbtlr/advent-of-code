from collections import defaultdict
import re

DESIRED_STRING_SIZE = 12

def check_string(current_string, remaining_string):
    if len(current_string) == DESIRED_STRING_SIZE:
        return current_string

    if (len(current_string) + len(remaining_string)) < DESIRED_STRING_SIZE:
        return None
    
    max_number = 0
    for i in range(9, 0, -1):
        indexes_to_check = [m.start() for m in re.finditer(str(i), remaining_string)]
        indexes_to_check = [i for i in indexes_to_check if len(current_string + remaining_string[i:]) >= DESIRED_STRING_SIZE]
        
        if indexes_to_check:
            testable_string = f"{current_string}{i}"
            for index in indexes_to_check:
                new_max = check_string(testable_string, remaining_string[index+1:])
                if new_max is not None:
                    max_number = max(max_number, int(new_max))
            break

    return max_number

def solve(file_location):
    question_input = None
    with open(file_location) as f:
        question_input = f.readlines()

    values = []

    for line in question_input:
        result = check_string("", line.strip("\n"))
        values += [result]

    return sum(values)


print("Example", solve("example.txt"))
print("Puzzle", solve("input.txt"))
