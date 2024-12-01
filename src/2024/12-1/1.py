def solve(file_location):
    input = None
    with open(file_location) as f:
        input = f.readlines()

    left_side = []
    right_side = []

    for line in input:
        line = line.strip().split("   ")
        left_side += [line[0]]
        right_side += [line[1]]

    left_side = sorted(left_side)
    right_side = sorted(right_side)

    total_distance = 0
    for index, left_value in enumerate(left_side):
        right_value = right_side[index]
        total_distance += abs(int(right_value) - int(left_value))

    return total_distance


print("Example", solve("example.txt"))
print("Puzzle", solve("input.txt"))
