from collections import defaultdict

def solve(file_location):
    input = None
    with open(file_location) as f:
        input = f.readlines()

    left_side = []
    right_side = []

    for line in input:
        line = line.strip().split("   ")
        left_side += [line[0]]
        right_side += [line[1]]

    appearances = defaultdict(lambda: 0)
    for left_value in left_side:
        if appearances.get(left_value) is None:
            appearances[left_value] = len([i for i in right_side if i == left_value])

    total = 0
    for left_value in left_side:
        total += int(left_value) * int(appearances[left_value])

    return total


print("Example", solve("example.txt"))
print("Puzzle", solve("input.txt"))
