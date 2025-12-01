
from heapq import heappush, heappop
from copy import copy
from collections import deque

def print_grid(grid, visited):
    for ri, r in enumerate(grid):
        s = ""
        for ci, i in enumerate(r):
            if ((ri, ci)) in visited:
                s += "*"
            elif i == ".":
                s += "."
            else:   
                s += str(i)
        print(s)

DIRECTIONS = [
    (-1, 0),
    (1, 0),
    (0, -1),
    (0, 1),
]

def walk_path(grid):
    stack = deque([(0, 0, 0)])
    visited = set()
    
    while stack:
        score, row, col = stack.popleft()

        if row == col == len(grid) - 1:
            return score

        else:
            for row_offset, col_offset in DIRECTIONS:
                new_row = row + row_offset
                new_col = col + col_offset

                if (
                    (new_row, new_col) not in visited and
                    new_row in range(len(grid)) and
                    new_col in range(len(grid)) and 
                    grid[new_row][new_col] == "."
                ):
                    stack.append((score + 1, new_row, new_col))
                    visited.add((new_row, new_col))
    
    return None

def solve(file_location, grid_size=71, stop_index=1024):
    file_input = None
    with open(file_location) as f:
        file_input = f.readlines()

    grid = [["." for _ in range(grid_size)] for _ in range(grid_size)]
    for index, line in enumerate(file_input):
        if index == stop_index:
            break

        col, row = tuple(line.replace("\n", "").split(","))
        grid[int(row)][int(col)] = "X"


    print_grid(grid, [])
    
    return walk_path(grid)
    

print("Example", solve("example.txt", grid_size=7, stop_index=12))
print("Puzzle", solve("input.txt", grid_size=71, stop_index=1024))