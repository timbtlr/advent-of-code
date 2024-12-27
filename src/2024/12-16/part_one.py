from heapq import heappush, heappop

DIRECTIONS = [
    (-1, 0, "^"),
    (1, 0, "V"),
    (0, -1, "<"),
    (0, 1, ">"),
]
TURN_COST = {
    "^": {
        "^": 0,
        "V": 2000,
        ">": 1000,
        "<": 1000,
    },
    "V": {
        "^": 2000,
        "V": 0,
        ">": 1000,
        "<": 1000,
    },
    ">": {
        "^": 1000,
        "V": 1000,
        ">": 0,
        "<": 2000,
    },
    "<": {
        "^": 1000,
        "V": 1000,
        ">": 2000,
        "<": 0,
    }
}
DIRECTION_OPPOSITES = {
    "^": "V",
    "V": "^",
    ">": "<", 
    "<": ">"
}

global index 
index = 0

def parse_input(file_input):
    starting_location = None
    ending_location = None
    
    grid = []
    starting_location = None
    for row_index, line in enumerate(file_input):
        line = line.replace("\n", "")
        row = []
        for col_index, char in enumerate(line):
            row += [char]
            if char == "S":
                starting_location = (row_index, col_index)
            elif char == "E":
                ending_location = (row_index, col_index)
        grid += [row]

    return grid, starting_location, ending_location

def print_grid(grid, visited):
    visited = [(x, y) for _,x,y in visited]
    for ri, r in enumerate(grid):
        s = ""
        for ci, i in enumerate(r):
            if ((ri, ci)) in visited:
                s += "*"
            elif i == ".":
                s += " "
            else:   
                s += str(i)
        print(s)

def walk_path(grid, start_row, start_col):
    stack = []
    heappush(stack, (0, start_row, start_col, ">"))
    visited = set()
    final_scores = []
    
    while stack:
        score, row, col, direction = heappop(stack)
        visited.add((direction, row, col))

        if grid[row][col] == "E":
            final_scores += [score]
            continue

        else:
            for row_offset, col_offset, new_direction in DIRECTIONS:
                turn_score = TURN_COST[direction][new_direction]
                new_score = score + turn_score + 1

                new_row = row + row_offset
                new_col = col + col_offset

                if new_direction == DIRECTION_OPPOSITES[direction]:
                    continue
                
                if (new_direction, new_row, new_col) in visited:
                    continue

                if grid[new_row][new_col] != "#":
                    heappush(stack, (new_score, new_row, new_col, new_direction))
        
    return min(final_scores)









def solve(file_location):
    file_input = None
    with open(file_location) as f:
        file_input = f.readlines()

    grid, starting_location, ending_location = parse_input(file_input)
    print_grid(grid, [])
    
    return walk_path(grid, starting_location[0], starting_location[1])
    

print("Simple Example", solve("example_simple.txt"))
print("Example", solve("example.txt"))
print("Puzzle", solve("input.txt"))