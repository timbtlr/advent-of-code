def solve(file_location):
    input = None
    with open(file_location) as f:
        input = f.readlines()

    safe = []

    def is_safe(line):
        directions = []
        for index in range(1, len(line)):
            directions += [line[index-1] - line[index]]

        if not all([i > 0 for i in directions]) and not all([i < 0 for i in directions]):
            return False

        if not all([abs(i) >=1 and abs(i) <= 3 for i in directions]):
            return False

        return True

    for line in input:
        line = [int(i) for i in line.strip().split(" ")]

        for i in range(-1, len(line)):
            line_copy = line.copy()
            if i >= 0:
                line_copy.pop(i)
            if is_safe(line_copy):
                safe += [line]
                break

    return len(safe)


print("Example", solve("example.txt"))
print("Puzzle", solve("input.txt"))
