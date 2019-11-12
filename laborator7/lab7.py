import nltk

file = "myText.txt"

def tokenize_text(text):
    tokens = nltk.word_tokenize(text)
    return tokens

def read_from_file():
     with open(file, encoding="utf8") as fr:
         return (fr.readlines())

if __name__ == "__main__":
    text = ''.join(read_from_file())
    print(text)
    listOfTokens = tokenize_text(text)  
    print(listOfTokens)
    print(nltk.pos_tag(listOfTokens))