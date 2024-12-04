import re

DIRECTION_OFFSETS = {
    "N": (0, -1),
    "NE": (1, -1),
    "E": (1, 0),
    "SE": (1, 1),
    "S": (0, 1),
    "SW": (-1, 1),
    "W": (-1, 0),
    "NW": (-1, -1),
}
SEARCHED_WORD = ["X", "M", "A", "S"]

def check_direction(grid, direction, start_x, start_y):
    offset_x, offset_y = DIRECTION_OFFSETS[direction]
    x_coord = start_x 
    y_coord = start_y
    word_offset = 0

    while True:
        try:
            if x_coord < 0 or y_coord < 0:
                return False
            
            character = grid[x_coord][y_coord]
        except IndexError:
            return False
        
        if character != SEARCHED_WORD[word_offset]:
            return False

        word_offset += 1
        x_coord += offset_x
        y_coord += offset_y

        if word_offset >= len(SEARCHED_WORD):
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
            for direction in DIRECTION_OFFSETS.keys():
                if check_direction(grid, direction, i, j):
                    total += 1

    return total


print("Example Small", solve("example_small.txt"))
print("Example", solve("example.txt"))
print("Puzzle", solve("input.txt"))
