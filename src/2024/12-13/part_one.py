from collections import defaultdict

def parse_groups(file_input):
    groups = defaultdict(lambda: [])
    buttons = []
    for line in file_input:
        line = line.replace("\n", "")
        if "Button" in line:
            offsets = line.split(": ")[1].split(", ")
            buttons += [(int(offsets[0].split("X+")[1]), int(offsets[1].split("Y+")[1]))]
        elif "Prize" in line:
            locations = line.split(": ")[1].split(", ")
            groups[(int(locations[0].split("X=")[1]), int(locations[1].split("Y=")[1]))] = buttons
            buttons = []
    
    return groups

def find_prize(prize_location, button_offsets):
    coins = []
    prize_x, prize_y = prize_location
    a_x_offset, a_y_offset = button_offsets[0]
    b_x_offset, b_y_offset = button_offsets[1]
    
    for i in range(0, 1000):
        for j in range(0, 1000):
            if a_x_offset * i + b_x_offset * j == prize_x and a_y_offset * i + b_y_offset * j == prize_y:
                coins += [i * 3 + j]

    if coins:
        return min(coins)
    return None

def solve(file_location):
    file_input = None
    with open(file_location) as f:
        file_input = f.readlines()

    total = 0
    groups = parse_groups(file_input)
    for key, value in groups.items():
        total += find_prize(key, value) or 0

    return total
    
print("Example", solve("example.txt"))
print("Puzzle", solve("input.txt"))
