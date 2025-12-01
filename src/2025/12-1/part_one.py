def solve(file_location):
    question_input = None
    with open(file_location) as f:
        question_input = f.readlines()

    dial_cursor = 50
    zero_count = 0

    for line in question_input:
        direction = line[0]
        number = int(line[1:])

        if direction == "L":
            dial_cursor -= number
        else:
            dial_cursor += number

        if dial_cursor < 0:
            dial_cursor = 100 - (abs(dial_cursor) % 100)
        elif dial_cursor > 99:
            dial_cursor = (dial_cursor % 100)     

        if dial_cursor == 100:
            dial_cursor = 0

        if dial_cursor == 0:
            zero_count += 1


    return zero_count


print("Example", solve("example.txt"))

print("Puzzle", solve("input.txt"))
