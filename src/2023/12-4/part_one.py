def solve(file_location):
    puzzle_input = None
    with open(file_location) as f:
        puzzle_input = f.readlines()

    def parse_line(line):
        game, numbers = line.split(": ")
        _, game_number = game.split("Card ")

        winning_numbers, game_numbers = numbers.split(" | ")
        winning_numbers = [int(i) for i in winning_numbers.split(" ") if i != ""]
        game_numbers = [int(i) for i in game_numbers.split(" ") if i != ""]

        return int(game_number), winning_numbers, game_numbers

    scores = []
    for line in puzzle_input:
        game_number, winning_numbers, game_numbers = parse_line(line)
        matches = [i for i in game_numbers if i in winning_numbers]
        if len(matches) == 0:
            continue

        if len(matches) == 1:
            scores += [1]
            continue

        scores += [1 * (2 ** (len(matches) - 1))]

    return sum(scores)


print("Example", solve("example.txt"))
print("Puzzle", solve("input.txt"))
