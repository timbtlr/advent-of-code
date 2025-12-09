import math

def solve(file_location, pairs_to_find=10):
    question_input = None
    with open(file_location) as f:
        question_input = f.readlines()

    circuits = []
    for line in question_input:
        x, y, z = tuple(line.strip("\n").split(","))
        circuits += [[(int(x), int(y), int(z))]]

    distances = {}
    for i in range(len(circuits)):
        for j in range(len(circuits)):
            if i == j:
                continue

            ic = circuits[i][0]
            jc = circuits[j][0]
            
            if f"{ic[0]},{ic[1]},{ic[2]} to {jc[0]},{jc[1]},{jc[2]}" not in distances.keys() and f"{jc[0]},{jc[1]},{jc[2]} to {ic[0]},{ic[1]},{ic[2]}" not in distances.keys():
                key = f"{ic[0]},{ic[1]},{ic[2]} to {jc[0]},{jc[1]},{jc[2]}"
                distances[key] = math.sqrt(
                    math.pow(ic[0]-jc[0], 2) + 
                    math.pow(ic[1]-jc[1], 2) + 
                    math.pow(ic[2]-jc[2], 2)
                )

    sorted_distances = {k: v for k, v in sorted(distances.items(), key=lambda item: item[1])}
    circuits_checked = 0
    for key, value in sorted_distances.items():
        ic = tuple(int(i) for i in key.split(" to ")[0].split(","))
        jc = tuple(int(i) for i in key.split(" to ")[1].split(","))

        if [ic] in circuits and [jc] in circuits:
            circuits.remove([jc])
            circuits[circuits.index([ic])] += [jc]

        elif [ic] in circuits:
            for index, circuit in enumerate(circuits):
                if jc in circuit:
                    print(index)
                    circuits += [circuits.pop(index) + [ic]]
                    circuits.remove([ic])
                    break
        
        elif [jc] in circuits:
            for index, circuit in enumerate(circuits):
                if ic in circuit:
                    circuits += [circuits.pop(index) + [jc]]
                    circuits.remove([jc])
                    break

        else:
            i_index = None
            for index, circuit in enumerate(circuits):
                if ic in circuit:
                    i_index = index
                    break

            j_index = None
            for index, circuit in enumerate(circuits):
                if jc in circuit:
                    j_index = index
                    break

            if i_index != j_index:
                if i_index > j_index:
                    circuits += [circuits.pop(i_index) + circuits.pop(j_index)]
                else:
                    circuits += [circuits.pop(j_index) + circuits.pop(i_index)]

        circuits_checked += 1
        if circuits_checked >= pairs_to_find:
            break

    circuits = sorted(circuits, key=lambda x: len(x), reverse=True)
    return math.prod([len(x) for x in circuits[:3]])


print("Example", solve("example.txt", pairs_to_find=10))

print("Puzzle", solve("input.txt", pairs_to_find=1000))
