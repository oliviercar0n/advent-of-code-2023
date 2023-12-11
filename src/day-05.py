import re


with open("day-05.txt", "r") as f:
    input_data = f.readlines()

# Part 1

seeds_list = [
    int(seed_number)
    for seed_number in re.match("seeds: (.*)", input_data[0]).group(1).split(" ")
]

master_map = {}

current_source = ""
current_destination = ""
for line in input_data[2:]:
    if "map" in line:
        parsed = re.match("(\w*)-to-(\w*) map", line)
        current_source = parsed.group(1)
        current_destination = parsed.group(2)
        master_map[current_source] = []
    elif len(line) > 1:
        master_map[current_source].append(
            [int(value) for value in line[:-1].split(" ")]
        )


def convert_source_to_destination(source_value, map):
    for line in map:
        if source_value in range(line[1], line[1] + line[2]):
            return source_value + (line[0] - line[1])

    return source_value


locations = []
for seed in seeds_list:
    soil = convert_source_to_destination(seed, master_map["seed"])
    fertilizer = convert_source_to_destination(soil, master_map["soil"])
    water = convert_source_to_destination(fertilizer, master_map["fertilizer"])
    light = convert_source_to_destination(water, master_map["water"])
    temperature = convert_source_to_destination(light, master_map["light"])
    humidity = convert_source_to_destination(temperature, master_map["temperature"])
    location = convert_source_to_destination(humidity, master_map["humidity"])
    locations.append(location)

print(f"The lowest location is {min(locations)}")
