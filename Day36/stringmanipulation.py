#String Manipulation
name = input("What's your name? ")
if name.upper().strip() == "PAWAN": 
  print("Hello buddy!")
else: 
  print("What a beautiful name!")

#No Duplicates
myList = []

def printList():
  print()
  for i in myList:
    print(i)
  print()

while True:
  addItem = input("Item > ").capitalize().strip()
  if addItem not in myList:
    myList.append(addItem)
  printList()

#error fix
whatToEat = input("What do you have for dinner? ")
if whatToEat.strip == "pasta": 
  print("Get out the pasta maker.")
elif whatToEat.lower() == "chappati":
  print("Let's do chappati Tuesday!")
else: 
  print("Go search the fridge.")

#day36 challenge
rolodex = []

def printList():
  print()
  for name in rolodex:
    print(name)
  print()

while True:
  firstName = input("First Name: ").strip().capitalize()
  lastName = input("Last Name: ").strip().capitalize()
  name = f"{firstName} {lastName}"
  if name not in rolodex:
    rolodex.append(name)
  else:
    print("ERROR: Duplicate name")
  printList()
