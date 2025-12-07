from collections import defaultdict
import math

OP_MAP = {
    "+": sum,
    "*": math.prod
}
def solve(file_location):
    question_input = None
    with open(file_location) as f:
        question_input = f.readlines()

    
    inputs = defaultdict(list)
    for line in question_input:
        index = 0
        for token in line.strip("\n").split(" "):
            if token == "":
                continue
            inputs[index] += [token]
            index += 1

    total = 0
    for i in inputs.values():
        total += OP_MAP[i[-1]]([int(i) for i in i[:-1]])
    return total


print("Example", solve("example.txt"))
print("Puzzle", solve("input.txt"))
