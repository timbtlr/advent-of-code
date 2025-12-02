def solve(file_location):
    question_input = None
    with open(file_location) as f:
        question_input = f.readlines()

    invalid_ids = []
    groups = question_input[0].split(",")
    for group in groups:
        low, high = tuple(group.split("-"))
        for index in range(int(low), int(high) + 1):
            index = str(index)
            half = int(len(index) / 2)
            if index[:half] == index[half:]:
                print(index)
                invalid_ids += [int(index)]
    
    return sum(invalid_ids)


print("Example", solve("example.txt"))
print("Puzzle", solve("input.txt"))
