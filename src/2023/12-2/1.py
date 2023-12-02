import re
from collections import defaultdict

MAX_COLORS = {"red": 12, "green": 13, "blue": 14}


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

    possible_games = []
    for line in puzzle_input:
        game_number, color_map = parse_line(line)
        if all(
            [
                max(color_map[color]) <= max_count
                for color, max_count in MAX_COLORS.items()
            ]
        ):
            possible_games += [game_number]

    return sum(possible_games)


print("Example", solve("example.txt"))
print("Puzzle", solve("input.txt"))
