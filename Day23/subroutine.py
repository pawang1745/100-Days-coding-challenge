def rollDice():
  import random
  dice = random.randint(1, 6)
  print("You rolled", dice)

for i in range(10):
  rollDice()

def myName():
  print("My Name is David")

myName()

def countToFive():
  for i in range(1, 6):
    print(i)

countToFive()

def  favoritecolor():
  print("My favorite color is red.")

favoritecolor()


# day23 challenge
def login():
    while True:
        username = input("What is your username?: ")
        password = input("What is your password? ")
        if username == "Rohit" and password == "4517":
            print("Welcome Rohit!")
            break
        else:
            print("That is not the correct username or password. Try again!")
            continue


print("College LOGIN SYSTEM")
login()
