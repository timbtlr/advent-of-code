def solve(file_location):
    question_input = None
    with open(file_location) as f:
        question_input = f.readlines()

    fresh_ranges = []
    confirmed_fresh = []
    for line in question_input:
        line = line.strip()
        if line == "":
            continue

        if "-" in line:
            start, end = tuple(line.split("-"))
            fresh_ranges += [(int(start), int(end))]
        
        else:
            line = int(line)
            for start, end in fresh_ranges:
                if line >= start and line <= end:
                    confirmed_fresh += [line]
                    break
        
    return len(confirmed_fresh)


print("Example", solve("example.txt"))
print("Puzzle", solve("input.txt"))
