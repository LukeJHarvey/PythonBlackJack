from tkinter import N
from Player import Player
from Dealer import Dealer
from Shoe import Shoe
class Game:
    def __init__(self):
        self.initPlayers()
        self.dealer = Dealer()
        self.initDeck()
        self.gameLoop()

    def initPlayers(self):
        self.players = []
        create = True
        id = 1
        while create:
            #Player Creation
            name = input("Player {}'s Name: ".format(id))
            manual = input("Is {} automatic?(y/n): ".format(name))
            while manual not in ["y", "n"]:
                print("Incorrect input, only accepting 'y' or 'n'")
                manual = input("Is {} automatic?(y/n): ".format(name))
            manual = False if manual == "y" else True
            tips = False
            if manual:
                tips = input("Do you want tips while playing?(y/n): ")
                while tips not in ["y", "n"]:
                    print("Incorrect input, only accepting 'y' or 'n'")
                    tips = input("Do you want tips while playing?(y/n): ")
                tips = True if tips == "y" else False

            #Player Created
            self.players.append(Player(name, manual))
            print("Player {} Created!".format(name))

            #Prompt to create another player
            another_player = input("Do you wish to create another player?(y/n): ")
            while another_player not in ["y", "n"]:
                print("Incorrect input, only accepting 'y' or 'n'")
                another_player = input("Do you wish to create another player?(y/n): ")
            create = True if another_player == "y" else False
            id += 1

    def initDeck(self):
        self.shoe = Shoe()
        deckCount = input("How many Decks in Shoe?: ")
        self.shoe.generate_deck(int(deckCount))
        shuffleCount = int(input("How many deck shuffles?: "))
        for _ in range(shuffleCount):
            self.shoe.shuffle()

    def dealCards(self):
        for i in range(2):
            for p in self.players:
                c = self.shoe.draw()
                p.add_card(c)
                print("Player {} dealt {} Face Up.".format(p.name, c))
            c = self.shoe.draw()
            self.dealer.add_card(c)
            print("Dealer dealt {} Face {}.".format(c, "Down" if i == 0 else "Up"))
        
    def playerTurn(self, player):
        hit = True
        while hit:
            choice = player.choice()
            if choice:
                print("{} hits.".format(player.name))
                c = self.shoe.draw()
                print("{} is dealt {}".format(player.name, c))
                player.add_card(c)
                print("{}'s hand: {}".format(player.name, player.hand_string()))
            else:
                hit = False
                print("{} Stands with hand {}".format(player.name, player.hand_string()))
                print("{}'s hand value is: {}".format(player.name, player.get_highest_hand_value()))
            if player.bust == True:
                hit = False
                print("{} busts with hand {}".format(player.name, player.hand_string()))
            


    def gameLoop(self):
        #Deal Cards to all Players
        self.dealCards()
        
        #Each Player gets to play out their turn
        for p in self.players:
            self.playerTurn(p)
        self.playerTurn(self.dealer)

        #Win State
        if self.dealer.bust:
            for p in self.players:
                if not p.bust:
                    print("{} wins the hand against the dealers bust!".format(p.name))
        else:
            dealerHandValue = self.dealer.get_highest_hand_value()
            for p in self.players:
                if not p.bust:
                    playerHandValue = p.get_highest_hand_value()
                    if playerHandValue > dealerHandValue:
                        print("{} wins the hand against the dealer!".format(p.name))
                    elif playerHandValue == dealerHandValue:
                        print("{} ties with the dealer.".format(p.name))
                    else:
                        print("{} loses to the dealer.".format(p.name))

        #Put all Hands back into discard pile
        for p in self.players:
            self.shoe.add_to_discard(p.clear_hand())
        self.shoe.add_to_discard(self.dealer.clear_hand())

        #Decide to play next Hand
        cont = input("Do you wish to play another hand?(y/n): ")
        while cont not in ["y", "n"]:
            print("Incorrect input, only accepting 'y' or 'n'")
            cont = input("Do you wish to play another hand?(y/n): ")
        if cont == "y":
            print("Another round will be played.")
            self.gameLoop()
        else:
            print("Game has ended.")
            return
