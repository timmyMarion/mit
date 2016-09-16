import string

def isWordGuessed(secretWord, lettersGuessed):
    for x in secretWord:
        if x not in lettersGuessed:
            answer = False
            break
        else:
            answer = True
    return answer

def getGuessedWord(secretWord, lettersGuessed):
    answer = ""
    for x in secretWord:
        if x not in lettersGuessed:
            answer = answer + "_ "
        else:
            answer = answer + x
    return answer


def getAvailableLetters(lettersGuessed):
    answer = ""
    for x in string.ascii_lowercase:
        if x not in lettersGuessed:
            answer = answer + x
    return answer

secretWord = 'apple'
lettersGuessed = ['e', 'a', 'k', 'r', 'l', 's']

print(getAvailableLetters(lettersGuessed))

print(getGuessedWord(secretWord, lettersGuessed))

print(isWordGuessed(secretWord, lettersGuessed))

