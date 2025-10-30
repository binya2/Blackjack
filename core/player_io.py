from core.game_logic import deal_two_each, calculate_hand_value, dealer_play


def ask_player_action() -> str:
    while True:
        user_input: str = input(f"Press 'S' for STAND, 'H' for HIT").upper()
        if user_input in ["S", "H"] and len(user_input) == 1:
            return user_input
        else:
            print("Invalid input. Please try again.")


def run_full_game(deck: list[dict], player: dict, dealer: dict) -> None:
    deal_two_each(deck, player, dealer)
    user_input: str = ask_player_action()
    while user_input == 'H':
        player_hand_value: int = calculate_hand_value(player["hand"])
        if player_hand_value > 21:
            print("Player hand value too high.\nGame Over..")
            break

    if user_input == 'S':
        dealer_all_in: bool = dealer_play(deck, player)
        if dealer_all_in:
            player_hand_value: int = calculate_hand_value(player["hand"])
            dealer_hand_value: int = calculate_hand_value(dealer["hand"])
            print(f"Player's card value:{player_hand_value}\n"
                  f" Value against the dealer:{dealer_hand_value}\n")
            if player_hand_value > dealer_hand_value:
                print("fThe player won!!!")
            if player_hand_value > dealer_hand_value:
                print("The dealer won!!!")
            if player_hand_value == dealer_hand_value:
                print(f"Draw!!!\n"
                      f"Player and dealer win")
