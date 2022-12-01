def get_input(file_name):
    input = None
    with open(file_name) as f:
        input = f.readlines()

    for line in input:
        yield line.replace("\n", "")


def calories_list():
    calorie_list = []
    pouch_total = 0
    for line in get_input("src/2022/12-1/input.txt"):
        if line == "":
            calorie_list += [pouch_total]
            pouch_total = 0
        else:
            pouch_total += int(line)
    calorie_list += [pouch_total]
    return calorie_list


def part_1():
    return max(calories_list())


def part_2():
    return sum(sorted(calories_list())[-3:])


print(part_1(), part_2())
