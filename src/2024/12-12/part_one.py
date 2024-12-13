from collections import defaultdict

directions = [
    (-1, 0),
    (1, 0),
    (0, 1),
    (0, -1),
]

def build_grid(file_input):
    grid = []

    for _, row in enumerate(file_input):
        grid_row = []
        for _, node in enumerate(row):
            if node != "\n":
                grid_row += [node]

        grid += [grid_row]

    return grid

def find_groups(grid):
    groups = defaultdict(lambda: [])
    visited = []

    def check_node(grid, row_index, column_index, visited=[]):
        visited += [(row_index, column_index)]
        grouped = [(row_index, column_index)]
        node_value = grid[row_index][column_index]

        for i, j in directions:
            neighbor_x = row_index + i
            neighbor_y = column_index + j
            
            if neighbor_x < 0 or neighbor_y < 0:
                continue

            if (neighbor_x, neighbor_y) not in visited:
                try:
                    if grid[neighbor_x][neighbor_y] == node_value:
                        group, visited = check_node(grid, neighbor_x, neighbor_y)
                        grouped += group
                except IndexError:
                    continue
            
        return list(set(grouped)), visited

    for row_index, row in enumerate(grid):
        for column_index, node in enumerate(row):
            if (row_index, column_index) not in visited:
                group, visited = check_node(grid, row_index, column_index, visited)
                groups[node] += [group]

    return groups

def walk_group(grid, group):
    area = 0
    perimeter = 0
    
    for row_index, column_index in group:
        area += 1

        for i, j in directions:
            neighbor_x = row_index + i
            neighbor_y = column_index + j

            if neighbor_x < 0 or neighbor_y < 0:
                perimeter += 1
                continue

            try:
                if grid[neighbor_x][neighbor_y] != grid[row_index][column_index]:
                    perimeter += 1
            except IndexError:
                perimeter += 1

    return area, perimeter

def solve(file_location):
    file_input = None
    with open(file_location) as f:
        file_input = f.readlines()

    grid = build_grid(file_input)
    groups = find_groups(grid)
    
    total = 0
    for key, value in groups.items():
        for group in value:
            area, perimeter = walk_group(grid, group)
            total += area * perimeter


    return total
    
print("Small example", solve("example_small.txt"))
print("Island example", solve("example_island.txt"))
print("Example", solve("example.txt"))
print("Puzzle", solve("input.txt"))
