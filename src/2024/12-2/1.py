def solve(file_location):
    input = None
    with open(file_location) as f:
        input = f.readlines()

    safe = []

    for line in input:
        line = [int(i) for i in line.strip().split(" ")]

        directions = []
        for index in range(1, len(line)):
            directions += [line[index-1] - line[index]]

        if not all([i > 0 for i in directions]) and not all([i < 0 for i in directions]):
            continue

        if not all([abs(i) >=1 and abs(i) <= 3 for i in directions]):
            continue

        safe += [line]
        print("SAFE", line) 

    return len(safe)


print("Example", solve("example.txt"))
print("Puzzle", solve("input.txt"))
