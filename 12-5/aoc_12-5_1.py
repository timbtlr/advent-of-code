from collections import Counter
import numpy as np


def solve():
    file = open("aoc_12-5_input.txt", "r")
    file_lines = file.read().splitlines()
    file.close()

    plotted = {}

    for line in file_lines:
        first_coord, second_coord = line.split(" -> ")
        x1, y1 = first_coord.split(",")
        x2, y2 = second_coord.split(",")
        x1 = int(x1)
        x2 = int(x2)
        y1 = int(y1)
        y2 = int(y2)

        if x1 == x2:
            increment = 1 if y2 > y1 else -1
            for i in range(y1, y2 + increment, increment):
                plotted[(x1, i)] = plotted.get((x1, i), 0) + 1

        if y1 == y2:
            increment = 1 if x2 > x1 else -1
            for i in range(x1, x2 + increment, increment):
                plotted[(i, y1)] = plotted.get((i, y1), 0) + 1

    return len([(key, value) for key, value in plotted.items() if value >= 2])


print(solve())
