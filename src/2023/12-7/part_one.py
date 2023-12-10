import collections
from collections import defaultdict

CARD_VALUE = {"A": 14, "K": 13, "Q": 12, "J": 11, "T": 10}


def get_hand_strength(cards):
    counts = collections.Counter(cards)
    count_len = len(counts)
    if count_len == 1:
        return 7

    if count_len == 2:
        if any([i == 4 for i in counts.values()]):
            return 6

        return 5

    if count_len == 3:
        if any([i == 3 for i in counts.values()]):
            return 4

        return 3

    if count_len == 4:
        return 2

    return 1


def order_hand_values(hands, card_start_index=0, excluded_hands=[], short=False):
    final_list = []

    for c in range(card_start_index, 5):
        for card_value in range(2, 15):
            hands_by_value = [
                hand
                for hand in hands
                if hand["values"][c] == card_value and hand not in excluded_hands
            ]

            if len(hands_by_value) == 0:
                continue

            if len(hands_by_value) == 1:
                final_list += hands_by_value
            else:
                final_list += order_hand_values(
                    hands_by_value,
                    card_start_index=c + 1,
                    excluded_hands=final_list + excluded_hands,
                )
        return final_list
    return final_list


def solve(file_location):
    puzzle_input = None
    with open(file_location) as f:
        puzzle_input = f.readlines()

    bid_ranks = defaultdict(lambda: [])
    for line in puzzle_input:
        cards, bid = line.replace("\n", "").split(" ")
        strength = get_hand_strength(cards)
        card_values = [int(CARD_VALUE.get(i) or i) for i in cards]
        bid_ranks[strength] += [
            {"bid": int(bid), "cards": cards, "values": card_values}
        ]

    hand_order = []
    for key, hands in dict(sorted(bid_ranks.items())).items():
        hand_count = len(hands)
        if hand_count == 0:
            continue

        if hand_count == 1:
            hand_order += hands
            continue

        hand_order += order_hand_values(hands)

    total = 0
    for index, hand in enumerate(hand_order):
        total += hand["bid"] * (index + 1)

    return total


print("Example", solve("example.txt"))
print("Puzzle", solve("input.txt"))
