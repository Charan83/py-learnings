from random import shuffle
from Card import Card


class Deck:
    suit_allowed = ("Hearts", "Diamonds", "Clubs", "Spades")
    value_allowed = ("A", "2", "3", "4", "5", "6", "7",
                     "8", "9", "10", "J", "Q", "K")
    """ deck_count = len([(suit, val)
                     for suit in suit_allowed for val in value_allowed]) """

    def __init__(self):
        """ all_cards_combinations = [(suit, val)
                                  for val in Deck.value_allowed for suit in Deck.suit_allowed]
        print(all_cards_combinations)
        print(len(all_cards_combinations))
        self.cards = [Card.from_tuple(t) for t in all_cards_combinations] 
        print(f"Deck Count printing : {Deck.deck_count}") """
        self.cards = [Card(suit, val)
                      for val in Deck.value_allowed for suit in Deck.suit_allowed]

    def __repr__(self):
        return f"Deck of {len(self.cards)} cards"

    def __iter__(self):
        # return self.cards  # iter() returned non-iterator of type 'list'
        return iter(self.cards)

    def _deal(self, num):
        if len(self.cards) < num & len(self.cards) != 0:
            self.cards = []
        elif not len(self.cards):
            raise ValueError(f"All cards have been dealt!")

        self.cards_dealt = self.cards[-num:]
        self.cards = self.cards[:-num]

    def deal_card(self):
        self._deal(1)
        return self.cards_dealt[0]

    def deal_hand(self, num):
        self._deal(num)
        return self.cards_dealt

    def count(self):
        return len(self.cards)

    def shuffle(self):
        if self.count() != 52:
            print(
                f"{self.count()} card are only present! But we need full deck of cards ")
            raise ValueError("Only full decks can be shuffled")
        shuffle(self.cards)


if __name__ == '__main__':
    deck1 = Deck()
"""     print(deck1.cards)
    deck1.shuffle()
    print("******Shuffle in progress******")
    print(deck1.cards) """
"""     print(deck1.deal_card())
    print(deck1)
    print(deck1.deal_hand(20))
    print(deck1)
    print(deck1.deal_hand(20))
    print(deck1)
    print(deck1.deal_hand(12))
    print(deck1)
    print(deck1.deal_card())
    print(deck1) """

for d in deck1:
    print(d)  # 'Deck' object is not iterable
