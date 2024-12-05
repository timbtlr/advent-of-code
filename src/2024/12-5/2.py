from collections import defaultdict

def is_in_order(manual_list, ordering_dict):
    for page_index, page_number in enumerate(manual_list):
        page_order = ordering_dict.get(page_number)
        if page_order is None:
            continue

        if page_index == 0:
            continue

        for check_index in range(0, page_index):
            if manual_list[check_index] in page_order:
                return False
            
    return True

def order_manual(manual_list, ordering_dict):
    while not is_in_order(manual_list, ordering_dict):
        for page_index, page_number in enumerate(manual_list):
            page_order = ordering_dict.get(page_number)

            if page_order is None:
                continue

            if page_index == 0:
                continue

            for check_index in range(0, page_index):
                if manual_list[check_index] in page_order:
                    manual_list.insert(check_index, manual_list.pop(page_index))

    return manual_list

def solve(file_location):
    file_input = None
    with open(file_location) as f:
        file_input = f.readlines()

    ordering = defaultdict(lambda: [])
    manuals = []

    for line in file_input:
        if "|" in line:
            key, value = line.split("|")
            ordering[int(key.strip("\n"))] += [int(value.strip("\n"))]

        elif "," in line:
            manuals += [[int(i.strip("\n")) for i in line.split(",")]]

    incorrectly_ordered = []
    for manual in manuals:
        if not is_in_order(manual, ordering):
            incorrectly_ordered += [order_manual(manual, ordering)]
    
    return sum([i[int((len(i) - 1)/2)] for i in incorrectly_ordered])

print("Example", solve("example.txt"))
print("Puzzle", solve("input.txt"))