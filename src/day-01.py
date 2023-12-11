with open("day-01.txt", "r") as f:
    calibration_data_input = f.readlines()

# Part 1

sum_calibration_values = 0
for value in calibration_data_input:
    digits = [c for c in value if c.isdigit()]
    sum_calibration_values += int(digits[0] + digits[-1])

print(sum_calibration_values)

# Part 2

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
for value in calibration_data_input:
    digits = []
    for i, character in enumerate(value):
        if character.isdigit():
            digits.append(character)
        for d, number in enumerate(numbers):
            if value[i:].startswith(number):
                digits.append(str(d))

    sum_calibration_values += int(digits[0] + digits[-1])

print(sum_calibration_values)
