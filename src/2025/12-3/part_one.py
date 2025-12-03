from collections import defaultdict

def solve(file_location):
    question_input = None
    with open(file_location) as f:
        question_input = f.readlines()

    values = []

    for line in question_input:
        line_map = defaultdict(list)
        for index, character in enumerate(line.strip("\n")):
            line_map[character] += [index]

        found = False
        keys = sorted(line_map.keys(), reverse=True)
        for index, key in enumerate(keys):
            #input()
            if found:
                break 

            min_index = min(line_map[key])
            for next_key in keys:
                if any([n > min_index for n in line_map[next_key]]):
                    found = True
                    values += [int(f"{key}{next_key}")]
                    break

    
    return sum(values)


print("Example", solve("example.txt"))
print("Puzzle", solve("input.txt"))
