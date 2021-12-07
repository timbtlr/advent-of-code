import statistics


def solve():
    file = open("aoc_12-7_input.txt", "r")
    file_lines = file.read().splitlines()
    file.close()

    input = [int(i) for i in file_lines[0].split(",")]
    median = statistics.median(input)
    return sum([abs(i - median) for i in input])


print(solve())
