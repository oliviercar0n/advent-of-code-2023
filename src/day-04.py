import re


with open("day-04.txt", "r") as f:
    input_data = f.readlines()

CARD_PATTERN = "Card\s*\d*: (.*)"

# Part 1

total_points = 0
for card_data in input_data:
    parsed_card_data = re.match(CARD_PATTERN, card_data)
    card_results = parsed_card_data.group(1).split("|")
    winning_numbers_str = card_results[0]
    card_numbers_str = card_results[1]
    winning_numbers = [
        int(winning_numbers_str[i : i + 3])
        for i in range(0, len(winning_numbers_str), 3)
    ]
    card_numbers = [
        int(card_numbers_str[i : i + 3]) for i in range(0, len(card_numbers_str), 3)
    ]
    winning_number_count = 0
    for number in card_numbers:
        if number in winning_numbers:
            winning_number_count += 1

    if winning_number_count > 0:
        total_points += 2 ** (winning_number_count - 1)

print(total_points)

# Part 2

card_scores = []
cards_count = len(input_data)
for card_data in input_data:
    parsed_card_data = re.match(CARD_PATTERN, card_data)
    card_results = parsed_card_data.group(1).split("|")
    winning_numbers_str = card_results[0]
    card_numbers_str = card_results[1]
    winning_numbers = [
        int(winning_numbers_str[i : i + 3])
        for i in range(0, len(winning_numbers_str), 3)
    ]
    card_numbers = [
        int(card_numbers_str[i : i + 3]) for i in range(0, len(card_numbers_str), 3)
    ]
    winning_number_count = 0
    for number in card_numbers:
        if number in winning_numbers:
            winning_number_count += 1

    card_scores.append(winning_number_count)

card_copies = [1] * cards_count
for i, winning_num in enumerate(card_scores):
    current_card_copies = card_copies[i]
    if winning_num > 0:
        won_cards = range(i + 1, min(i + 1 + winning_num, cards_count))
        for card_num in won_cards:
            card_copies[card_num] += current_card_copies

print(sum(card_copies))
