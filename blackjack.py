import random as rand

cards = []
suits = ["spades", "hearts", "clubs", "diamonds"]
ranks = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

for suit in suits:
    for rank in ranks:
        cards.append([suit, rank])


def shuffle() -> list:
    """
    Shuffles our list of cards
    """
    rand.shuffle(cards)


def deal() -> list:
    """This will deal a single card from a full, shuffled deck.

    Returns:
        a single card from our deck
    """
    hand = cards.pop()
    return hand


shuffle()
hand = deal()
print(hand)
