import random 
import string

nouns = ["cat", "dog", "book", "computer", "sun", "tree", "ocean", "mountain", "flower", "car", "house", "cup", "pizza", "pencil", "phone"]
adjectives = ["happy", "beautiful", "clever", "mysterious", "brave", "vibrant", "peaceful", "energetic", "graceful", "adorable", "gloomy", "playful", "elegant", "delicious", "thoughtful"]

another_PASSWORD=True

while another_PASSWORD==True:

    noun=random.choice(nouns)
    adjective=random.choice(adjectives)
    number=random.randrange(1,100)
    special_character=random.choice(string.punctuation)

    password=noun+adjective+special_character+str(number)

    print("Your Password is...",password)

    option=input("Do you want another password ? (YES/NO)")

    if option.lower()== "yes":
        print("Your Password is...",password)

    else:
        break




    
    
    
      