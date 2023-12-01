import re

STRING_DIGITS = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}


def solve(file_location):
    puzzle_input = None
    with open(file_location) as f:
        puzzle_input = f.readlines()

    all_calibration_digits = []
    for line in puzzle_input:
        index_map = {
            index: int(value) for index, value in enumerate(line) if value.isdigit()
        }
        for key, value in STRING_DIGITS.items():
            for index in [s.start() for s in re.finditer(key, line)]:
                index_map[index] = int(value)
        sorted_digits = [i[1] for i in sorted(index_map.items())]
        all_calibration_digits += [int(f"{sorted_digits[0]}{sorted_digits[-1]}")]

    return sum(all_calibration_digits)


print("Example", solve("example.txt"))
print("Puzzle", solve("input.txt"))
