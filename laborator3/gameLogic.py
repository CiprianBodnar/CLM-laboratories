from nltk.corpus import wordnet
from nltk.corpus import words
import random
class Game:
   
    def __init__(self, numberOfLivers, word):
        self.numberOfLives = numberOfLivers
        self.word = word
        self.listOfDefinition = []

    def getWord(self):
        return self.word

    def getNumberOfLivers(self):
        return self.numberOfLives

 
    def __generateAllDefinitions(self, word):
        return wordnet.synsets(word)

    def __addAllDefinition(self):
        for definition in self.__generateAllDefinitions(self.word):
            self.listOfDefinition.append(definition.definition())

    def __generateDefinition(self):
        return self.listOfDefinition[(random.randrange(0, len(self.listOfDefinition)))]    
    
    def gameStart(self):
        print("###################GAME START####################")
        self.__addAllDefinition()
        while(self.numberOfLives>0):
            definition = self.__generateDefinition()
            print(definition)
            answer = input('Enter your input:')
            if(answer == self.word):
                print("You win!")
                self.numberOfLives = 0
            else:
                if self.numberOfLives==1:
                    print("Game Over! The word is:", self.word)
                    break
                else:
                    print("Wrong! Guess again! Here’s another hint:")
                    self.numberOfLives = self.numberOfLives -1
                    definition = self.__generateDefinition()



       
        
             
