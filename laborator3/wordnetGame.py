from nltk.corpus import wordnet
from nltk.corpus import words
from random import sample

def generateRandomWOrd():
   return ' '.join(sample(words.words(), 1))
  
def getAllDefinitions(word):
    return wordnet.synsets(word)

if __name__ == "__main__":
    print("Start the game")
    word = generateRandomWOrd()
    numberOfLives = 3
    print(word)
    flag = False

    for definition in getAllDefinitions(word):
        print(definition.definition())
        while(numberOfLives>0 or flag==False):
            answer = input('Enter your input:')
            if(answer==word):
                print("You win!")
                flag = True
            else:
                numberOfLives -= 1
                print("You lost a live!")
                print(numberOfLives )
            if numberOfLives==0:
                print("You lost!")


   # for definition in getAllDefinitions(word):
    #    print (definition.definition())
    #print(getAllDefinitions(word))



#syns = wordnet.synsets("program")

#print(syns[0].definition())