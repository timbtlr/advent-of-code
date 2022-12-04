def get_input(file_name):
    input = None
    with open(file_name) as f:
        input = f.readlines()
    input = [line.replace("\n", "") for line in input]
    return input


def get_pairs(input):
    for line in input:
        pair = []
        for assignment in line.split(","):
            r = assignment.split("-")
            pair.append(set([i for i in range(int(r[0]), int(r[1]) + 1)]))
        yield pair


def part_1():
    input = get_input("src/2022/12-4/input.txt")
    overlaps = 0
    for pair in get_pairs(input):
        if pair[0].issubset(pair[1]) or pair[1].issubset(pair[0]):
            overlaps += 1
    return overlaps


def part_2():
    input = get_input("src/2022/12-4/input.txt")
    overlaps = 0
    for pair in get_pairs(input):
        if len(pair[0].intersection(pair[1])) > 0:
            overlaps += 1
    return overlaps


print(part_1(), part_2())
