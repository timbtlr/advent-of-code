def get_increments():
    file = open("aoc_12-1_input.txt", "r")
    line_list = list(map(int, file.readlines()))
    file.close()

    increments = 0
    current = previous = None
    for i in range(0, len(line_list)):
        segment = line_list[i : i + 3]
        if len(segment) == 3:
            previous = current
            current = sum(segment)
            if current and previous and current > previous:
                increments += 1
    return increments


print(get_increments())
