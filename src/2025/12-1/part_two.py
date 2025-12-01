def solve(file_location):
    question_input = None
    with open(file_location) as f:
        question_input = f.readlines()

    dial_cursor = 50
    zero_count = 0

    for line in question_input:
        direction = line[0]
        number = int(line[1:])
        previous_dial_cursor = dial_cursor

        if direction == "L":
            dial_cursor -= number
        else:
            dial_cursor += number

        if dial_cursor in [0, 100]:
            zero_count += 1
            dial_cursor = 0

        elif dial_cursor < 0:
            if previous_dial_cursor == 0:
                zero_count += int((number - previous_dial_cursor) / 100)
            else: 
                zero_count += 1 + int((number - previous_dial_cursor) / 100)
            dial_cursor = 100 - (abs(dial_cursor) % 100)
            
        elif dial_cursor > 99:
            zero_count += 1 + int((number - (100 - previous_dial_cursor)) / 100)
            dial_cursor = dial_cursor % 100
        
        if dial_cursor == 100:
            dial_cursor = 0

    return zero_count


print("Example", solve("example.txt"))
print("Puzzle", solve("input.txt")) # 6133
