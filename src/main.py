import random
from enum import Enum


class GameResult(Enum):
    TIE = "tie"
    PLAYER_WINS = "player"
    COMPUTER_WINS = "computer"


def display_rules():
    print("=== ROCK PAPER SCISSORS ===")
    print("Rules:")
    print("• Rock beats Scissors")
    print("• Scissors beats Paper")
    print("• Paper beats Rock")
    print("=" * 28)


def get_player_choice():
    while True:
        choice = input("Enter your choice (rock/paper/scissors) or 'q' to quit: ").strip()
        if choice in ["rock", "paper", "scissors", "DYNAMITE", "q"]:
            return choice
        print("Invalid choice! Please enter rock, paper, scissors, or 'q' to quit.")


def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])


def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return GameResult.TIE

    if player_choice == "DYNAMITE":
        return GameResult.PLAYER_WINS
    winning_combinations = {"rock": "scissors", "scissors": "paper", "paper": "rock"}

    if winning_combinations[player_choice] == computer_choice:
        return GameResult.PLAYER_WINS
    else:
        return GameResult.COMPUTER_WINS


def main():
    display_rules()
    print()

    while True:
        player_choice = get_player_choice()
        if player_choice == "q":
            print("Thanks for playing!")
            break

        computer_choice = get_computer_choice()

        print(f"\nYou chose: {player_choice}")
        print(f"Computer chose: {computer_choice}")
        print()

        winner = determine_winner(player_choice, computer_choice)

        if winner == GameResult.TIE:
            print("It's a tie!")
        elif winner == GameResult.PLAYER_WINS:
            print("You win!")
        else:
            print("Computer wins!")

        print()


if __name__ == "__main__":
    main()
