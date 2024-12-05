from collections import defaultdict

def solve(file_location):
    input = None
    with open(file_location) as f:
        input = f.readlines()

    ordering = defaultdict(lambda: [])
    manuals = []

    for line in input:
        if "|" in line:
            key, value = line.split("|")
            ordering[int(key.strip("\n"))] += [int(value.strip("\n"))]

        elif "," in line:
            manuals += [[int(i.strip("\n")) for i in line.split(",")]]

    correctly_ordered = []

    for manual in manuals:
        is_correct = True

        for page_index, page_number in enumerate(manual):
            page_order = ordering.get(page_number)
            if page_order is None:
                continue

            if page_index == 0:
                continue

            for check_index in range(0, page_index):
                if manual[check_index] in page_order:
                    is_correct = False

            if not is_correct:
                break

        if is_correct:
            correctly_ordered += [manual]
    
    return sum([i[int((len(i) - 1)/2)] for i in correctly_ordered])

print("Example", solve("example.txt"))
print("Puzzle", solve("input.txt"))
