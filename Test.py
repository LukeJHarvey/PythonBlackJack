from CountStrategy import CountStrategy
from Card import Card
from Shoe import Shoe
from AbsPlayer import AbsPlayer

def test_countstrategies():
    hiLo = CountStrategy("Hi-Lo")
    hiLo1 = CountStrategy("Hi-Lo I")
    hiLo2 = CountStrategy("Hi-Lo II")
    ko = CountStrategy("KO")
    omega = CountStrategy("Omega II")
    halves = CountStrategy("Halves")
    zen = CountStrategy("Zen Count")
    count = CountStrategy("10 Count")
    assert hiLo.get_bj_values("A") == -1, "Hi-Lo Ace should be -1"
    assert hiLo1.get_bj_values(2) == 0, "Hi-Lo I 2 should be 0"
    assert hiLo2.get_bj_values(10) == -2, "Hi-Lo II 10 should be -2"
    assert hiLo2.get_bj_values("J") == -2, "Hi-Lo II J/Q/K should be -2"
    assert ko.get_bj_values("3") == 1, "KO 3 should be 1"
    assert omega.get_bj_values("Q") == -2, "Omega II Q should be -2"
    assert halves.get_bj_values(2) == 0.5, "Halves 2 should be 0.5"
    assert zen.get_bj_values(4) == 2, "Zen Count 4 should be 2"
    assert count.get_bj_values("K") == -2, "10 Count K should be -2"

def test_card():
    aceDiamonds = Card("A", "D")
    threeSpades = Card("3", "S")
    eightClubs = Card(8, "C")
    jackHearts = Card("J", "H")
    queenSpades = Card("Q", "S")
    kingDiamonds = Card("K", "D")
    assert aceDiamonds.get_value() == "A", "Ace of Diamonds is not the correct value"
    assert aceDiamonds.get_suit() == "D", "Ace of Diamonds is not the correct Suit"
    assert threeSpades.get_value() == "3", "Three of Spades is not the correct value"
    assert threeSpades.get_suit() == "S", "Three of Spades is not the correct Suit"
    assert eightClubs.get_value() == "8", "Eight of Clubs is not the correct value"
    assert eightClubs.get_suit() == "C", "Eight of Clubs is not the correct Suit"
    assert jackHearts.get_value() == "J", "Jack of Hearts is not the correct value"
    assert jackHearts.get_suit() == "H", "Jack of Hearts is not the correct Suit"
    assert queenSpades.get_value() == "Q", "Queen of Spades is not the correct value"
    assert queenSpades.get_suit() == "S", "Queen of Spades is not the correct Suit"
    assert kingDiamonds.get_value() == "K", "King of Diamonds is not the correct value"
    assert kingDiamonds.get_suit() == "D", "King of Diamonds is not the correct Suit"

def test_absplayer():
    c1 = Card("A", "D")
    c2 = Card("5", "H")
    c3 = Card("J", "H")
    tPlayer = AbsPlayer()
    tPlayer.add_card(c1)
    assert tPlayer.get_hand_value() == [1,11]
    tPlayer.add_card(c2)
    assert tPlayer.get_hand_value() == [6,16]
    tPlayer.add_card(c3)
    assert tPlayer.get_hand_value() == [16,26]
    tPlayer.add_card(c1)
    assert tPlayer.get_hand_value() == [17,27,27,37]
    tPlayer.clear_hand()
    assert tPlayer.get_hand_value() == [0]
    tPlayer.add_card(c3)
    assert tPlayer.get_hand_value() == [10]

def test_shoe():
    shoe = Shoe()
    shoe.generate_deck(3)
    shoe.shuffle()
    #shoe.print_deck()

if __name__ == "__main__":
    test_countstrategies()
    test_card()
    test_absplayer()
    #test_shoe()

    print("All Tests Completed")