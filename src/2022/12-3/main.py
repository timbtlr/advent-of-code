def get_input(file_name):
    input = None
    with open(file_name) as f:
        input = f.readlines()
    input = [line.replace("\n", "") for line in input]
    return input


priorities = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"


def part_1():
    intersection = []
    lines = get_input("src/2022/12-3/input.txt")
    for line in lines:
        middle = int(len(line) / 2)
        intersection += list(set([i for i in line[:middle] if i in line[middle:]]))
    return sum([priorities.index(i) for i in intersection])


def part_2():
    lines = get_input("src/2022/12-3/input.txt")
    groups = [lines[i : i + 3] for i in range(0, len(lines), 3)]
    intersection = []
    for group in groups:
        intersection += list(set([i for i in group[0] if i in group[1] and i in group[2]]))
    return sum([priorities.index(i) for i in intersection])


print(part_1(), part_2())
