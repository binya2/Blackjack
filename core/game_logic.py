def calculate_hand_value(hand: list[dict]) -> int:
    value_of_card = {'A': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 20, 'Q': 10,
                     'K': 10}
    sum_of_hand: int = 0
    for card in hand:
        sum_of_hand += value_of_card[card['rank']]
    return sum_of_hand


def deal_two_each(deck: list[dict], player: dict, dealer: dict) -> None:
    dealer["hand"] += [deck.pop(0) for _ in range(2)]
    player["hand"] += [deck.pop(0) for _ in range(2)]


def dealer_play(deck: list[dict], dealer: dict) -> bool:
    while calculate_hand_value(dealer["hand"]) <= 17:
        dealer["hand"] += deck.pop(0)
    if 17 <= calculate_hand_value(dealer["hand"]) <= 21:
        return True
    return False
