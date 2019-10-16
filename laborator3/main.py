from gameLogic import Game
import random

def readAllWord(fileName):
    with open(fileName) as f:
        return [x.strip() for x in f.readlines()] 

def getUniqueWord(listOfWords):
    return listOfWords[(random.randrange(0, len(listOfWords)))]


if __name__ == "__main__":
    allWords =readAllWord("corpus.txt")

    myGame = Game(5, getUniqueWord(allWords))
    
    myGame.gameStart()
    