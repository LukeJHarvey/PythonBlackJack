from CountStrategy import CountStrategy
from Card import Card
from Shoe import Shoe
from AbsPlayer import AbsPlayer

def testCountStrategies():
    hiLo = CountStrategy("Hi-Lo")
    hiLo1 = CountStrategy("Hi-Lo I")
    hiLo2 = CountStrategy("Hi-Lo II")
    ko = CountStrategy("KO")
    omega = CountStrategy("Omega II")
    halves = CountStrategy("Halves")
    zen = CountStrategy("Zen Count")
    count = CountStrategy("10 Count")
    assert hiLo.getBJValues("A") == -1, "Hi-Lo Ace should be -1"
    assert hiLo1.getBJValues(2) == 0, "Hi-Lo I 2 should be 0"
    assert hiLo2.getBJValues(10) == -2, "Hi-Lo II 10 should be -2"
    assert hiLo2.getBJValues("J") == -2, "Hi-Lo II J/Q/K should be -2"
    assert ko.getBJValues("3") == 1, "KO 3 should be 1"
    assert omega.getBJValues("Q") == -2, "Omega II Q should be -2"
    assert halves.getBJValues(2) == 0.5, "Halves 2 should be 0.5"
    assert zen.getBJValues(4) == 2, "Zen Count 4 should be 2"
    assert count.getBJValues("K") == -2, "10 Count K should be -2"

def testCard():
    aceDiamonds = Card("A", "D")
    threeSpades = Card("3", "S")
    eightClubs = Card(8, "C")
    jackHearts = Card("J", "H")
    queenSpades = Card("Q", "S")
    kingDiamonds = Card("K", "D")
    assert aceDiamonds.getValue() == "A", "Ace of Diamonds is not the correct value"
    assert aceDiamonds.getSuit() == "D", "Ace of Diamonds is not the correct Suit"
    assert threeSpades.getValue() == "3", "Three of Spades is not the correct value"
    assert threeSpades.getSuit() == "S", "Three of Spades is not the correct Suit"
    assert eightClubs.getValue() == "8", "Eight of Clubs is not the correct value"
    assert eightClubs.getSuit() == "C", "Eight of Clubs is not the correct Suit"
    assert jackHearts.getValue() == "J", "Jack of Hearts is not the correct value"
    assert jackHearts.getSuit() == "H", "Jack of Hearts is not the correct Suit"
    assert queenSpades.getValue() == "Q", "Queen of Spades is not the correct value"
    assert queenSpades.getSuit() == "S", "Queen of Spades is not the correct Suit"
    assert kingDiamonds.getValue() == "K", "King of Diamonds is not the correct value"
    assert kingDiamonds.getSuit() == "D", "King of Diamonds is not the correct Suit"

def testAbsPlayer():
    c1 = Card("A", "D")
    c2 = Card("5", "H")
    c3 = Card("J", "H")
    tPlayer = AbsPlayer()
    tPlayer.addCard(c1)
    assert tPlayer.getHandValue() == [1,11]
    tPlayer.addCard(c2)
    assert tPlayer.getHandValue() == [6,16]
    tPlayer.addCard(c3)
    assert tPlayer.getHandValue() == [16,26]
    tPlayer.addCard(c1)
    assert tPlayer.getHandValue() == [17,27,27,37]
    tPlayer.clearHand()
    assert tPlayer.getHandValue() == [0]
    tPlayer.addCard(c3)
    assert tPlayer.getHandValue() == [10]

def testShoe():
    shoe = Shoe()
    shoe.generateDeck(3)
    shoe.shuffle()
    #shoe.print_deck()

if __name__ == "__main__":
    testCountStrategies()
    testCard()
    testAbsPlayer()
    #testShoe()

    print("All Tests Completed")