import re


SET_DATA_PATTERN = "(Game )(\d*): (.*)"
TURN_DATA_PATTERN = "(\d*) (\w*)"

CONFIGURATION = {"red": 12, "green": 13, "blue": 14}

with open("day-02.txt", "r") as f:
    game_results = f.readlines()

# Part 1

sum_possible_game_ids = 0
for game in game_results:
    game_possible = True
    parsed_game_data = re.match(SET_DATA_PATTERN, game)
    game_id = int(parsed_game_data.group(2))
    set_data = parsed_game_data.group(3)
    set_list = set_data.split(";")
    for _set in set_list:
        for turn in _set.split(","):
            data = re.match(TURN_DATA_PATTERN, turn.strip())
            color = data.group(2)
            count = int(data.group(1))
            if color in CONFIGURATION.keys() and count > CONFIGURATION[color]:
                game_possible = False

    if game_possible:
        sum_possible_game_ids += game_id

print(sum_possible_game_ids)

# Part 2

sum_powers = 0
for game in game_results:
    red_values = []
    green_values = []
    blue_values = []
    parsed_game_data = re.match(SET_DATA_PATTERN, game)
    set_data = parsed_game_data.group(3)
    set_list = set_data.split(";")
    for _set in set_list:
        for turn in _set.split(","):
            data = re.match(TURN_DATA_PATTERN, turn.strip())
            color = data.group(2)
            count = int(data.group(1))
            if color == "red":
                red_values.append(count)
            elif color == "green":
                green_values.append(count)
            elif color == "blue":
                blue_values.append(count)

    sum_powers += max(red_values) * max(green_values) * max(blue_values)

print(sum_powers)
