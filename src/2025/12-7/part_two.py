def solve(file_location):
    question_input = None
    with open(file_location) as f:
        question_input = f.readlines()

    grid = []
    for line in question_input:
        grid += [list(line.strip("\n"))]

    beams = [1 if i == "S" else 0 for i in grid[0]]
        
    for row in grid[1:]:
        new_beams = [0 for _ in range(len(beams))]
        for row_index, beam_value in enumerate(beams):
            if beam_value > 0:
                if row[row_index] == "^":
                    if row_index - 1 > 0:
                        new_beams[row_index - 1] += beam_value

                    if row_index + 1 < len(row):
                        new_beams[row_index + 1] += beam_value

                else:
                    new_beams[row_index] += beam_value

        beams = new_beams

    return sum(beams) + 1


print("Example", solve("example.txt"))
print("Puzzle", solve("input.txt"))
