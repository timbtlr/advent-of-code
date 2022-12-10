def get_input(file_name: str):
    input = None
    with open(file_name) as f:
        input = f.readlines()
    input = [line.replace("\n", "") for line in input]
    for line in input:
        yield line


def read_line(line:str):
    line = line.split(" ")
    if len(line) == 1:
        return (line[0], None)
    else:
        return (line[0], int(line[1]))

def get_cycle_increment(action:str):
    cycle_increment = 1
    match action:
        case "addx":
            cycle_increment = 2
    return cycle_increment


def check_register(cycle, value):
    if (cycle % 40) + 20 == 40:
        return cycle * value
    return 0


def part_1():
    generator = get_input("src/2022/12-10/input.txt")
    line = next(generator)
    cycle = 0
    register_value = 1
    checked_sum = 0

    while True:
        action, value_change = read_line(line)
        cycle_increment = get_cycle_increment(action)

        for _ in range(0, cycle_increment):
            cycle += 1
            checked_sum += check_register(cycle, register_value)

        if value_change:
            register_value += value_change

        try:
            line = next(generator)
        except StopIteration:
            break
    return checked_sum



def row_changed(cycle, row_size):
    if (cycle % row_size) == 0:
        return True
    return False


def draw_pixel(cycle, register, row, row_size):
    #print("DRAWING", cycle, cycle % 40, register)
    for index in [register-1, register, register+1]:
        if cycle % row_size == index:
            try:
                row[index] = "#"
            except IndexError:
                pass
    return row

def part_2():
    generator = get_input("src/2022/12-10/input.txt")
    line = next(generator)
    cycle = 0
    register_value = 1
    rows = []
    row_size = 40
    current_row = ["."] * row_size

    while True:
        action, value_change = read_line(line)
        cycle_increment = get_cycle_increment(action)

        for _ in range(0, cycle_increment):
            current_row = draw_pixel(cycle, register_value, current_row, row_size)

            cycle += 1
            if row_changed(cycle, row_size):
                rows.append(current_row)
                current_row = ["."] * row_size

        if value_change:
            register_value += value_change

        try:
            line = next(generator)
        except StopIteration:
            break
    
    for row in rows:
        print("".join(row))


print(part_1(), part_2())
