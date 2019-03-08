'''
定义抽象基类的子类
'''
import collections
import random

Card = collections.namedtuple("Card", ["rank", "suit"])


class FrenchDeck2(collections.MutableSequence):
    ranks = [str(n) for n in range(2, 11)] + list("JQKA")
    suits = "spades diamonds clubs hearts".split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]

    def __setitem__(self, key, value):
        self._cards[key] = value

    def __delitem__(self, key):
        del self._cards[key]

    def insert(self, index, value):
        self._cards.insert(index, value)

if __name__ == "__main__":
    deck = FrenchDeck2()
    random.shuffle(deck)
    print(deck[:4])
