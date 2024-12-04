import re

DIRECTION_PAIRS = [
    ((-1, 1), (1, -1)),
    ((1, 1), (-1, -1)), 
]

def check_cross(grid, start_x, start_y):
    if grid[start_x][start_y] != "A":
        return False

    for pair_one, pair_two in DIRECTION_PAIRS:
        x_one, y_one = pair_one
        x_two, y_two = pair_two

        try:
            if start_x + x_one < 0 or start_y + y_one < 0 or start_x + x_two < 0 or start_y + y_two < 0:
                return False

            if sorted([
                grid[start_x + x_one][start_y + y_one], 
                grid[start_x + x_two][start_y + y_two]
            ]) != ["M", "S"]:
                return False
        except IndexError:
            return False
    
    return True



def solve(file_location):
    input = None
    with open(file_location) as f:
        input = f.readlines()

    grid = []
    for line in input:
        grid += [[i for i in line if i != "\n"]]

    total = 0

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if check_cross(grid, i, j):
                total += 1

    return total


print("Example Small", solve("example_small.txt"))
print("Example", solve("example.txt"))
print("Puzzle", solve("input.txt"))
