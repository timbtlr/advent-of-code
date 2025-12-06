directions = [
    (-1, -1),
    (-1, 0),
    (-1, 1),
    (0, -1),
    (0, 1),
    (1, -1),
    (1, 0),
    (1, 1)
]

def solve(file_location):
    question_input = None
    with open(file_location) as f:
        question_input = f.readlines()

    grid = []
    for line in question_input:
        grid += [list(line.strip("\n"))]

    total = 0
    for row_index, row in enumerate(grid):
        for col_index, node in enumerate(row):
            if node != "@":
                continue
            
            adjacent = []
            for row_offset, col_offset in directions:
                if row_index + row_offset < 0 or col_index + col_offset < 0:
                    continue

                if row_index + row_offset > len(row)-1 or col_index + col_offset > len(grid)-1:
                    continue

                adjacent += [grid[row_index + row_offset][col_index + col_offset]]

            if len([adj for adj in adjacent if adj == "@"]) < 4:
                total += 1
    
    return total


print("Example", solve("example.txt"))
print("Puzzle", solve("input.txt"))
