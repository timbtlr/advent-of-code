from collections import defaultdict
from collections import Counter

import copy

def get_steps_to(source_coords, dest_coords):
    return abs(source_coords[0] - dest_coords[0]) + abs(source_coords[1] - dest_coords[1])

def is_straight_line(a_coords, b_coords, c_coords):
    return (a_coords[1] - b_coords[1]) * (a_coords[0] - c_coords[0]) == (a_coords[1] - c_coords[1]) * (a_coords[0] - b_coords[0])
    
def is_double_away(source_coords, antennas):
    for antenna_coords in antennas.values():
        for outer_index, outer_coords in enumerate(antenna_coords):
            for inner_index, inner_coords in enumerate(antenna_coords):
                if outer_index == inner_index:
                    continue

                if is_straight_line(source_coords, outer_coords, inner_coords):
                    outer_distance = get_steps_to(source_coords, outer_coords)
                    inner_distance = get_steps_to(source_coords, inner_coords)
                    if outer_distance * 2 == inner_distance or inner_distance * 2 == outer_distance:   
                        return True
        
    return False

def build_grid(file_input):
    grid = []
    antenna = defaultdict(lambda: [])
    for row_index, row in enumerate(file_input):
        grid_row = []
        for column_index, node in enumerate(row):
            if node != "\n":
                grid_row += [node]

                if node != ".":
                    antenna[node] += [(row_index, column_index)]
        grid += [grid_row]

    return grid, antenna

def solve(file_location):
    file_input = None
    with open(file_location) as f:
        file_input = f.readlines()
        
    grid, antenna = build_grid(file_input)
    test_grid = copy.deepcopy(grid)

    unique = []
    for row_index, row in enumerate(grid):
        for column_index, _ in enumerate(row):
            if is_double_away((row_index, column_index),antenna):
                #print("found at ", (row_index, column_index))
                test_grid[row_index][column_index] = "#"
                unique += [(row_index, column_index)]
                
    return len(list(set(unique)))



print("Example Simple", solve("example_simple.txt"))
print("Example", solve("example.txt"))
print("Puzzle", solve("input.txt"))
