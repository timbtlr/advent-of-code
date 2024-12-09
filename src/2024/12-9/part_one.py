def solve(file_location):
    file_input = None
    with open(file_location) as f:
        file_input = f.readlines()
        
    file_layout = []
    taken_spaces = []
    free_spaces = []
    counter = 0
    for index, char in enumerate(file_input[0]):
        if char == "\n":
            continue

        if index % 2 == 0:
            taken_spaces.extend([len(file_layout) + i for i in range(int(char))])
            file_layout.extend([f"{counter}"] * int(char))
            counter += 1
        else:
            free_spaces.extend([len(file_layout) + i for i in range(int(char))])
            file_layout.extend(["."] * int(char))

    while free_spaces[0] < taken_spaces[-1]:
        file_layout[free_spaces.pop(0)] = file_layout.pop(taken_spaces.pop(-1))
        file_layout.extend(["."])
        
    totals = []
    for index, char in enumerate(file_layout):
        if char == ".":
            break

        totals += [index * int(char)]
        
    return "".join(file_layout), sum(totals)

print("Example", solve("example.txt"))
print("Puzzle", solve("input.txt"))
