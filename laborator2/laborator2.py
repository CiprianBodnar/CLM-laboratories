from nltk.tokenize import word_tokenize, casual_tokenize
import re

corpusName = "corpus.txt"
startWithBigLettter = "^([A-Z])"
listOfAbrv = ["Mr", "Dr", "Lect"]
listOfName = ["a priori", "San Francisco"]
listOfHyphens = ["dati-i-l","dati-m-il","da-mi","s-a","i-am","mi-ai","l-ai","m-ai","m-a","te-a"]


def readCorpusFromFile(corpusName):
    file = open(corpusName,"r") 
    return file.read()

#Task 1
def tokenizeText(text):
    return casual_tokenize(text)

#Task 2
def checkIpAddresses(token):
    #Se verifica daca token-ul gasit este de forma unei adrese IP
    check = re.match(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$",token)
    if(check):
        return True
    return False

def concatIpAddress(listOfTokens):
    #Se verifica daca exista token-uri consecutive care pot forma o adresa IP, apoi se concateneaza
    # si se ia drept un singur token
    newList = []
    index = 0
    while index < len(listOfTokens) :
        if index < len(listOfTokens)-2 and (checkIpAddresses(listOfTokens[index] + listOfTokens[index + 1])):
            newList.append(listOfTokens[index] + listOfTokens[index + 1])
            index = index + 1
        else:
            if index < len(listOfTokens)-3 and (checkIpAddresses(listOfTokens[index] + listOfTokens[index + 1] + listOfTokens[index + 2])):
                newList.append(listOfTokens[index] + listOfTokens[index + 1] + listOfTokens[index + 2])
                index = index + 2
            else:
                newList.append(listOfTokens[index])
            index = index + 1
    return newList


#Task 3       
def checkStartWith(token):
    #Verificare daca incepe cu litera mare
    return re.match(startWithBigLettter, token) or token in listOfAbrv
  
def checkForAbreviation(listOfTokens, index):
    #Verificare daca exista abrevieri
    return checkStartWith(listOfTokens[index]) and listOfTokens[index+1] == '.' and checkStartWith(listOfTokens[index+2])

def concatNames(listOfTokens):
    #Daca sunt gasite abrevieri, se concateneaza cu urmatorul token daca acesta incepe cu o litera mare
    newList = []
    index = 0
    while index< len(listOfTokens):
        if index <=len(listOfTokens)-3 and checkForAbreviation(listOfTokens, index):
                newList.append(listOfTokens[index] + listOfTokens[index+1] + " "+ listOfTokens[index+2])
                index = index +2
        else:
            newList.append(listOfTokens[index])
        index = index +1
    return newList        


#Task 4
def checkPhoneNumber(listOfTokens):
    #Verifica daca exista token-uri consecutive care pot forma un numar de telefon si le concateneaza in unul singur
    newList = []
    index = 0
    while index < len(listOfTokens):
        if listOfTokens[index][-1] in ['-','/'] and listOfTokens[index + 1][0] in ['0','1','2','3','4','5','6','7','8','9']:
            newList.append(listOfTokens[index]+listOfTokens[index+1])
            index = index + 2
        else:
            newList.append(listOfTokens[index])
        index = index + 1
    return newList

def checkCompoundPhrases(listOfTokens):
    #Verifica daca exista token-uri care pot forma expresii sau substantive compuse si le concateneaza
    newList = []
    index = 0
    while index < len(listOfTokens)-1:
        if (listOfTokens[index]+" "+listOfTokens[index + 1]) in listOfName :
            newList.append(listOfTokens[index]+" "+listOfTokens[index + 1])
            index = index + 2
        else:
            newList.append(listOfTokens[index])
            index = index + 1
            if(len(listOfTokens) - index ==1):
                newList.append(listOfTokens[index])
    return newList


#Task 5
def checkHyphens(listOfTokens):
    newList = []
    index = 0
    while index< len(listOfTokens):
        if listOfTokens[index] in listOfHyphens:
            auxList = listOfTokens[index].split('-')
            for token in auxList:
                newList.append(token)
            index = index + 1
        else:
            newList.append(listOfTokens[index])
            index = index + 1
    return newList

#Task 6
def checkDespSilabe(listOfTokens):
    #Verifica daca exista cuvinte despartite in silabe, astfel uneste cele doua token-uri, eliminand cratima ce le desparte
    newList = []
    index = 0
    while index < len(listOfTokens) - 1:
        if listOfTokens[index + 1] == '-':
            newList.append(listOfTokens[index]+listOfTokens[index + 2])
            index = index + 2
        else:
            newList.append(listOfTokens[index])
            index = index + 1
            if(len(listOfTokens) - index ==1):
                newList.append(listOfTokens[index])
    return newList



####
def printList(listToPrint):
    for element in listToPrint:
        print(element)    

if __name__ == "__main__":
    
    listOfTokens = tokenizeText(readCorpusFromFile(corpusName))
    listOfTokens =checkDespSilabe(listOfTokens)
    listOfTokens = concatIpAddress(listOfTokens)
    listOfTokens = concatNames(listOfTokens)
    listOfTokens = checkPhoneNumber(listOfTokens)
    listOfTokens = checkCompoundPhrases(listOfTokens)
    listOfTokens = checkHyphens(listOfTokens)


    printList(listOfTokens)
