from random import Random, random

def organized_deck(suits, ranks):
    deck = []

    for x in range(len(suits)):
        for y in range(len(ranks)):
            deck.append(ranks[y] + suits[x])

    return deck

def shuffle(deck):
    for x in range(10000):
        r1 = round(random() * 51)
        r2 = round(random() * 51)
        temp = deck[r1]
        deck[r1] = deck[r2]
        deck[r2] = temp