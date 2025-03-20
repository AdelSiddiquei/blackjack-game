from blackjack import blackjack as bj

card1 = bj.Card("hearts", {"rank": "esbs", "value": 2})

try:
    print(card1)
except Exception as e:
    print(f"An error occured {e}")
