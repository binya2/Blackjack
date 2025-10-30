def calculate_hand_value(hand: list[dict]) -> int:
    value_of_card = {'A': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 20, 'Q': 10,
                     'K': 10}
    sum_of_hand: int = 0
    have_ace: bool = False
    for card in hand:
        value = card['rank']
        if value == 'A':
            have_ace = True
        sum_of_hand += value_of_card[value]
    if have_ace:
        if sum_of_hand + 10 <= 21:
            sum_of_hand += 10
    return sum_of_hand


def deal_two_each(deck: list[dict], player: dict, dealer: dict) -> None:
    dealer["hand"] += [deck.pop(0) for _ in range(2)]
    player["hand"] += [deck.pop(0) for _ in range(2)]


def dealer_play(deck: list[dict], dealer: dict) -> bool:
    dealer_hand_value: int = calculate_hand_value(dealer["hand"])
    while dealer_hand_value <= 17:
        dealer["hand"].append(deck.pop(0))
        dealer_hand_value: int = calculate_hand_value(dealer["hand"])
    if 17 <= calculate_hand_value(dealer["hand"]) <= 21:
        return True
    return False
