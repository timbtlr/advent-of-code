from collections import Counter


def solve():
    file = open("aoc_12-3_input.txt", "r")
    file_lines = file.read().splitlines()
    file.close()

    gamma = []
    epsilon = []

    for i in range(0, len(file_lines[0])):
        common_output = Counter([line[i] for line in file_lines]).most_common()
        if common_output[0][1] == common_output[1][1]:
            gamma.append("1")
            epsilon.append("0")
        else:
            gamma.append(common_output[0][0])
            epsilon.append(common_output[-1][0])

    return int("".join(gamma), 2) * int("".join(epsilon), 2)


print(solve())
