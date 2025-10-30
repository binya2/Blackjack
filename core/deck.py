import random


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
    for _ in range(swaps):
        index1: int = random.randrange(1, 52)
        index2: int = check_by_suit(deck, index1)

        temp: dict = deck[index1]
        deck[index1] = deck[index2]
        deck[index2] = temp
    return deck


def check_by_suit(deck: list[dict], index1: int) -> int:
    index2: int = random.randrange(1, 52)
    card1: dict = deck[index1]
    while True:
        card_equal: bool = index2 == index1
        if not card_equal:
            suite = card1["suite"]
            match suite:
                case "H":
                    if index2 % 5 == 0:
                        break
                case "C":
                    if index2 % 3 == 0:
                        break
                case "D":
                    if index2 % 2 == 0:
                        break
                case "S":
                    if index2 % 7 == 0:
                        break
        index2: int = random.randrange(1, 52)
    return index2
