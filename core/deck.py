def build_standard_deck() -> list[dict]:
    suite_dict = {0: 'H', 1: 'C', 2: 'D', 3: 'S'}
    rank_revers_dict = {0: 'A', 1: '2', 2: '3', 3: '4', 4: '5', 5: '6', 6: '7',
                        7: '8', 8: '9', 9: '10', 10: 'J', 11: 'Q', 12: 'K'}
    deck_cards: list[dict] = []
    for i in range(52):
        num = i % 13
        side = int(i / 13)
        deck_cards.append({"rank": rank_revers_dict[num], "suite": suite_dict[side]})
    return deck_cards


def shuffle_by_suit(deck: list[dict], swaps: int = 5000) -> list[dict]:
    pass

# def shuffle(deck: list[dict]) -> list[dict]:
#     shuffle_list = deck.copy()
#     for i in range(1000):
#         num1 = random.randrange(1, 52)
#         num2 = random.randrange(1, 52)
#         if num1 == num2:
#             i -= 1
#             continue
#         shuffle_list[num1], shuffle_list[num2] = shuffle_list[num2], shuffle_list[num1]
#
#     return shuffle_list
