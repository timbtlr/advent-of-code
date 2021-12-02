def get_total():
    file = open("aoc_12-2_input.txt", "r")
    file_lines = file.readlines()
    file.close()

    progress = depth = 0
    for line in file_lines:
        direction, increment = line.split(" ")
        if direction == "forward":
            progress += int(increment)
        elif direction == "down":
            depth += int(increment)
        elif direction == "up":
            depth -= int(increment)

    return progress * depth


print(get_total())
