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

KNOWN_MAP = {}

def walk_value(value, depth=0, max_depth=6):
    depth += 1
    if depth > max_depth:
        return 1
    
    for func in RULES_TO_APPLY:
        result = func(value)
        if result is not None:
            total = 0
            for i in result:
                if (existing_solution := KNOWN_MAP.get(f"{i}-{depth}")) is not None:
                    total += existing_solution
                else:
                    cnt = walk_value(i, depth, max_depth)
                    KNOWN_MAP[f"{i}-{depth}"] = cnt
                    total += cnt
            return total

def solve(file_location):
    file_input = None
    with open(file_location) as f:
        file_input = f.readlines()
        
    values = [int(v) for v in file_input[0].split(" ")]
    total_count = 0
    for value in values:
        total_count += walk_value(value, max_depth=75)

    return total_count

print("Example", solve("example.txt"))
print("Puzzle", solve("input.txt"))
