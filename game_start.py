from betting import *

def card_distribute(players, deck):
    num_players = len(players)
    for x in range(num_players):
        hand = [deck[x], deck[num_players + x]]
        players[x].set_hand(hand)

def game_start(players, deck):
    board = ['XX', 'XX', 'XX', 'XX', 'XX']
    card_distribute(players, deck)

    betting = Betting(players)
    preflop(betting, players)    