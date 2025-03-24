from blackjack import blackjack as bj
from random import randrange

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
    deck = bj.Deck()

    assert len(deck.cards) == len(suitlist) * len(
        ranklist
    )  # checking correct deck size

    assert len(deck.cards) == len(set(deck.cards))  # checking no duplicates

    for card in deck.cards:
        assert card.suit in suitlist

        assert card.rank in ranklist


def test_shuffle():
    deck = bj.Deck()
    original_deck = deck.cards.copy()
    deck.shuffle()

    assert set(original_deck) == set(deck.cards)

    assert len(original_deck) == len(deck.cards)

    assert original_deck != deck.cards


def test_deal():
    deck = bj.Deck()
    original_deck = deck.cards.copy()
    cards_dealt = []
    cards_dealt.extend(deck.deal(randrange(1, len(deck.cards))))

    assert set(original_deck) != set(deck.cards)

    assert set(cards_dealt) <= set(original_deck)

    assert not set(cards_dealt) <= set(deck.cards)
