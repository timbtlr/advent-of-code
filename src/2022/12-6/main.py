def get_input(file_name: str):
    input = None
    with open(file_name) as f:
        input = f.readlines()
    input = [line.replace("\n", "") for line in input]
    return input


def get_unique_message(line: str, length: int):
    characters = list(line[:length])
    for index, value in enumerate(line[length:]):
        characters.pop(0)
        characters.append(value)
        if len(set(characters)) == length:
            return index + length + 1


def part_1():
    input = get_input("src/2022/12-6/input.txt")
    indicies = []
    for line in input:
        indicies.append(get_unique_message(line=line, length=4))
    return indicies


def part_2():
    input = get_input("src/2022/12-6/input.txt")
    indicies = []
    for line in input:
        indicies.append(get_unique_message(line=line, length=14))
    return indicies


print(part_1(), part_2())
