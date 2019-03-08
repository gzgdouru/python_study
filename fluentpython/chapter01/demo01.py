'''
一摞python风格的纸牌
'''
from collections import namedtuple
import random

Card = namedtuple("Card", ["rank", "suit"])


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list("JQKA")
    suits = "spades diamonds clubs hearts".split()

    def __init__(self):
        self._crads = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    def __len__(self):
        return len(self._crads)

    def __getitem__(self, position):
        return self._crads[position]


suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)


def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]


if __name__ == "__main__":
    deck = FrenchDeck()
    # print(len(deck))
    # print(deck[11])
    # print(random.choice(deck))

    for card in sorted(deck, key=spades_high):
        print(card)
