print("Welcome to the Animal Quiz")
score=0
def checkguess(guess,answer):
    global score
    if guess == answer:
        print("Correct Answer")
        score=score+1

    

guess1=input("which bear lives in the north ?").lower()
checkguess(guess1,"polar bear")

guess2=input("Which is the fastest Land Animal ? ").lower()
checkguess(guess2,"cheetah")

guess3=input("Which is the Largest Animal ? ")
checkguess(guess3,"blue whale")

print("Your Score is : ",score)
