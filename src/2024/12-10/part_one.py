directions = [
    (-1, 0),
    (1, 0),
    (0, 1),
    (0, -1),
]

def dfs(grid, node, visited, peaks):
    visited += [node]
    x = node[0]
    y = node[1]
    #input()
    if grid[x][y] == 9:
        if (node[0], node[1]) not in peaks:
            peaks += [(node[0], node[1])]
        return peaks

    for i, j in directions:
        neighbor_x = x + i
        neighbor_y = y + j

        if neighbor_x < 0 or neighbor_y < 0:
            continue

        if (neighbor_x, neighbor_y) in visited:
            continue

        try:
            if grid[neighbor_x][neighbor_y] != "." and grid[neighbor_x][neighbor_y] == grid[x][y] + 1:
                peaks = dfs(grid, (neighbor_x, neighbor_y), visited, peaks)
        except IndexError:
            pass

    return peaks


def build_grid(file_input):
    grid = []
    trail_heads = []
    for row_index, row in enumerate(file_input):
        grid_row = []
        for column_index, node in enumerate(row):
            if node != "\n":
                if node == ".":
                    grid_row += [node]
                else:
                    grid_row += [int(node)]

                if node == "0":
                    trail_heads += [(row_index, column_index)]
        grid += [grid_row]

    return grid, trail_heads

def solve(file_location):
    file_input = None
    with open(file_location) as f:
        file_input = f.readlines()
        
    grid, trail_heads = build_grid(file_input)
        
    total_peaks = 0
    for head in trail_heads:
        peaks = dfs(grid, (head[0], head[1]), [], [])
        total_peaks += len(list(set(peaks)))
    
    return total_peaks

#print("Small Example", solve("example_small.txt"))
#print("Medium Example", solve("example_medium.txt"))
print("Example", solve("example.txt"))
print("Puzzle", solve("input.txt"))
