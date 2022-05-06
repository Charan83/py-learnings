class Card:
    suit_allowed = ("Hearts", "Diamonds", "Clubs", "Spades")
    value_allowed = ("A", "2", "3", "4", "5", "6", "7",
                     "8", "9", "10", "J", "Q", "K")

    @classmethod
    def from_tuple(cls, card_suite_val):
        suit, val = card_suite_val
        return cls(suit, val)

    def __init__(self, suit, value):
        if suit not in Card.suit_allowed:
            raise ValueError(f"suit passes should be from {Card.suit_allowed}")
        if value not in Card.value_allowed:
            raise ValueError(
                f"value passes should be from {Card.value_allowed}")
        self.suit = suit
        self.value = value

    def __repr__(self) -> str:
        return f"{self.value} of {self.suit}"


if __name__ == '__main__':
    c1 = Card('Hearts', 'J')
    print(c1)


""" suit_allowed = ("Hearts", "Diamonds", "Clubs", "Spades")
value_allowed = ("A", "2", "3", "4", "5", "6", "7",
                 "8", "9", "10", "J", "Q", "K")
cards_list = [(suit, val) for suit in suit_allowed for val in value_allowed]
print(cards_list)
suit_1, val_1 = ('Heart', 'A')
print(suit_1, val_1) """
