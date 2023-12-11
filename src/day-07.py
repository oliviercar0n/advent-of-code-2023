with open("day-07.txt", "r") as f:
    input_data = f.read().strip()

cards = ["J", "2", "3", "4", "5", "6", "7", "8", "9", "T", "Q", "K", "A"]

hands = [tuple(x.split()) for x in input_data.split("\n")]


five = []
four = []
full_house = []
three = []
two_pairs = []
pairs = []
single = []

# Part 2
for hand in hands:
    hs = hand[0]
    best_kind = 999
    for cc in cards[1:]:
        c_pairs = []
        c_trips = []
        highest = 0
        hs_replaced = hs.replace("J", cc)
        for card in set(hs_replaced):
            occ = hs_replaced.count(card)
            combo = (card, occ)
            if occ == 2:
                c_pairs.append(combo)
            elif occ == 3:
                c_trips.append(combo)
            if occ > highest:
                highest = occ

        if highest == 5:
            hand_rank = 1
        elif highest == 4:
            hand_rank = 2
        elif len(c_pairs) == 1 and len(c_trips) == 1:  # Full House
            hand_rank = 3
        elif highest == 3:
            hand_rank = 4
        elif len(c_pairs) == 2:  # Two Pairs
            hand_rank = 5
        elif highest == 2:
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
    winnings += (i + 1) * int(hand[1])

print(winnings)
