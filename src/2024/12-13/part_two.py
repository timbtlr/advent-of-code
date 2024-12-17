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
            groups[(
                int(locations[0].split("X=")[1]) + 10000000000000, 
                int(locations[1].split("Y=")[1]) + 10000000000000
            )] = buttons
            buttons = []
    
    return groups

def find_prize(prize_location, button_offsets):
    prize_x, prize_y = prize_location
    a_x_offset, a_y_offset = button_offsets[0]
    b_x_offset, b_y_offset = button_offsets[1]

    a_presses = int((prize_x * b_y_offset - prize_y * b_x_offset) / (a_x_offset * b_y_offset - a_y_offset * b_x_offset))
    b_presses = int((a_x_offset * prize_y - a_y_offset * prize_x) / (a_x_offset * b_y_offset - a_y_offset * b_x_offset))

    if a_x_offset * a_presses + b_x_offset * b_presses == prize_x and a_y_offset * a_presses + b_y_offset * b_presses == prize_y:
        return (a_presses*3) + b_presses

    return None



def solve(file_location):
    file_input = None
    with open(file_location) as f:
        file_input = f.readlines()

    total = 0
    groups = parse_groups(file_input)
    for key, value in groups.items():
        coins = find_prize(key, value)
        total += coins or 0

    return total
    
print("Example", solve("example.txt"))
print("Puzzle", solve("input.txt"))
