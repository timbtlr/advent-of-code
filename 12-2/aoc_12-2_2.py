def get_total():
    file = open("aoc_12-2_input.txt", "r")
    file_lines = file.readlines()
    file.close()

    progress = depth = aim = 0
    for line in file_lines:
        direction, increment = line.split(" ")
        increment = int(increment)
        if direction == "forward":
            progress += increment
            depth += aim * increment
        elif direction == "down":
            aim += increment
        elif direction == "up":
            aim -= increment

    return progress * depth


print(get_total())
