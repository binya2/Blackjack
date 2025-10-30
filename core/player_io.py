from core.game_logic import deal_two_each, calculate_hand_value, dealer_play


def ask_player_action() -> str:
    while True:
        user_input: str = input(f"\nPress 'S' for STAND, 'H' for HIT: ").upper()
        if user_input in ["S", "H"] and len(user_input) == 1:
            return user_input
        else:
            print("Invalid input. Please try again.")


def run_full_game(deck: list[dict], player: dict, dealer: dict) -> None:
    deal_two_each(deck, player, dealer)
    player_hand_value: int = calculate_hand_value(player["hand"])
    print(f"Welcome to Blackjack!!!\n"
          f"The values of your cards are: {player_hand_value}")
    user_input: str = ask_player_action()
    while user_input == 'H':
        user_input = h_input(deck, player)
    if user_input == 'S':
        s_input(deck, dealer, player)


def h_input(deck: list[dict], player: dict) -> str:
    player["hand"].append(deck.pop(0))
    player_hand_value: int = calculate_hand_value(player["hand"])
    print(f"The values of your cards are: {player_hand_value}")
    if player_hand_value > 21:
        print("Yuor hand value too high.\nGame Over..")
        return ""
    user_input: str = ask_player_action()
    return user_input


def s_input(deck: list[dict], dealer: dict, player: dict) -> None:
    dealer_all_in: bool = dealer_play(deck, dealer)
    if dealer_all_in:
        player_hand_value: int = calculate_hand_value(player["hand"])
        dealer_hand_value: int = calculate_hand_value(dealer["hand"])
        print(f"Player's card value: {player_hand_value}\n"
              f"Dealer's card value: {dealer_hand_value}\n")
        if player_hand_value > dealer_hand_value:
            print("The player won!!!")
        if player_hand_value < dealer_hand_value:
            print("The dealer won!!!")
        if player_hand_value == dealer_hand_value:
            print(f"Draw!!!\n"
                  f"Player and dealer win")
