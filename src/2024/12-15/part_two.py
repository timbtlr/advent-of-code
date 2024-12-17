DIRECTION_OFFSETS = {
    ">": (0, 1),
    "<": (0, -1),
    "^": (-1, 0),
    "v": (1, 0)
}

import time

def print_grid(grid):
    for row in grid:
        s = ""
        for i in row:
            if i == 0:
                s += "."
            else:   
                s += str(i)
        print(s)

def parse_input(file_input):
    grid = []
    directions = []
    starting_location = None
    for row_index, line in enumerate(file_input):
        line = line.replace("\n", "")
        if "#" in line:
            row = []
            for col_index, char in enumerate(line):
                if char == "#":
                    row += [char, char]
                elif char == "O":
                    row += ["[", "]"]
                elif char == "@":
                    row += ["@", "."]
                else:
                    row += [".", "."]

                if char == "@":
                    starting_location = (row_index, col_index * 2)
            grid += [row]

        elif any([i in ["^", "<", ">", "v"] for i in line]):
            directions.extend(line)

    return grid, starting_location, directions

def move_in_grid(grid, starting_location, direction, move=True):
    row_offset, col_offset = DIRECTION_OFFSETS[direction]

    current_row = starting_location[0]
    current_col = starting_location[1]
    desired_row = current_row + row_offset
    desired_col = current_col + col_offset
    current_node = grid[current_row][current_col]

    if current_node == "#":
        return False, (current_row, current_col)
    
    desired_node = grid[desired_row][desired_col]
    if current_node == "@" and desired_node == ".":
        if move:
            grid[desired_row][desired_col] = current_node
            grid[current_row][current_col] = "."
            return True, (desired_row, desired_col)
        return True, (current_row, current_col)
        
    if direction in ["<", ">"]:
        if desired_node == ".":
            if move:
                grid[desired_row][desired_col] = current_node
                grid[current_row][current_col] = "."
                return True, (desired_row, desired_col)
            return True, (current_row, current_col)
        can_move, _ = move_in_grid(grid, (desired_row, desired_col), direction)
        if can_move:
            if move: 
                grid[desired_row][desired_col] = current_node
                grid[current_row][current_col] = "."
                return True, (desired_row, desired_col)
            
            return True, (current_row, current_col)
        
        return False, (current_row, current_col)
        
    else:
        offset = 0
        if current_node == "[":
            offset = 1
        elif current_node == "]":
            offset = -1

        if offset == 0:
            if current_node == ".":
                return True, (current_row, current_col)
            
            can_move, _ = move_in_grid(grid, (desired_row, desired_col), direction)
            if can_move:
                if move: 
                    grid[desired_row][desired_col] = current_node
                    grid[current_row][current_col] = "."
                    return True, (desired_row, desired_col)
                
                return True, (current_row, current_col)
            
            return False, (current_row, current_col)

        if grid[desired_row][desired_col] == "." and grid[desired_row][desired_col + offset] == ".":
            if move:
                grid[desired_row][desired_col] = current_node
                grid[current_row][current_col] = "."
                grid[desired_row][desired_col + offset] = grid[current_row][current_col + offset]
                grid[current_row][current_col + offset] = "."
                return True, (desired_row, desired_col)
            
            return True, (current_row, current_col)

        can_move_this, _ = move_in_grid(grid, (desired_row, desired_col), direction, move=False)
        can_move_other, _ = move_in_grid(grid, (desired_row, desired_col + offset), direction, move=False)

        if can_move_this and can_move_other:
            if move:
                move_in_grid(grid, (desired_row, desired_col), direction)
                move_in_grid(grid, (desired_row, desired_col + offset), direction)
                grid[desired_row][desired_col] = current_node
                grid[current_row][current_col] = "."
                grid[desired_row][desired_col + offset] = grid[current_row][current_col + offset]
                grid[current_row][current_col + offset] = "."
                return True, (desired_row, desired_col)
            
            return True, (current_row, current_col)

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
            if node == "[":
                total += (100 * row_index) + col_index

    return total
    
print("Simple Example", solve("example_simple.txt"))
print("Example", solve("example.txt"))
print("Puzzle", solve("input.txt"))
