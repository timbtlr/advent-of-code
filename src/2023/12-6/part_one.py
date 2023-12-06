def solve(file_location):
    puzzle_input = None
    with open(file_location) as f:
        puzzle_input = f.readlines()

    time = int(
        "".join(
            [
                i
                for i in puzzle_input[0].replace("\n", "").split("Time:")[1].split(" ")
                if i != ""
            ]
        )
    )
    distance = int(
        "".join(
            [
                i
                for i in puzzle_input[1]
                .replace("\n", "")
                .split("Distance:")[1]
                .split(" ")
                if i != ""
            ]
        )
    )

    ways_to_win = 0
    for i in range(time):
        if i * (time - i) > distance:
            ways_to_win += 1
    return ways_to_win


print("Example", solve("example.txt"))
print("Puzzle", solve("input.txt"))
