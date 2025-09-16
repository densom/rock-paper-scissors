import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

from main import determine_winner, get_computer_choice, GameResult

def test_determine_winner():
    # Test tie scenarios
    assert determine_winner("rock", "rock") == GameResult.TIE
    assert determine_winner("paper", "paper") == GameResult.TIE
    assert determine_winner("scissors", "scissors") == GameResult.TIE

    # Test player wins
    assert determine_winner("rock", "scissors") == GameResult.PLAYER_WINS
    assert determine_winner("scissors", "paper") == GameResult.PLAYER_WINS
    assert determine_winner("paper", "rock") == GameResult.PLAYER_WINS

    # Test computer wins
    assert determine_winner("scissors", "rock") == GameResult.COMPUTER_WINS
    assert determine_winner("paper", "scissors") == GameResult.COMPUTER_WINS
    assert determine_winner("rock", "paper") == GameResult.COMPUTER_WINS

def test_computer_choice():
    # Test that computer choice is valid
    for _ in range(10):
        choice = get_computer_choice()
        assert choice in ['rock', 'paper', 'scissors']

if __name__ == "__main__":
    test_determine_winner()
    test_computer_choice()
    print("All tests passed!")