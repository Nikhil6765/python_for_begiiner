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
        index+=1        #index=index+1
        
while lives>0:
    print(clue)
    print('Lives left : '+heart_symbol*lives)
    guess=input("guess a letter or whole word :")

    if guess == secret_word:
        guessed_word_correctly=True
        break

    if guess in secret_word:
        update_clue(guess,secret_word,clue)

    else:
        print("Incorrect, You loose a life")
        lives-=1    #lives=lives-1

if guessed_word_correctly:     # it means guessd_word_correctlty == True :
    print("you Won! The secret word was " + secret_word)

else:
    print("you lost! The secret word was "+ secret_word)


