#while loop
counter = 0
while counter < 10:
  print(counter)
  counter +=1
variable = 10
while variable >7:
  print(variable)
  variable-=1

exit = ""
while exit != "yes":
  print("🥳")
  exit = input("Exit?: ")

exit = "no"
while exit == "no":
    exit = input("do you want to exit?")
    if exit == "yes":
        print("thankyou!")
        break
    sound = input("what animal do you want?: ")

    if sound == "cow":
        print("moo")
    elif sound == "dog":
        print("wow..wow")
    elif sound == "cat":
        print("mew")
    else:
        print("cat or dog or cow!")
