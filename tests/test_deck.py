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
    try:
        assert len(deck.cards) == len(suitlist)*len(ranklist)  # checking correct deck size
    except AssertionError:
        print("Deck.__init__(), Deck.cards incorrect size")
    
    try:
        assert len(deck.cards) == len(set(deck.cards))  # checking no duplicates
    except AssertionError:
        print("Deck.__init__(),Deck.cards contains duplicates")
    
    for card in deck.cards:
        
        try:
            assert (card.suit in suitlist)
        except AssertionError:
            print("Deck.__init__(), Deck.cards has Card with unexpected suit")

        try:
            assert card.rank in ranklist
        except AssertionError:
            print("Deck.__init__(), Deck.cards has Card with unexpected rank")


def test_shuffle():
    deck = bj.Deck()
    original_deck = deck.cards.copy()
    deck.shuffle()

    try:
        assert set(original_deck) == set(deck.cards)
    except AssertionError:
        print("Deck.shuffle() has changed the elements in Deck.cards")
    
    try:
        assert len(original_deck) == len(deck.cards)
    except AssertionError:
        print("Deck.shuffle() has changed the size of Deck.cards")

    try:
        assert original_deck != deck.cards
    except AssertionError:
        print("if test_shuffle() has not returned any other messages then Deck.shuffle() has not shuffled Deck.cards")

def test_deal():
    deck = bj.Deck()
    original_deck = deck.cards.copy()
    cards_dealt = []
    cards_dealt.extend(deck.deal(randrange(1, len(deck.cards))))

    try:
        assert set(original_deck) != set(deck.cards)
    except AssertionError:
        print("Deck.Deal(), deck.cards has stayed the same")
    
    try:
        assert set(cards_dealt) <= set(original_deck)
    except AssertionError:
        print("Deck.Deal(), cards dealt not from original deck.cards")
    
    try:
        assert not set(cards_dealt).issubset(set(deck.cards))
    except AssertionError:
        print("Deck.Deal(), cards dealt not removed from deck.cards")
    

