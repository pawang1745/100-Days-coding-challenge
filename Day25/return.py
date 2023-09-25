def pinpicker(number):
  import random
  pin = ""
  for i in range(number):
    pin += str(random.randint(0,9))
  return pin
pinpicker(4)
mypin = pinpicker(4)
print(mypin)

def area_square(side1, side2):
  area = 0.5 * side1 * side2
  return area_square

area = area_square(4, 12)
print(area)

#day25 challenge
import random


def rollDice(sides):
  result = random.randint(1, sides)
  return result


def roll_6_and_8():
  roll_6_sided_dice = rollDice(6)
  roll_8_sided_dice = rollDice(8)
  health = roll_6_sided_dice * roll_8_sided_dice
  return health


print("⚔️Character stats generator⚔️")

haveACharacter = "yes"

while haveACharacter == "yes":
  character = input("Name your warrior: ")
  health = str(roll_6_and_8())
  print("Their health is ", health, "hp")
  haveACharacter = input("Want to create another character?")
