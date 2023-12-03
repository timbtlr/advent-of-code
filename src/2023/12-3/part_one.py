def parse_to_matrix(puzzle_input):
    matrix = []
    for line in puzzle_input:
        matrix += [list(line.replace("\n", ""))]
    return matrix


def has_symbols_in_coords(matrix, coords):
    coords = list(set(coords))
    matched = []
    for i, j in coords:
        try:
            if i < 0 or j < 0:
                continue

            value = matrix[i][j]
            if not value.isdigit() and value != ".":
                matched += [(value, (i, j))]
        except IndexError:
            continue

    return matched


def calculate_coordinates_to_check(row, col):
    coords = []
    for row_mod in [-1, 0, 1]:
        for col_mod in [-1, 0, 1]:
            coords += [(row + row_mod, col + col_mod)]
    return coords


def solve(file_location):
    puzzle_input = None
    with open(file_location) as f:
        puzzle_input = f.readlines()

    matrix = parse_to_matrix(puzzle_input)

    number_list = []
    for row_index in range(len(matrix)):
        current_number = ""
        check_coords = []
        for column_index in range(len(matrix[row_index])):
            node_value = matrix[row_index][column_index]
            if node_value.isdigit():
                current_number += node_value
                check_coords += calculate_coordinates_to_check(row_index, column_index)
                continue

            if current_number != "":
                number_list += [(int(current_number), check_coords)]
                current_number = ""
                check_coords = []

        if current_number != "":
            number_list += [(int(current_number), check_coords)]

    all_numbers = []
    for number, coordinates_to_check in number_list:
        found_symbols = has_symbols_in_coords(matrix, coordinates_to_check)
        if found_symbols:
            all_numbers += [number]

    return sum(all_numbers)


print("Example", solve("example.txt"))
print("Puzzle", solve("input.txt"))
