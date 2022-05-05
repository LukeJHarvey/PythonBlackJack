
class Card:
    CARD_VALUE = {
        "A": (1,11),
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
        "10": 10,
        "J": 10,
        "Q": 10,
        "K": 10
    }
    def __init__(self, _value, _suit):
        self.value = str(_value) # A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K
        self.suit = _suit # D, C, H, S
    
    def get_value(self):
        return str(self.value)
    def get_suit(self):
        return self.suit

    def get_value_name(self):
        if self.value in ["A", "J", "Q", "K"]:
            if self.value == "A": return "Ace"
            elif self.value == "J": return "Jack"
            elif self.value == "Q": return "Queen"
            elif self.value == "K": return "King"
        return str(self.value)

    def get_suit_name(self):
        if self.value == "D": return "Diamonds"
        elif self.value == "C": return "Clubs"
        elif self.value == "H": return "Hearts"
        else: return "Spades"

    def print(self):
        ret = self.get_value_name()
        ret += " of "
        ret += self.get_suit_name()
        return ret

    def __str__(self):
        ret = "{}({})".format(self.value, self.suit)
        return ret