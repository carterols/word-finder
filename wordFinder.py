import nltk
nltk.download('words')
from nltk.corpus import words
from timeit import default_timer as timer

dictionary = set(words.words())

def isEnglishWord(word):
    return word.lower() in dictionary

def recurCombination(text, currentString, i, textLen, combLen, wordsFound, wordsFoundIdx): 
    if combLen > textLen:
        return
    if combLen == 0 and isEnglishWord(currentString):
        wordsFound[wordsFoundIdx].add(currentString)
        # print("\t", currentString)
        return
    
    for j in range(i, textLen):
        recurCombination(text, currentString + text[j], j + 1, textLen, combLen - 1, wordsFound, wordsFoundIdx)

def main():
    text = input("Enter the letters: ")
    wordsFound = [set() for i in range(len(text))]
    MIN_WORD_SIZE = 2
    for i in range(MIN_WORD_SIZE, len(text)):
        recurCombination(text, "", 0, len(text), i, wordsFound, i - MIN_WORD_SIZE)
        
    i = MIN_WORD_SIZE
    for arr in wordsFound:
        if (len(arr) > 0):
            arr = sorted(arr)
            print("LENGTH " + str(i))
            for word in arr:
                print("\t", word)
        i += 1
if __name__ == "__main__":
    main()