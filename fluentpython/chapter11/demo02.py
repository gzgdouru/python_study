'''
使用猴子补丁在运行时实现协议
'''
from collections import namedtuple
import random

Card = namedtuple("Card", ["rank", "suit"])


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list("JQKA")
    suits = "spades diamonds clubs hearts".split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]


def set_card(deck, position, card):
    deck._cards[position] = card

if __name__ == "__main__":
    deck = FrenchDeck()
    FrenchDeck.__setitem__ = set_card
    random.shuffle(deck)
    print(deck[:4])
