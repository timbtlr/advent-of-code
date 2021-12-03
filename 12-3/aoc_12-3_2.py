from collections import Counter
from copy import deepcopy


def solve():
    file = open("aoc_12-3_input.txt", "r")
    file_lines = file.read().splitlines()
    file.close()

    oxygen_readings = dioxide_readings = deepcopy(file_lines)

    for index in range(0, len(file_lines[0])):
        if len(oxygen_readings) > 1:
            common_output = Counter([l[index] for l in oxygen_readings]).most_common()
            if len(common_output) > 1 and common_output[0][1] == common_output[1][1]:
                most_common_value = "1"
            else:
                most_common_value = common_output[0][0]

            oxygen_readings = [
                i for i in oxygen_readings if i[index] == most_common_value
            ]

        if len(dioxide_readings) > 1:
            common_output = Counter([l[index] for l in dioxide_readings]).most_common()
            if len(common_output) > 1 and common_output[0][1] == common_output[1][1]:
                least_common_value = "0"
            else:
                least_common_value = common_output[-1][0]

            dioxide_readings = [
                i for i in dioxide_readings if i[index] == least_common_value
            ]

    return int("".join(oxygen_readings), 2) * int("".join(dioxide_readings), 2)


print(solve())
