from blackjack import blackjack as bj
from random import choice
import pytest

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
    dealer_hand = bj.Hand(dealer=True)
    assert len(hand.cards) == 0
    assert hand.value == 0
    assert not hand.dealer
    assert len(dealer_hand.cards) == 0
    assert dealer_hand.value == 0
    assert dealer_hand.dealer


def test_take_cards():
    hand = bj.Hand()
    cards = []
    for i in range(5):
        cards.append(bj.Card(choice(suitlist), choice(ranklist)))

    hand.take_cards(cards)

    assert len(hand.cards) == 5

    for i in range(5):
        assert hand.cards[0] == cards[0]


def test_calc_value():
    hand = bj.Hand()
    hand.take_cards(
        [
            bj.Card("hearts", {"rank": "A", "value": 11}),
            bj.Card("spades", {"rank": "10", "value": 10}),
            bj.Card("diamonds", {"rank": "5", "value": 5}),
        ]
    )

    hand.calc_value()
    assert hand.value == 16


def test_isblackjack():
    hand = bj.Hand()
    hand.take_cards(
        [
            bj.Card("hearts", {"rank": "A", "value": 11}),
            bj.Card("diamonds", {"rank": "J", "value": 10}),
        ]
    )

    assert hand.isblackjack  # Should return true since hand.calc_value should return 21, so hand.isblackjack should return true.


def test_display_hand(capsys):
    hand = bj.Hand()
    hand.take_cards(
        [
            bj.Card("hearts", {"rank": "A", "value": 11}),
            bj.Card("diamonds", {"rank": "J", "value": 10}),
        ]
    )

    hand.display()
    captured = capsys.readouterr()  # captures output
    """Testing non-dealer hand"""
    assert "Your hand contains:" in captured.out
    assert "A of hearts" in captured.out
    assert "J of diamonds" in captured.out
    assert "Value:  21" in captured.out

    dealer_hand = bj.Hand(dealer=True)
    dealer_hand.take_cards(
        [
            bj.Card("spades", {"rank": "A", "value": 11}),
            bj.Card("clubs", {"rank": "7", "value": 7}),
        ]
    )

    dealer_hand.display()
    captured = capsys.readouterr()

    assert "Dealer hand contains:" in captured.out
    assert "Hidden" in captured.out
    assert "A of spades" not in captured.out
    assert "7 of clubs" in captured.out

    dealer_hand.display(show_dealer_cards=True)
    captured = capsys.readouterr()

    assert "Hidden" not in captured.out
    assert "A of spades" in captured.out
    assert "7 of clubs" in captured.out
