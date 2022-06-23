from Player.Player import Player
from Player.Dealer import Dealer
from Shoe import Shoe
from Utils import YNInput, typedInput
import json
class BlackJack:
    def __init__(self, initPlayersFileName = "", initDeckFileName = ""):
        self.initPlayers(initPlayersFileName)
        self.dealer = Dealer()
        self.initDeck(initDeckFileName)
        self.gameLoop()

    def initPlayers(self, initPlayersFileName):
        self.players = []
        if initPlayersFileName == "":
            if YNInput("Use Json File to Load Player Information?(yes/no): "):
                fileName = input("Name of Json File: ")
                self.loadPlayersJson(fileName)
            if YNInput("Do you wish to create another player?(yes/no): "):
                self.createPlayers()
        else:
            self.loadPlayersJson(initPlayersFileName)
            if YNInput("Do you wish to create another player?(yes/no): "):
                self.createPlayers()

    def loadPlayersJson(self, fileName):
        if ".json" not in fileName: fileName += ".json"
        with open(fileName, "r") as file:
            data = json.loads(file.read())
            cashStart = -1 if not "Start_Cash" in data else data["Start_Cash"]
            for player in data["Players"]:
                if cashStart == -1:
                    self.players.append(Player(player["Name"], player["Manual"], player["Money"]))
                else:
                    self.players.append(Player(player["Name"], player["Manual"], cashStart))

    def createPlayers(self, startMoney = 1000):
        create = True
        while create:
            #Player Creation
            name = input("New Player's Name: ")

            manual = YNInput("Is {} automatic?(yes/no): ".format(name))

            tips = False
            if manual:
                tips = YNInput("Do you want tips while playing?(yes/no): ")

            money = startMoney
            #money = typedInput("Starting Cash Amount({} if empty): ".format(startMoney), int)
            #money = startMoney if money is -1 else money

            #Player Created
            self.players.append(Player(name, manual, tips, money))
            print("Player {} Created!".format(name))

            #Prompt to create another player
            create = YNInput("Do you wish to create another player?(yes/no): ")

    def initDeck(self, initDeckFileName):
        if initDeckFileName == "":
            self.shoe = Shoe()
            deckCount = typedInput("How many Decks in Shoe?: ", int)
            self.shoe.generateDeck(deckCount)
            shuffleCount = typedInput("How many deck shuffles?: ", int)
            for _ in range(shuffleCount):
                self.shoe.shuffle()
        else:
            if ".json" not in initDeckFileName: initDeckFileName += ".json"
            with open(initDeckFileName, "r") as file:
                data = json.loads(file.read())
                self.shoe = Shoe()
                self.shoe.generateDeck(data["deckCount"])
                for _ in range(data["shuffleCount"]):
                    self.shoe.shuffle()

    def dealCards(self):
        for i in range(2):
            for p in self.players:
                c = self.shoe.draw()
                p.addCard(c)
                print("Player {} dealt {} Face Up.".format(p.name, c))
            c = self.shoe.draw()
            self.dealer.addCard(c)
            print("Dealer dealt {} Face {}.".format(c, "Down" if i == 0 else "Up"))
        
    def playerTurn(self, player):
        hit = True
        while hit:
            choice = player.choice()
            if choice:
                print("{} hits.".format(player.name))
                c = self.shoe.draw()
                print("{} is dealt {}".format(player.name, c))
                player.addCard(c)
                print("{}'s hand: {}".format(player.name, player.handString()))
            else:
                hit = False
                print("{} Stands with hand {}".format(player.name, player.handString()))
                print("{}'s hand value is: {}".format(player.name, player.getHighestHandValue()))
            if player.bust == True:
                hit = False
                print("{} busts with hand {}".format(player.name, player.handString()))
            


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
            dealerHandValue = self.dealer.getHighestHandValue()
            for p in self.players:
                if not p.bust:
                    playerHandValue = p.getHighestHandValue()
                    if playerHandValue > dealerHandValue:
                        print("{} wins the hand against the dealer!".format(p.name))
                    elif playerHandValue == dealerHandValue:
                        print("{} ties with the dealer.".format(p.name))
                    else:
                        print("{} loses to the dealer.".format(p.name))

        #Put all Hands back into discard pile
        for p in self.players:
            self.shoe.addToDiscard(p.clearHand())
        self.shoe.addToDiscard(self.dealer.clearHand())

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
