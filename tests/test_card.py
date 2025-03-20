from blackjack import blackjack as bj
from random import choice

suitlist = ["hearts", "diamonds", "clubs", "spades"]
ranklist = [
    {"rank": "A", "value": 11},
    {"rank": "2", "value": 2},
    {"rank": "3", "value": 3},
    {"rank": "4", "value": 4},
    {"rank": "5", "value": 5},
    {"rank": "6", "value": 6},
    {"rank": "7", "value": 7},
    {"rank": "8", "value": 8},
    {"rank": "9", "value": 9},
    {"rank": "10", "value": 10},
    {"rank": "J", "value": 10},
    {"rank": "Q", "value": 10},
    {"rank": "K", "value": 10},
]


def test_init():
    suit = choice(suitlist)
    rank = choice(ranklist)
    card = bj.Card(suit, rank)

    assert card.suit == suit
    assert card.rank["rank"] == rank["rank"]
    assert card.rank["value"] == rank["value"]


def test_str():
    suit = choice(suitlist)
    rank = choice(ranklist)
    card = bj.Card(suit, rank)

    assert str(card) == f"{card.rank['rank']} of {suit}"
