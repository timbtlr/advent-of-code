def get_input(file_name):
    input = None
    with open(file_name) as f:
        input = f.readlines()
    for line in input:
        yield line.replace("\n", "")


score_map = {
    "X": 1,
    "Y": 2,
    "Z": 3,
}
win_map = {
    "A": "Y",
    "B": "Z",
    "C": "X",
}
tie_map = {
    "A": "X",
    "B": "Y",
    "C": "Z",
}
lose_map = {
    "A": "Z",
    "B": "X",
    "C": "Y",
}

def part_1():
    total = 0
    for line in get_input("src/2022/12-2/input.txt"):
        opponent, me = line.split(" ")
        total += score_map[me]
        if tie_map[opponent] == me:
            total += 3
        elif win_map[opponent] == me:
            total += 6
    return total

def part_2():
    total = 0
    for line in get_input("src/2022/12-2/input.txt"):
        opponent, should_win = line.split(" ")
        match should_win:
            case "X":
                total += score_map[lose_map[opponent]]
            case "Y":
                total += 3 + score_map[tie_map[opponent]]
            case "Z":
                total += 6 + score_map[win_map[opponent]]
    return total


print(part_1(), part_2())
