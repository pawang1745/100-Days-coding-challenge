def whichCake(ingredient, base, coating):
  if ingredient == "chocolate":
    print("Mmm, chocolate cake is amazing")
  elif ingredient == "broccoli":
    print("You what mate?!")
  else:
    print("Yeah, that's great I suppose...")
  print("So you want a", ingredient, "cake on a", base, "base with", coating, "on top?")

userIngredient = input("Name an ingredient: ")
userBase = input("Name a type of base: ")
userCoating = input("Fave cake topping: ")
whichCake(userIngredient, userBase, userCoating)


def pizza_order(topping1, topping2):
    if topping1 == "pepperoni":
        print(topping1, "is a great choice")
    else:
        print(topping1, "is kinda lame on pizza")
    print(topping2, "sounds delicious, much better than", topping1)


topping1 = input("Name a pizza topping. ")
topping2 = input("Name a second pizza topping. ")

pizza_order(topping1, topping2)

import random

print("Infinity Dice 🎲")

sides = int(input("How many sides?: "))
playGame = "yes"


def rollDice(sides):
    print("You rolled ", random.randint(1, sides))


while playGame == "yes":
    rollDice(sides)
    playGame = input("Roll again?")
