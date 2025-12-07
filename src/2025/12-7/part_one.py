def solve(file_location):
    question_input = None
    with open(file_location) as f:
        question_input = f.readlines()

    grid = []
    beams = []
    for line in question_input:
        grid += [list(line.strip("\n"))]
        if "S" in line:
            beams += [line.find("S")]
    
    total_splits = 0
    for row in grid[1:]:
        new_beams = []
        for beam_index in beams:
            if row[beam_index] == "^":
                total_splits += 1
                if beam_index - 1 > 0:
                    row[beam_index - 1] = "|"
                    new_beams += [beam_index - 1]

                if beam_index + 1 < len(row):
                    row[beam_index + 1] = "|"
                    new_beams += [beam_index + 1]
            else:
                new_beams += [beam_index]
                row[beam_index ] = "|"

        beams = list(set(new_beams))

    return total_splits


print("Example", solve("example.txt"))

print("Puzzle", solve("input.txt"))
