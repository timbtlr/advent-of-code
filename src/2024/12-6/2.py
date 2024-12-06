from copy import deepcopy

MOVEMENT_OFFSETS = {
    "^": (-1, 0),
    ">": (0, 1),
    "V": (1, 0),
    "<": (0, -1)
}

TURN_ORDER = {
    "^": ">",
    ">": "V",
    "V": "<",
    "<": "^"
}

def build_grid(file_input):
    grid = []
    guard_location = None
    for row_index, row in enumerate(file_input):
        grid_row = []
        for column_index, node in enumerate(row):
            if node != "\n":
                grid_row += [node]
                if node == "^":
                    guard_location = (row_index, column_index)
        grid += [grid_row]

    return grid, guard_location

def is_subsequence(a, b):
    seq = iter(b)
    return all(i in seq for i in a)

def walk_grid(grid, guard_location):
    visited = [guard_location]
    looping = False

    while True:
        if len(visited) > 10:
            if is_subsequence(visited[-10:], visited[:-10]):
                looping = True
                break

        guard_row, guard_col = guard_location
        if guard_row < 0 or guard_col < 0:
            break

        try:
            guard_node = grid[guard_row][guard_col]
        except IndexError:
            break

        row_offset, col_offset = MOVEMENT_OFFSETS[guard_node]
        next_row = guard_row + row_offset
        next_col = guard_col + col_offset
        next_node = None

        try:
            next_node = grid[next_row][next_col]
            if next_node is not None and next_node == "#":
                grid[guard_row][guard_col] = TURN_ORDER[guard_node]
            else:
                visited += [(next_row, next_col)]
                guard_location = (next_row, next_col)
                grid[next_row][next_col] = guard_node
                grid[guard_row][guard_col] = "."
        except IndexError:
            break

    return visited, looping


def solve(file_location):
    file_input = None
    with open(file_location) as f:
        file_input = f.readlines()

    grid, guard_location = build_grid(file_input)
    visited, _ = walk_grid(deepcopy(grid), guard_location)   

    looping = []
    for row_index, col_index in list(set(visited)):
        if (row_index, col_index) != guard_location:
            if grid[row_index][col_index] == ".":
                test_grid = deepcopy(grid)
                test_grid[row_index][col_index] = "#"
                _, has_loop = walk_grid(test_grid, guard_location)
                if has_loop:
                    looping += [(row_index, col_index)]

    return len(looping)

print("Example", solve("example.txt"))
print("Puzzle", solve("input.txt"))
