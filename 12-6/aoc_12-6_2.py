from collections import Counter
import numpy as np


def solve():
    file = open("aoc_12-6_input.txt", "r")
    file_lines = file.read().splitlines()
    file.close()

    fish = {}
    for entry in [int(i) for i in file_lines[0].split(",")]:
        fish[entry] = fish.get(entry, 0) + 1

    for i in range(0, 256):
        for countdown in range(-1, 9):
            fish[countdown] = fish.get(countdown + 1, 0)

        new_fish = fish.get(-1, 0)
        if new_fish:
            fish[8] = new_fish
            fish[6] = fish.get(6, 0) + new_fish
        del fish[-1]
    return sum(fish.values())


print(solve())
