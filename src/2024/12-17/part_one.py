from math import pow

def get_operand_value(registers, operand):
    if operand >= 0 and operand <= 3:
        return operand
    
    MAPPING = {
        4: "A",
        5: "B", 
        6: "C"
    }
    return registers[MAPPING[operand]]

def adv(registers, operand):
    operand = get_operand_value(registers, operand)
    registers["A"] = int(registers["A"] / int(pow(2, operand)))
    return registers, None, None

def bxl(registers, operand):
    registers["B"] = int(registers["B"] ^ operand)
    return registers, None, None

def bst(registers, operand):
    operand = get_operand_value(registers, operand)
    registers["B"] = int(operand % 8)
    return registers, None, None

def jnz(registers, operand):
    if registers["A"] == 0:
        return registers, None, None
    
    return registers, operand, None

def bxc(registers, operand):
    registers["B"] = int(registers["B"] ^ registers["C"])
    return registers, None, None

def out(registers, operand):
    operand = get_operand_value(registers, operand)
    return registers, None, int(operand % 8)

def bdv(registers, operand):
    operand = get_operand_value(registers, operand)
    registers["B"] = int(registers["A"] / int(pow(2, operand)))
    return registers, None, None

def cdv(registers, operand):
    operand = get_operand_value(registers, operand)
    registers["C"] = int(registers["A"] / int(pow(2, operand)))
    return registers, None, None

OPERATIONS = {
    0: adv,
    1: bxl,
    2: bst,
    3: jnz,
    4: bxc,
    5: out,
    6: bdv,
    7: cdv
}

def parse_input(file_input):
    registers = {}
    program = []
    for line in file_input:
        line = line.replace("\n", "").strip()
        if not line:
            continue

        values = line.split(": ")[1]
        if "A:" in line:
            registers["A"] = int(values)
        elif "B:" in line:
            registers["B"] = int(values)
        elif "C:" in line:
            registers["C"] = int(values)
        elif "Program" in line:
            program = [int(i) for i in values.split(",")]

    return registers, program


def solve(file_location):
    file_input = None
    with open(file_location) as f:
        file_input = f.readlines()

    registers, program = parse_input(file_input)
    print(registers)
    print(program)

    index = 0
    all_output = []
    while index < len(program)-1:
        op = program[index]
        operand = program[index + 1]

        registers, jump_to, output = OPERATIONS[op](registers, operand)
        if output is not None:
            print("OUTPUT", output)
            all_output += [str(output)]

        if jump_to is not None:
            index = jump_to
        else:
            index += 2

    return ",".join(all_output)
    

print("Example", solve("example.txt"))
print("Puzzle", solve("input.txt"))