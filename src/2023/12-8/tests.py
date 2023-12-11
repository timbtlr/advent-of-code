from part_one import get_hand_strength, order_hand_values
from part_two import get_hand_strength as get_hand_strength_wild

assert get_hand_strength("AAAAA") == 7
assert get_hand_strength("AAAAK") == 6
assert get_hand_strength("AAAKK") == 5
assert get_hand_strength("AAAK2") == 4
assert get_hand_strength("AAKK2") == 3
assert get_hand_strength("AAKQ2") == 2
assert get_hand_strength("AKQJT") == 1


assert get_hand_strength_wild("AAAAA") == 7
assert get_hand_strength_wild("AAAAK") == 6
assert get_hand_strength_wild("AAAKK") == 5
assert get_hand_strength_wild("AAAK2") == 4
assert get_hand_strength_wild("AAKK2") == 3
assert get_hand_strength_wild("AAKQ2") == 2
assert get_hand_strength_wild("AKQ9T") == 1

assert get_hand_strength_wild("AAJJJ") == 7
assert get_hand_strength_wild("AJJJJ") == 7
assert get_hand_strength_wild("JJJJJ") == 7
assert get_hand_strength_wild("AAAJK") == 6
assert get_hand_strength_wild("AAJJK") == 6
assert get_hand_strength_wild("AJJJK") == 6
assert get_hand_strength_wild("AAJKK") == 5
assert get_hand_strength_wild("AAJK2") == 4
assert get_hand_strength_wild("AJJK2") == 4
assert get_hand_strength_wild("AJ123") == 2
assert get_hand_strength_wild("A1234") == 1

assert order_hand_values(
    [
        {"values": [10, 5, 5, 11, 5]},
        {"values": [12, 12, 12, 11, 14]},
    ]
) == [
    {"values": [10, 5, 5, 11, 5]},
    {"values": [12, 12, 12, 11, 14]},
]


assert order_hand_values(
    [
        {"values": [13, 13, 6, 7, 7]},
        {"values": [13, 10, 11, 11, 10]},
    ]
) == [
    {"values": [13, 10, 11, 11, 10]},
    {"values": [13, 13, 6, 7, 7]},
]


assert order_hand_values(
    [
        {"bid": 329, "cards": "55655", "values": [5, 5, 6, 5, 5]},
        {"bid": 237, "cards": "6T666", "values": [6, 10, 6, 6, 6]},
        {"bid": 764, "cards": "99998", "values": [9, 9, 9, 9, 8]},
        {"bid": 841, "cards": "88688", "values": [8, 8, 6, 8, 8]},
        {"bid": 948, "cards": "A9999", "values": [14, 9, 9, 9, 9]},
        {"bid": 186, "cards": "22322", "values": [2, 2, 3, 2, 2]},
        {"bid": 736, "cards": "77T77", "values": [7, 7, 10, 7, 7]},
        {"bid": 730, "cards": "A5AAA", "values": [14, 5, 14, 14, 14]},
        {"bid": 282, "cards": "TATTT", "values": [10, 14, 10, 10, 10]},
        {"bid": 699, "cards": "66A66", "values": [6, 6, 14, 6, 6]},
        {"bid": 776, "cards": "4TTTT", "values": [4, 10, 10, 10, 10]},
        {"bid": 793, "cards": "8888J", "values": [8, 8, 8, 8, 11]},
        {"bid": 209, "cards": "JJJ2J", "values": [11, 11, 11, 2, 11]},
        {"bid": 898, "cards": "77747", "values": [7, 7, 7, 4, 7]},
    ]
) == [
    {"bid": 186, "cards": "22322", "values": [2, 2, 3, 2, 2]},
    {"bid": 776, "cards": "4TTTT", "values": [4, 10, 10, 10, 10]},
    {"bid": 329, "cards": "55655", "values": [5, 5, 6, 5, 5]},
    {"bid": 699, "cards": "66A66", "values": [6, 6, 14, 6, 6]},
    {"bid": 237, "cards": "6T666", "values": [6, 10, 6, 6, 6]},
    {"bid": 898, "cards": "77747", "values": [7, 7, 7, 4, 7]},
    {"bid": 736, "cards": "77T77", "values": [7, 7, 10, 7, 7]},
    {"bid": 841, "cards": "88688", "values": [8, 8, 6, 8, 8]},
    {"bid": 793, "cards": "8888J", "values": [8, 8, 8, 8, 11]},
    {"bid": 764, "cards": "99998", "values": [9, 9, 9, 9, 8]},
    {"bid": 282, "cards": "TATTT", "values": [10, 14, 10, 10, 10]},
    {"bid": 209, "cards": "JJJ2J", "values": [11, 11, 11, 2, 11]},
    {"bid": 730, "cards": "A5AAA", "values": [14, 5, 14, 14, 14]},
    {"bid": 948, "cards": "A9999", "values": [14, 9, 9, 9, 9]},
]
