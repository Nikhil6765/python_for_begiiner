import random 
import string

nouns = ["cat", "dog", "book", "computer", "sun", "tree", "ocean", "mountain", "flower", "car", "house", "cup", "pizza", "pencil", "phone"]
adjectives = ["happy", "beautiful", "clever", "mysterious", "brave", "vibrant", "peaceful", "energetic", "graceful", "adorable", "gloomy", "playful", "elegant", "delicious", "thoughtful"]

noun=random.choice(nouns)
adjective=random.choice(adjectives)
number=random.randrange(1,100)
special_character=random.choice(string.punctuation)

print("Your Password is...",noun+adjective+special_character+str(number))
      