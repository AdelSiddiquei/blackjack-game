from blackjack import blackjack as bj
import pytest


def test_complete_game(
    monkeypatch, capsys
):  # check to see if game reaches final message
    inputs = iter(["1", "s"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))  # Simulate 1 game
    game = bj.Game()
    game.play()

    output = capsys.readouterr().out
    assert "Thank you for playing!!!" in output


def test_check_winner(capsys):
    player_hand = bj.Hand()
    dealer_hand = bj.Hand(dealer=True)
    player_hand.take_cards(
        [
            bj.Card("hearts", {"rank": "A", "value": 11}),
            bj.Card("hearts", {"rank": "10", "value": 10}),
        ]
    )
    dealer_hand.take_cards(
        [
            bj.Card("spades", {"rank": "J", "value": 10}),
            bj.Card("spades", {"rank": "K", "value": 10}),
        ]
    )
    game = bj.Game()

    game.check_winner(player_hand, dealer_hand)

    output = capsys.readouterr().out
    assert "You have Blackjack, You win!!!" in output

    player_hand.take_cards([bj.Card("diamonds", {"rank": "5", "value": 5})])
    dealer_hand.take_cards([bj.Card("clubs", {"rank": "5", "value": 5})])

    game.check_winner(player_hand, dealer_hand)

    output = capsys.readouterr().out
    assert "Dealer busted, You win!!!" in output
