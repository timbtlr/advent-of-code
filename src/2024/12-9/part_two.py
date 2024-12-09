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
            taken_spaces += [(len(file_layout), len(file_layout) + int(char))]
            file_layout.extend([f"{counter}"] * int(char))
            counter += 1

        else:
            free_spaces += [(len(file_layout), len(file_layout) + int(char), int(char))]
            file_layout.extend(["."] * int(char))

    for start, end in reversed(taken_spaces):
        length = end - start
        
        for slot_index, free_slot in enumerate(free_spaces):
            slot_start, slot_end, slot_length = free_slot

            if slot_start >= start:
                break

            if slot_length >= length: 
                file_layout[slot_start:slot_start + length] = file_layout[start:end]
                file_layout[start:end] = ["."] * length

                if slot_start + length == slot_end:
                    del free_spaces[slot_index]

                else:
                    free_spaces[slot_index] = (slot_start + length, slot_end, slot_length - length)

                break

        
    totals = []
    for index, char in enumerate(file_layout):
        if char == ".":
            continue

        totals += [index * int(char)]
        
    return sum(totals)

print("Example", solve("example.txt"))
print("Puzzle", solve("input.txt"))
