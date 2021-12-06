from collections import Counter
import numpy as np


def solve():
    file = open("aoc_12-6_input.txt", "r")
    file_lines = file.read().splitlines()
    file.close()

    fish = np.array([int(i) for i in file_lines[0].split(",")])
    print("DAY 0", len(fish))

    for i in range(0, 256):
        fish = fish - 1
        new_fish = len(fish[fish < 0])
        fish = np.where(fish < 0, 6, fish)
        fish = np.pad(fish, (0, new_fish), "constant", constant_values=(0, 8))
        print(f"DAY {i+1}", len(fish))


print(solve())
