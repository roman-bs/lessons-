"""
Написать функцию которая возвращают случайным образом одну карту из стандартной колоды в 36 карт,
 где на первом месте номинал карты номинал (6 - 10, J, D, K, A), а на втором название масти (Hearts, Diamonds, Clubs, Spades).
"""
import random


number_card = ["6", "7", "8", "9", "10", "J", "D", "K", "A"]
card_suit = ["Hearts", "Diamonds", "Clubs", "Spades"]


def card_36():
    card = (f"{random.choice(number_card)} {random.choice(card_suit)}")
    return card

print(card_36())

