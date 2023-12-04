from collections import defaultdict


def solve(file_location):
    puzzle_input = None
    with open(file_location) as f:
        puzzle_input = f.readlines()

    def parse_line(line):
        _, numbers = line.split(": ")
        winning_numbers, game_numbers = numbers.split(" | ")
        winning_numbers = [int(i) for i in winning_numbers.split(" ") if i != ""]
        game_numbers = [int(i) for i in game_numbers.split(" ") if i != ""]

        return winning_numbers, game_numbers

    copy_map = defaultdict(lambda: 1)
    copy_map[1] = 1

    for index, line in enumerate(puzzle_input):
        index = index + 1
        winning_numbers, game_numbers = parse_line(line)
        matches = [i for i in game_numbers if i in winning_numbers]

        for _ in range(copy_map[index]):
            for i in range(len(matches)):
                copy_map[index + i + 1] += 1

    return sum(copy_map.values())


print("Example", solve("example.txt"))
print("Puzzle", solve("input.txt"))
