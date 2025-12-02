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
            for i in range(0, len(index)):
                replaced = index.replace(index[0:i], "")
                if replaced == "":
                    invalid_ids += [int(index)]
                    break

    return sum(invalid_ids)


print("Example", solve("example.txt"))
print("Puzzle", solve("input.txt"))
