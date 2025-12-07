from collections import defaultdict
import math

OP_MAP = {
    "+": sum,
    "*": math.prod
}
def solve(file_location):
    question_input = None
    with open(file_location) as f:
        question_input = f.readlines()

    column_separators = []
    max_line_length = max([len(line.strip("\n")) for line in question_input])
    for i in range(max_line_length):
        if all([line[i] == " " for line in question_input]):
            column_separators += [i]
    column_separators += [max_line_length]

    inputs = defaultdict(list)
    for line in question_input:
        input_index = 0
        column_index = 0
        for separator in column_separators:
            inputs[input_index] += [line[column_index:separator]]
            column_index = separator + 1
            input_index += 1
                    
    total = 0
    for column in inputs.values():
        operator = OP_MAP[column.pop(-1).strip()]
        max_character_size = max([len(str(i)) for i in column])
        reordered_column = ["" for _ in range(max_character_size)]
        for index in range(max_character_size-1, -1, -1):
            for value in column:
                try:
                    reordered_column[index] += value[index]
                except IndexError:
                    pass

        total += operator([int(i.strip()) for i in reordered_column])
    return total


print("Example", solve("example.txt"))
print("Puzzle", solve("input.txt"))
