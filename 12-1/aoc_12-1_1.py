def get_increments():
    file = open("aoc_12-1_input.txt", "r")
    Lines = file.readlines()
    file.close()
    
    increments = 0
    current = previous = None
    for line in Lines:
        previous = current
        current = int(line) if line else None
        if current and previous and current > previous:
            increments += 1
    return increments


increments = get_increments()
print(increments)
