def transform_zero(value):
    if value == 0:
        return [1]
    
    return None

def split_even(value):
    value_list = list(str(value))
    if len(value_list) % 2 == 0:
        return [
            int("".join(value_list[:int(len(value_list) / 2)])), 
            int("".join(value_list[int(len(value_list) / 2):]))
        ]
    return None

def default_transform(value):
    return [value * 2024]

RULES_TO_APPLY = [
    transform_zero,
    split_even,
    default_transform
]

def solve(file_location):
    file_input = None
    with open(file_location) as f:
        file_input = f.readlines()
        
    values = [int(v) for v in file_input[0].split(" ")]
    for _ in range(25):
        new_list = []
        for value in values:
            for func in RULES_TO_APPLY:
                result = func(value)
                if result is not None:
                    new_list.extend(result)
                    break
        values = new_list

    return len(values)

print("Example", solve("example.txt"))
print("Puzzle", solve("input.txt"))
