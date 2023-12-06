def solve(file_location):
    humidity_to_location_map = {"ranges": []}
    temp_to_humidity_map = {"ranges": []}
    light_to_temp_map = {"ranges": []}
    water_to_light_map = {"ranges": []}
    fertilizer_to_water_map = {"ranges": []}
    soil_to_fertilizer_map = {"ranges": []}
    seed_to_soil_map = {"ranges": []}
    section_title_map = {
        "seed-to-soil map": seed_to_soil_map,
        "soil-to-fertilizer map": soil_to_fertilizer_map,
        "fertilizer-to-water map": fertilizer_to_water_map,
        "water-to-light map": water_to_light_map,
        "light-to-temperature map": light_to_temp_map,
        "temperature-to-humidity map": temp_to_humidity_map,
        "humidity-to-location map": humidity_to_location_map,
    }

    puzzle_input = None
    with open(file_location) as f:
        puzzle_input = f.readlines()

    def parse_mapping_line(line, map):
        dest_start, source_start, map_length = (int(i) for i in line.split(" "))
        map["ranges"] += [(source_start, source_start + map_length, dest_start)]

    def link_maps():
        seed_to_soil_map.update({"next": soil_to_fertilizer_map})
        soil_to_fertilizer_map.update({"next": fertilizer_to_water_map})
        fertilizer_to_water_map.update({"next": water_to_light_map})
        water_to_light_map.update({"next": light_to_temp_map})
        light_to_temp_map.update({"next": temp_to_humidity_map})
        temp_to_humidity_map.update({"next": humidity_to_location_map})
        humidity_to_location_map.update({"next": None})

    seeds = []
    current_mapping = None
    for index, line in enumerate(puzzle_input):
        if index == 0:
            seeds = [int(i) for i in line.replace("\n", "").split(": ")[1].split(" ")]
            continue

        if line.strip() == "":
            continue

        if "map" in line:
            map_title = line.split(":")[0]
            current_mapping = section_title_map[map_title]
            continue

        parse_mapping_line(line, current_mapping)

    link_maps()

    locations = []
    for seed in seeds:
        print(f"checking seed {seed}")
        value = seed
        next_map = seed_to_soil_map
        while next_map is not None:
            for range_entry in next_map["ranges"]:
                source_start, source_end, dest_start = range_entry
                if source_start <= value <= source_end:
                    value = dest_start + value - source_start
                    break
            next_map = next_map["next"]
        locations += [value]

    return locations, min(locations)


print("Example", solve("example.txt"))
print("Puzzle", solve("input.txt"))
