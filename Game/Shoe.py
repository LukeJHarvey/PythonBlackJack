from Card import Card
import random
class Shoe:
    DECK_LAYOUT = (["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"], ["D", "C", "H", "S"])
    def __init__(self):
        self.deck = []
        self.discard = []
    
    def generateDeck(self, num):
        for _ in range(num):
            for suit in Shoe.DECK_LAYOUT[1]:
                for value in Shoe.DECK_LAYOUT[0]:
                    self.deck.append(Card(value, suit))
    
    def shuffle(self):
        random.shuffle(self.deck)

    def draw(self):
        if len(self.deck) > 0:
            return self.deck.pop()
        else:
            print("Shoe is empty. Reshuffling Deck.")
            self.deck = self.discard
            self.discard = []
    
    def addToDiscard(self, hand):
        for c in hand:
            self.discard.append(c)

    def printDeck(self):
        for i in self.deck:
            print(i)