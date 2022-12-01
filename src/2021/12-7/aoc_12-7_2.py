import statistics
from math import floor


def fuel_usage(start, dest):
    fuel = 0
    inc = 1 if dest > start else -1
    for i in range(start, dest + inc, inc):
        fuel += abs(start - i)
    return fuel


def solve():
    file = open("aoc_12-7_input.txt", "r")
    file_lines = file.read().splitlines()
    file.close()

    input = [int(i) for i in file_lines[0].split(",")]
    mean = floor(statistics.mean(input))
    return sum([fuel_usage(i, mean) for i in input])


print(solve())
