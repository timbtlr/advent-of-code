DIRECTION_OFFSETS = {
    ">": (0, 1),
    "<": (0, -1),
    "^": (-1, 0),
    "v": (1, 0)
}

def check_node(grid, row_index, column_index):
    if row_index < 0 or column_index < 0:
        return False

    try:
        if grid[row_index][column_index] != value:
            return False
    except IndexError:
        return False
    
    return True

def parse_input(file_input):
    grid = []
    directions = []
    starting_location = None
    for row_index, line in enumerate(file_input):
        line = line.replace("\n", "")
        if "#" in line:
            row = []
            for col_index, char in enumerate(line):
                row += [char]
                if char == "@":
                    starting_location = (row_index, col_index)
            grid += [row]

        elif any([i in ["^", "<", ">", "v"] for i in line]):
            directions.extend(line)

    return grid, starting_location, directions

def move_in_grid(grid, starting_location, direction):
    row_offset, col_offset = DIRECTION_OFFSETS[direction]

    current_row = starting_location[0]
    current_col = starting_location[1]
    desired_row = current_row + row_offset
    desired_col = current_col + col_offset

    if grid[desired_row][desired_col] == "#":
        return False, (current_row, current_col)

    if grid[desired_row][desired_col] == ".":
        grid[desired_row][desired_col] = grid[current_row][current_col]
        grid[current_row][current_col] = "."
        return True, (desired_row, desired_col)
    
    can_move, _ = move_in_grid(grid, (desired_row, desired_col), direction)
    if can_move: 
        grid[desired_row][desired_col] = grid[current_row][current_col]
        grid[current_row][current_col] = "."
        return True, (desired_row, desired_col)
    
    return False, (current_row, current_col)


def solve(file_location):
    file_input = None
    with open(file_location) as f:
        file_input = f.readlines()

    grid, current_location, directions = parse_input(file_input)

    for direction in directions:
        _, current_location = move_in_grid(grid, current_location, direction)

    total = 0
    for row_index, row in enumerate(grid):
        for col_index, node in enumerate(row):
            if node == "O":
                total += (100 * row_index) + col_index

    return total
    
print("Simple Example", solve("example_simple.txt"))
print("Example", solve("example.txt"))
print("Puzzle", solve("input.txt"))
