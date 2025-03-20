from random import shuffle
from typing import Literal


class Card:
    """
    Used to represent the cards, their ranks and suits.
    """

    def __init__(
        self, suit: Literal["hearts", "diamonds", "clubs", "spades"], rank: dict
    ):
        """
        Args:
            suit : ["hearts", "diamonds", "clubs", "spades"]
            rank (dict): {'rank' : str , 'value' : int}
        """
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f"{self.rank['rank']} of {self.suit}"


class Deck:
    """
    Used to represent the deck we are playing from.
    """

    def __init__(self):
        self.cards = []
        suits = ["hearts", "diamonds", "clubs", "spades"]
        ranks = [
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
        for suit in suits:
            for rank in ranks:
                self.cards.append(Card(suit, rank))

    def shuffle(self):
        """
        Shuffle self.cards to create a shuffled deck
        """
        if len(self.cards) > 1:
            shuffle(self.cards)

    def deal(self, number: int) -> list:
        """
        Select and remove cards from self.cards . deck.shuffle first

        Args:
            number (int): number of cards to be dealt

        Returns:
            list: The cards that have been removed from self.cards
        """
        cards_dealt = []
        if len(self.cards) >= number >= 0:
            for i in range(number):
                card = self.cards.pop()
                cards_dealt.append(card)
        else:
            raise ValueError(
                "arg 'number' must be greater than 0 and less than len(self.cards)"
            )

        return cards_dealt


class Hand:
    def __init__(self, dealer=False):
        """
        Initialises hand.

        Args:
            dealer (bool, optional): Only true for dealer hand. Defaults to False.
        """
        self.cards = []
        self.value = 0
        self.dealer = dealer

    def take_cards(self, card_list: list):
        """
        Use to deal new cards to a hand.

        Args:
            card_list (list): The cards dealt, use self.deal on deck to create.
        """
        self.cards.extend(card_list)

    def calc_value(self):
        """
        Calculates Hand value and updates self.value
        """
        self.value = 0
        ace_count = 0
        for card in self.cards:
            card_value = int(card.rank["value"])
            self.value += card_value
            if card.rank["rank"] == "A":
                ace_count += 1

        while ace_count > 0 and self.value > 21:
            self.value -= 10
            ace_count -= 1

    def get_value(self):
        """
        Returns Hand value.

        Returns:
            Int: Hand value
        """
        self.calc_value()
        return self.value

    def isblackjack(self):
        """
        Checks for a win (a blackjack)
        Returns:
            Bool: True for a win.
        """
        return self.get_value() == 21

    def display(self, show_dealer_cards=False):
        print(f"""'{"Dealer" if self.dealer else "Your"} hand contains: """)
        for index, card in enumerate(self.cards):
            if (
                index == 0
                and self.dealer
                and not (show_dealer_cards or self.isblackjack())
            ):
                print("Hidden")
            else:
                print(card)
        if not self.dealer:
            print("Value: ", self.get_value())


class Game:
    def play(self):
        """
        This method starts and handles the game(s).
        """
        game_number = 0
        games_to_play = 0

        while games_to_play <= 0:
            try:
                games_to_play = int(input("How many games do you want to play?"))
            except:
                print("Input must be a positive integer number")

        while game_number < games_to_play:
            game_number += 1

            deck = Deck()
            deck.shuffle()

            player_hand = Hand()
            dealer_hand = Hand(dealer=True)

            for i in range(2):
                player_hand.take_cards(deck.deal(1))
                dealer_hand.take_cards(deck.deal(1))

            print(f"\n" + "*" * 20)
            print(f"Game {game_number} of {games_to_play}")
            print("*" * 20)

            player_hand.display()
            dealer_hand.display()

            if self.check_winner(player_hand, dealer_hand):
                continue

            choice = ""
            while player_hand.get_value() < 21 and choice not in ["s", "stand"]:
                choice = input("Please choose 'Hit' or 'Stand'").lower()
                print()
                while choice not in ["s", "stand", "h", "hit"]:
                    choice = input("Please choose 'Hit' or 'Stand' (Enter H/S)").lower()
                    print()
                if choice in ["h", "hit"]:
                    player_hand.take_cards(deck.deal(1))
                    player_hand.display()

            if self.check_winner(player_hand, dealer_hand):
                continue

            player_hand_value = player_hand.get_value()
            dealer_hand_value = dealer_hand.get_value()

            while dealer_hand_value < 17:
                dealer_hand.take_cards(deck.deal(1))
                dealer_hand_value = dealer_hand.get_value()

            dealer_hand.display(show_dealer_cards=True)

            if self.check_winner(player_hand, dealer_hand):
                continue

            print("Final Results")
            print("Your hand: ", player_hand_value)
            print(f"Dealer's hand: {dealer_hand_value}")

            self.check_winner(player_hand, dealer_hand, game_over=True)
        print("\n Thank you for playing!!!")

    def check_winner(self, player_hand: Hand, dealer_hand: Hand, game_over=False):
        """
        Checks for a winner
        Args:
            player_hand (Hand): Hand class
            dealer_hand (Hand): Hand class
            game_over (bool, optional): Only true if both players have chosen stand. Defaults to False.

        Returns:
            False (if no winner yet) or Str (if there is a winner)
        """
        if not game_over:
            if player_hand.get_value() > 21:
                print("You busted, Dealer Wins")
                return True
            elif dealer_hand.get_value() > 21:
                print("Dealer busted, You win!!!")
                return True
            elif player_hand.isblackjack() and dealer_hand.isblackjack():
                print("Both players have Blackjack, it's a tie.")
                return True
            elif player_hand.isblackjack():
                print("You have Blackjack, You win!!!")
                return True
            elif dealer_hand.isblackjack():
                print("Dealer has Blackjack, You lose.")
                return True
        else:
            if player_hand.get_value() > dealer_hand.get_value():
                print("Well done, you win!!!")
                return True
            elif player_hand.get_value() < dealer_hand.get_value():
                print("Peak, you Lose")
                return True
            elif player_hand.get_value() == dealer_hand.get_value():
                print("It's a tie.")
                return True
        return False
