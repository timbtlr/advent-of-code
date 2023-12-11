from collections import defaultdict


def solve(file_location):
    puzzle_input = None
    with open(file_location) as f:
        puzzle_input = f.readlines()

    instructions = None
    node_links = defaultdict(lambda: {"L": None, "R": None})
    for index, line in enumerate(puzzle_input):
        line = line.replace("\n", "")
        if index == 0:
            instructions = list(line)
            continue

        if line.strip() == "":
            continue

        start, nodes = line.split(" = ")
        left, right = nodes.replace("(", "").replace(")", "").split(", ")
        node_links[start]["L"] = left
        node_links[start]["R"] = right

    found = False
    counter = 0
    current_node = "AAA"
    while not found:
        for instruction in instructions:
            current_node = node_links[current_node][instruction]
            counter += 1
            if current_node == "ZZZ":
                found = True
                break

    return counter


print("Example", solve("example.txt"))
print("Puzzle", solve("input.txt"))
