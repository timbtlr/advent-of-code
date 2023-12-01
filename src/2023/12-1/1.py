def solve(file_location):
    input = None
    with open(file_location) as f:
        input = f.readlines()

    all_calibration_digits = []
    for line in input:
        line_digits = [i for i in line if i.isdigit()]
        all_calibration_digits += [int(f"{line_digits[0]}{line_digits[-1]}")]

    return sum(all_calibration_digits)


print("Example", solve("example.txt"))
print("Puzzle", solve("input.txt"))
