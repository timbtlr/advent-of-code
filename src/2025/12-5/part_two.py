def solve(file_location):
    question_input = None
    with open(file_location) as f:
        question_input = f.readlines()

    fresh_ranges = []
    for line in question_input:
        line = line.strip()
        if line == "":
            continue

        if "-" in line:
            start, end = tuple(line.split("-"))
            start = int(start)
            end = int(end)
        
            #print(start, end)
            if fresh_ranges:
                while True:
                    found = False
                    for index, range in enumerate(fresh_ranges):
                        range_start, range_end = range
                        if ((start >= range_start and start <= range_end or end >= range_start and end <= range_end) or 
                           (range_start >= start and range_start <= end or range_end >= start and range_end <= end)):
                            fresh_ranges.pop(index)
                            start = min(start, range_start)
                            end = max(end, range_end)
                            found = True
                            break

                    if not found:
                        break
                
                fresh_ranges += [(start, end)]
            else:
                fresh_ranges += [(start, end)]

    total = 0
    for start, end in fresh_ranges:
        total += end +- start + 1

    return total


print("Example", solve("example.txt"))
print("Puzzle", solve("input.txt"))
