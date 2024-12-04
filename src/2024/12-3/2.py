import re

def solve(file_location):
    input = None
    with open(file_location) as f:
        input = f.readlines()

    totals = []
    enabled=True

    for line in input:
        matching = re.findall("(mul\(\d{1,3}\,\d{1,3}\)|do\(\)|don\'t\(\))", line)
        for match in matching:
            print(match)
            if match == "do()":
                enabled = True
            elif match == "don't()":
                enabled = False
            else:
                if enabled:
                    values = [int(i) for i in match.strip("mul(").strip(")").split(",")]
                    totals += [values[0] * values[1]]

    return sum(totals)


print("Example", solve("example.txt"))
print("Puzzle", solve("input.txt"))
