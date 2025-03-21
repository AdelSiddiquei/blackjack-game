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

def test_hand_init():
    hand = bj.Hand()
    dealer_hand = bj.Hand(dealer= True)
    assert len(hand.cards) == 0
    assert hand.value == 0
    assert not hand.dealer
    assert len( dealer_hand.cards) == 0
    assert  dealer_hand.value == 0
    assert  dealer_hand.dealer

def test_take_cards():
    hand = bj.Hand()
    card = bj.Card(choice(suitlist), choice(ranklist))
    hand.add_card(card)

    assert len(hand.cards) == 1
    assert hand.cards[0] == card