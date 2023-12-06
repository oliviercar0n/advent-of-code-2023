def p1(input_data: str):
    sum_calibration_values = 0
    for value in input_data:
        digits = [c for c in value if c.isdigit()]
        sum_calibration_values += int(digits[0] + digits[-1])

    print(f"The sum of all configuration values is {sum_calibration_values}")

def p2(input_data: str):

    numbers = [
        "zero",
        "one",
        "two",
        "three",
        "four",
        "five",
        "six",
        "seven",
        "eight",
        "nine",
    ]

    sum_calibration_values = 0
    for value in input_data:
        digits = []
        for i, character in enumerate(value):
            if character.isdigit():
                digits.append(character)
            for d, number in enumerate(numbers):
                if value[i:].startswith(number):
                    digits.append(str(d))

        calibration_value = int(digits[0] + digits[-1])
        sum_calibration_values += calibration_value

    print(f"The sum of all configuration values is {sum_calibration_values}")


with open("puzzle-input.txt", "r") as f:
    calibration_data_input = f.readlines()

p1(calibration_data_input)
p2(calibration_data_input)