import itertools


def get_operations(value_len):
    raw_operations = list(itertools.product(["+", "*", "|"], repeat=value_len - 1))
    finalized_operations = []

    for operations in raw_operations:
        finalized_operations += [[op[0] for op in operations]]

    return finalized_operations

def can_solve(total, child_values):
    operations = get_operations(len(child_values))

    for operation in operations:
        print("starting new", total, child_values, operation)

        if len(child_values) == 1:
            if total == child_values[0]:
                return True, None
            
            return False, None

        current_value = child_values[0]
        for index, new_value in enumerate(child_values[1:]):
            if operation[index] == "|":
                current_value = int(f"{current_value}{new_value}")
            else:
                current_value = eval(f"{current_value} {operation[index]} {new_value}")

        if current_value == total:
            return True, operation
        
    return False, None


def solve(file_location):
    file_input = None
    with open(file_location) as f:
        file_input = f.readlines()
        
    values = []
    for line in file_input:
        parsed = line.split(":")
        values += [(int(parsed[0]), parsed[1].strip().split(" "))]

    working_totals = []
    for total, child_values in values:
        does_match, _ = can_solve(total, child_values)
        if does_match:
            working_totals += [total]

    return sum(working_totals)



print("Example", solve("example.txt"))
print("Puzzle", solve("input.txt"))
