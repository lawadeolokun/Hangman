import random

# wordbank of random words to choose from
# (for now it is hardcoded but should be moved to file or API)

word_list = ('love', 'happy', 'football', 'basketball', 'sports', 'monumental', 'astronomical', 'onomatopoeia', 'inspirational', 'Ireland', 'Lawrence', 'Adeolokun')

# this function chooses a random word from the wordbank
def chooseWord():
    return random.choice(word_list)

# this functions displays the correct words guessed so far
def displayWord(word, guessedLetters):
    display = ''
    for letter in word:
        if letter in guessedLetters:
            display in letter + ''
        else:
            display += '_'
        return display.strip()