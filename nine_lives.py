import random

lives=9
words=['pizza','fairy','teeth','shirt','otter','plane']

secret_word=random.choice(words)
clue=list('?????')

heart_symbol=u'\u2764'

guessed_word_correctly=False

def update_clue(guessed_letter,secret_word,clue):
    index=0
    while index <len(secret_word):
        if guessed_letter==secret_word[index]:
            clue[index]=guessed_letter
        index+=1
        