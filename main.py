from player import *
from deck import *
from game_start import game_start

def game():
    SUITS = ['C', 'H', 'D', 'S']
    RANKS = ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K']
    MAX_PLAYER_NUMBER = 9

    deck = organized_deck(SUITS, RANKS)

    num_players = choose_players()
    players = create_players(num_players)

    game_over = False

    while (not game_over):
        shuffle(deck)
        players = players_shift(players)
        game_start(players, deck)

game()