from collections import Counter
from copy import deepcopy


def solve():
    file = open("aoc_12-3_input.txt", "r")
    file_lines = file.read().splitlines()
    file.close()

    oxygen_readings = dioxide_readings = deepcopy(file_lines)

    for index in range(0, len(file_lines[0])):
        common_output = Counter([line[index] for line in file_lines]).most_common()
        if common_output[0][1] == common_output[1][1]:
            common_value = "1"
        else:
            common_value = common_output[0][0]

        if len(oxygen_readings) > 1:
            oxygen_readings = [i for i in oxygen_readings if i[index] == common_value]
        if len(dioxide_readings) > 1:
            dioxide_readings = [i for i in dioxide_readings if i[index] != common_value]

        print(oxygen_readings)


print(solve())
