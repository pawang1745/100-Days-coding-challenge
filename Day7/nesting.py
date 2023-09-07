#Nesting
sport = input("What is your favorite sport? ")
if sport == "cricket":
  print("Wow! same here")
  favourite_team = input("which is your fouvrite team? ")
  if favourite_team == "India":
    print("True indian supporter")
  elif favourite_team == "australia":
    print("not bad")
  else:
    print("fake ")

else:
  print("Yeah, that's cool and all…")
  
#Day 7 challenge
print("Food ordering in nesting")
order = input("What would you like to order: pizza or hamburger? ")
if order == "hamburger":
  print("Thank you.")
  cheese = input("Do you want cheese?")
  if cheese == "yes":
    print("You got it.")
  else: 
    print("No cheese it is.")
elif order == "pizza":
  print("Pizza coming up.")
  toppings = input("Do you want pepperoni on that?")
  if toppings == "yes":
    print("We will add pepperoni.")
else:
  print("Your pizza will not have pepperoni.")
