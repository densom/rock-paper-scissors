import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

from main import determine_winner, get_computer_choice

def test_determine_winner():
    # Test tie scenarios
    assert determine_winner("rock", "rock") == "tie"
    assert determine_winner("paper", "paper") == "tie"
    assert determine_winner("scissors", "scissors") == "tie"

    # Test player wins
    assert determine_winner("rock", "scissors") == "player"
    assert determine_winner("scissors", "paper") == "player"
    assert determine_winner("paper", "rock") == "player"

    # Test computer wins
    assert determine_winner("scissors", "rock") == "computer"
    assert determine_winner("paper", "scissors") == "computer"
    assert determine_winner("rock", "paper") == "computer"

def test_computer_choice():
    # Test that computer choice is valid
    for _ in range(10):
        choice = get_computer_choice()
        assert choice in ['rock', 'paper', 'scissors']

if __name__ == "__main__":
    test_determine_winner()
    test_computer_choice()
    print("All tests passed!")