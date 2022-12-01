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

        x_increment = 1 if x2 > x1 else -1
        y_increment = 1 if y2 > y1 else -1

        if x1 == x2:
            for i in range(y1, y2 + y_increment, y_increment):
                plotted[(x1, i)] = plotted.get((x1, i), 0) + 1

        elif y1 == y2:
            for i in range(x1, x2 + x_increment, x_increment):
                plotted[(i, y1)] = plotted.get((i, y1), 0) + 1

        else:
            done = False
            while ((x1 != x2 or y1 != y2) and not done) or (x1 == x2 and y1 == y2):
                plotted[(x1, y1)] = plotted.get((x1, y1), 0) + 1
                x1 = x1 + x_increment
                y1 = y1 + y_increment
                if x1 == x2 and y1 == y2:
                    done = True

    return len([(key, value) for key, value in plotted.items() if value >= 2])


print(solve())
