def solve(file_location):
    question_input = None
    with open(file_location) as f:
        question_input = f.readlines()

    for line in question_input:
        pass
    
    return


print("Example", solve("example.txt"))
print("Puzzle", solve("input.txt"))
