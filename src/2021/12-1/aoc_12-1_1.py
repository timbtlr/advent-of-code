def get_increments():
    input = None
    with open("src/2021/12-1/aoc_12-1_input.txt") as f:
        input = f.readlines()

    increments = 0
    current = previous = None
    for line in input:
        previous = current
        current = int(line) if line else None
        if current and previous and current > previous:
            increments += 1
    return increments


increments = get_increments()
print(increments)
