#Dictionaries With Loops
myDictionary = {"name" : "Ian", "health": 219, "strength": 199, "equipped": "Axe"}

for i in myDictionary:
  print(myDictionary[i])

print()
myDictionary = {"name" : "Ian", "health": 219, "strength": 199, "equipped": "Axe"}

for value in myDictionary.values():
  print(value)

print()
myDictionary = {"name" : "Ian", "health": 219, "strength": 199, "equipped": "Axe"}

for name,value in myDictionary.items():
  print(f"{name}:{value}")

print()
myDictionary = {"name" : "Ian", "health": 219, "strength": 199, "equipped": "Axe"}

for name,value in myDictionary.items():
  print(f"{name}:{value}")

  if (name == "strength"):
    print("Whoa, SO STRONG!")

print()
myDictionary = {"name" : "David the Mildy Terrifying", "health": 186, "strength": 4, "equipped":"l33t haxx0r p0werz"}

for name,value in myDictionary.items():
  print(f"{name}:{value}")

  if (name == "strength"):
    if value > 100:
      print("Whoa, SO STRONG")
    else:
      print("Looks like you skipped leg day, arm day, chest day and, well, gym day entirely bro!")

#day41 challenge
website = {"name": None, "url": None, "desc": None, "rating": None}

for name in website.keys():
  website[name] = input(f"{name}: ")

print()
for name, value in website.items():
  print(f"{name}: {value}")
