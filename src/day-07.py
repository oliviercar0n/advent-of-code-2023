with open("day-07-puzzle-input.txt", "r") as f:
    input_data = f.read().strip()

cards = ["J", "2", "3", "4", "5", "6", "7", "8", "9", "T", "Q", "K", "A"]

hands = [tuple(x.split()) for x in input_data.split("\n")]


five = []
four = []
three = []
two_pairs = []
pairs = []
single = []
full_house = []

for hand in hands:
    hs = hand[0]
    
    best_kind = 999
    for cc in cards[1:]:
        combos = []
        highest = ("", 0)
        hs_replaced = hs.replace("J", cc)
        for card in set(hs_replaced):
            occ = hs_replaced.count(card)
            combos.append((card, occ))
            if occ > highest[1]:
                highest = (card, occ)

        is_full_house = False
        is_two_pair = False
        c_pairs = []
        c_trips = []

        for combo in combos:
            if combo[1] == 2:
                c_pairs.append(combo)
            elif combo[1] == 3:
                c_trips.append(combo)
        if len(c_pairs) == 1 and len(c_trips) == 1:
            is_full_house = True
        elif len(c_pairs) == 2:
            is_two_pair = True

        if highest[1] == 5:
            hand_rank = 1
        elif highest[1] == 4:
            hand_rank = 2
        elif is_full_house:
            hand_rank = 3
        elif highest[1] == 3:
            hand_rank = 4
        elif is_two_pair:
            hand_rank = 5
        elif highest[1] == 2:
            hand_rank = 6
        else:
            hand_rank = 7

        if hand_rank < best_kind:
            best_kind = hand_rank

        
    if best_kind == 1:
        five.append(hand)
    elif best_kind == 2:
        four.append(hand)
    elif best_kind == 3:
        full_house.append(hand)
    elif best_kind == 4:
        three.append(hand)
    elif best_kind == 5:
        two_pairs.append(hand)
    elif best_kind == 6:
        pairs.append(hand)
    else:
        single.append(hand)


def f(hand):
    return [cards.index(c) for c in hand[0]]


# full_house = [(hand[0], hand[1], f(hand)[0], f(hand)[1], f(hand)[2], f(hand)[3], f(hand)[4]) for hand in full_house]
# full_house.sort(key=lambda k: (k[2],k[3],k[4],k[5],k[6]), reverse=True)

final_rank = []
for kind in [single, pairs, two_pairs, three, full_house, four, five]:
    expanded = [
        (hand[0], hand[1], f(hand)[0], f(hand)[1], f(hand)[2], f(hand)[3], f(hand)[4])
        for hand in kind
    ]
    expanded.sort(key=lambda k: (k[2], k[3], k[4], k[5], k[6]))
    final_rank.extend(expanded)

winnings = 0
for i, hand in enumerate(final_rank):
    # print(hand)
    winnings += (i + 1) * int(hand[1])

print(winnings)
