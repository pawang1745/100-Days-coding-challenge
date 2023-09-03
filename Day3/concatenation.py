#Concatenation
name = input("What is your name?: ")
sport = input("Which is your favourite sport?: ")

#joining all variables to be printed in same line 
print(name , "is going to play" , sport , "on sports day!")

#fixed the error
print("=== Your Song Generator ===")
print("""You'll be asked a bunch of questions
then we'll make you up an amazing
song, totally copyright free 😭""")
print()
person = input("Name a person famous for something good: ")
thing = input("Name a thing they did: ")
place = input("Name a place you like: ")
rhyme = input("Give me a verb that rhymes with your person's name: ")
print()
print("There was a person called", person)
print("Who did something cool like", thing, "at the wonderful", place ,"where you'll find me", rhyme)

#Day 3 challenge
food = input("Name of the food: ")
plant = input("Name a type of plant: ")
cooking = input("Name the methode of cooking: ")
description = input("What word describes burned food? ")
diy = input("Name a diy iteam: ")

print("Menu")
print(cooking , food , "with" , description , plant , "on bed of" , diy )
