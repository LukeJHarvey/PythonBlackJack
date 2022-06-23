import sys
from Game.BlackJack import BlackJack
if __name__ == '__main__':
    argCount = len(sys.argv)
    playerFileName = sys.argv[1] if argCount >= 2 else ""
    deckFileName = sys.argv[2] if argCount >= 3 else ""
    bjGame = BlackJack(playerFileName, deckFileName)