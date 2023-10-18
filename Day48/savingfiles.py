#Creating A New File
f = open("savedFile.txt", "w")
print()

#Writing Data To The File
f = open("savedFile.txt", "w")
f.write("Hello there")
print()

#Close
f = open("savedFile.txt", "w")
f.write("Hello there")
f.close()
print()

#Saving to Files
f = open("savedFile.txt", "w")
whatText = input("> ")
f.write(whatText)
f.close()
print()

#Preventing Overwrite
f = open("savedFile.txt", "a+")
whatText = input("> ")
f.write(whatText)
f.close()
print()

#New Lines
f = open("savedFile.txt", "a+")
whatText = input("> ")
f.write(f"{whatText}\n")
f.close()
print()

f = open("savedFile.txt", "a+")
whatText = input("> ")
f.write(f"{whatText}\n")
f.close()
print()
#Day 48 challenge
#saving files


while True:
  print("HIGH SCORE TABLE")
  print()
  name = input("INITIALS > ").upper()
  score = input("SCORE > ")
  print()

  f = open("high.score", "a+")
  f.write(f"{name} {score}\n")
  f.close()

  print("ADDED")
