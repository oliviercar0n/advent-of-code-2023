import re


CONFIGURATION = (12, 13, 14)

with open("puzzle_input.txt", "r") as f:
    game_results = f.readlines()

set_data_pattern = "(Game )(\d*): (.*)"
color_pattern = "(\d*) (\w*)"

sum_possible_game_ids = 0
for game in game_results:
    game_possible = True
    parsed_game_data = re.match(set_data_pattern, game)
    game_id = int(parsed_game_data.group(2))
    set_data = parsed_game_data.group(3)
    set_list = set_data.split(";")
    for _set in set_list:
        for turn in _set.split(","):
            data = re.match(color_pattern, turn.strip())
            color = data.group(2)
            if color == "red":
                if int(data.group(1)) > CONFIGURATION[0]:
                    game_possible = False
            elif color == "green":
                if int(data.group(1)) > CONFIGURATION[1]:
                    game_possible = False
            elif color == "blue":
                if int(data.group(1)) > CONFIGURATION[2]:
                    game_possible = False
    
    if game_possible:
        sum_possible_game_ids += game_id

print(f"The sum of all possible game IDs is {sum_possible_game_ids}")
