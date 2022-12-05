def get_input(file_name: str):
    input = None
    with open(file_name) as f:
        input = f.readlines()
    input = [line.replace("\n", "") for line in input]
    return input


def get_stacks(input: str):
    stacks = None
    for line in input:
        if "[" not in line and "]" not in line:
            break

        groups = [line[i : i + 3].strip().replace("[", "").replace("]", "") for i in range(0, len(line), 4)]
        if not stacks:
            stacks = []
            for _ in range(0, len(groups)):
                stacks.append([])
        for index, value in enumerate(groups):
            if value != "":
                stacks[index].append(value)

    return stacks


def build_output(stacks):
    output = ""
    for stack in stacks:
        try:
            output += stack[0]
        except:
            pass
    return output


def part_1():
    input = get_input("src/2022/12-5/input.txt")
    stacks = get_stacks(input)
    for line in input:
        if "move" not in line:
            continue

        split_line = line.split(" ")
        amount = int(split_line[1])
        source = int(split_line[3]) - 1
        destination = int(split_line[5]) - 1

        for _ in range(0, amount):
            stacks[destination].insert(0, stacks[source].pop(0))

    return build_output(stacks)


def part_2():
    input = get_input("src/2022/12-5/input.txt")
    stacks = get_stacks(input)

    for line in input:
        if "move" not in line:
            continue

        split_line = line.split(" ")
        amount = int(split_line[1])
        source = int(split_line[3]) - 1
        destination = int(split_line[5]) - 1

        stacks[destination] = stacks[source][:amount] + stacks[destination]
        stacks[source] = stacks[source][amount:]

    return build_output(stacks)


print(part_1(), part_2())
