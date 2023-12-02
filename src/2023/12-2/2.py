import re
from collections import defaultdict
from functools import reduce


def solve(file_location):
    puzzle_input = None
    with open(file_location) as f:
        puzzle_input = f.readlines()

    def parse_line(line):
        game_number = None
        color_map = defaultdict(list)

        game, colors = line.split(": ")
        _, game_number = game.split("Game ")

        colors = re.split(";|,", colors)
        for color in colors:
            value, key = color.strip().split(" ")
            color_map[key] += [int(value)]

        return int(game_number), dict(color_map)

    total = []
    for line in puzzle_input:
        _, color_map = parse_line(line)
        total += [
            reduce((lambda x, y: x * y), [max(value) for value in color_map.values()])
        ]

    return sum(total)


print("Example", solve("example.txt"))
print("Puzzle", solve("input.txt"))
