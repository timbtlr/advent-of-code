import math
from collections import defaultdict


def solve(file_location):
    puzzle_input = None
    with open(file_location) as f:
        puzzle_input = f.readlines()

    instructions = None
    walking_nodes = []
    node_links = defaultdict(lambda: {"L": None, "R": None})
    for index, line in enumerate(puzzle_input):
        line = line.replace("\n", "")
        if index == 0:
            instructions = list(line)
            continue

        if line.strip() == "":
            continue

        start, nodes = line.split(" = ")
        if start[-1] == "A":
            walking_nodes += [start]
        left, right = nodes.replace("(", "").replace(")", "").split(", ")
        node_links[start]["L"] = left
        node_links[start]["R"] = right

    steps_per_node = []
    for index, label in enumerate(walking_nodes):
        counter = 0
        found = False
        while not found:
            for instruction in instructions:
                counter += 1
                label = node_links[label][instruction]
                if label[-1] == "Z":
                    steps_per_node += [counter]
                    found = True
                    break

    return math.lcm(*steps_per_node)


print("Example", solve("example_two.txt"))
print("Puzzle", solve("input.txt"))
