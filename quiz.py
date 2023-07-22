print("Welcome to the Animal quiz")
score=0
def checkguess(guess,answer):
    global score
    if guess == answer:
        print("Correct Answer")
        score=score+1

guess1=input("which bear lives in the north ?")

checkguess(guess1,"polar bear")
print(score)
