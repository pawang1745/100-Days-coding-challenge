while True:
  print("This program is running")
  goAgain = input("Go again?: ")
  if goAgain == "no":
    break
print("Aww, I was having a good time 😭")

counter = 0
while True:
  answer = int(input("Enter a number: "))
  print("Adding it up!")
  counter += answer
  print("Current total is", counter)
  addAnother = input("Add another? ")
  if addAnother == "no":
    break
print("Bye!")

#day16 challenge
print("Welcome to Name the Song Lyric")
print()
print("Figure out the missing word as quickly as you can!")
print()
counter = 1
while True:
  blank = input("Never going to ----- you up.")
  if blank != "give" :
    print("nope, try again.")
    counter +=1
  else:
    print("well done, It took",counter, "attempts")
    break
