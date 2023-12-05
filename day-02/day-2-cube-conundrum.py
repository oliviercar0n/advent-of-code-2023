import re


def p1(input_data: str):
    CONFIGURATION = (12, 13, 14)
    set_data_pattern = "(Game )(\d*): (.*)"
    color_pattern = "(\d*) (\w*)"

    sum_possible_game_ids = 0
    for game in input_data:
        game_possible = True
        parsed_game_data = re.match(set_data_pattern, game)
        game_id = int(parsed_game_data.group(2))
        set_data = parsed_game_data.group(3)
        set_list = set_data.split(";")
        for _set in set_list:
            for turn in _set.split(","):
                data = re.match(color_pattern, turn.strip())
                color = data.group(2)
                count = int(data.group(1))
                if color == "red" and count > CONFIGURATION[0]:
                    game_possible = False
                elif color == "green" and count > CONFIGURATION[1]:
                    game_possible = False
                elif color == "blue" and count> CONFIGURATION[2]:
                    game_possible = False
        
        if game_possible:
            sum_possible_game_ids += game_id

    print(f"The sum of all possible game IDs is {sum_possible_game_ids}")

def p2(input_data: str):
    set_data_pattern = "(Game )(\d*): (.*)"
    color_pattern = "(\d*) (\w*)"

    sum_powers = 0
    for game in input_data:
        red_values = []
        green_values = []
        blue_values = []
        parsed_game_data = re.match(set_data_pattern, game)
        set_data = parsed_game_data.group(3)
        set_list = set_data.split(";")
        for _set in set_list:
            for turn in _set.split(","):
                data = re.match(color_pattern, turn.strip())
                color = data.group(2)
                count = int(data.group(1))
                if color == "red":
                    red_values.append(count)
                elif color == "green":
                    green_values.append(count)
                elif color == "blue":
                    blue_values.append(count)

        sum_powers += max(red_values) * max(green_values) * max(blue_values)

    print(f"The sum of the powers is {sum_powers}")

with open("puzzle_input.txt", "r") as f:
    game_results = f.readlines()

p1(game_results)
p2(game_results)