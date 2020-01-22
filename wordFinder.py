from timeit import default_timer as timer
from itertools import permutations

MIN_WORD_SIZE = 2
words = set()

def isWord(word):
    return word in words

def getAllWords():
    with open('words.txt', 'r') as f:
        word = f.readline().rstrip().lower()
        while word:
            words.add(word)
            word = f.readline().rstrip().lower()

def permutation(text, n):
    return map(lambda x: ''.join(x), permutations(list(text), n))

def main():
    text = input("Enter the letters: ").strip().lower()
    getAllWords()
    wordsFound = []

    for i in range(MIN_WORD_SIZE, len(text) + 1):
        wordsFound.append([])
        strPerms = set(permutation(text, i))
        for word in strPerms:
            if word in words:
                wordsFound[i - MIN_WORD_SIZE].append(word)
    
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