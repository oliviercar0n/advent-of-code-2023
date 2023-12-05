with open("puzzle_input.txt", "r") as f:
    calibration_data_input = f.readlines()

sum_calibration_values = 0
for value in calibration_data_input:
    first_digit = None
    last_digit = None
    for character in value:
        if character.isdigit():
            if last_digit is None:
                first_digit = character
            last_digit = character

    calibration_value = int(first_digit + last_digit)
    sum_calibration_values += calibration_value

print(f"The sum of all configuration values is {sum_calibration_values}")