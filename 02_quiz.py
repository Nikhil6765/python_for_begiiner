print("Welcome to the Animal Quiz")
score=0
def checkguess(guess,answer):
    global score
    Still_Guess=True
    i=0
    while i<3 and Still_Guess==True:
        if guess == answer:
            print("Correct Answer")
            score=score+1
            Still_Guess=False
        else:
            if i<2:
                guess=input("Sorry Wrong Answer, Please try again..")
            i=i+1


guess1=input("which bear lives in the north ?").lower()
checkguess(guess1,"polar bear")

guess2=input("Which is the fastest Land Animal ? ").lower()
checkguess(guess2,"cheetah")

guess3=input("Which is the Largest Animal ? ").lower()
checkguess(guess3,"blue whale")

print("Your Score is : ",score)
