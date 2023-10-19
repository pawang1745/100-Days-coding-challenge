#Open
f = open("filenames.list", "r")

#Read and Close
f = open("filenames.list", "r")
contents = f.read()
f.close()

#Print
f = open("filenames.list", "r")
contents = f.read()
f.close()

print(contents)

#Split
f = open("filenames.list", "r")
contents = f.read()
f.close()

contents = contents.split() 

print(contents)

#Repeat
f = open("filenames.list","r")
contents = f.readline().strip()
print(contents)
contents = f.readline().strip()
print(contents)
contents = f.readline().strip()
print(contents)
contents = f.readline().strip()
print(contents)

f.close()

#Just Use a Loop!
f = open("filenames.list","r")
while True:
  contents = f.readline().strip()

  if contents == "":
    break


  print(contents)

f.close()

#Day49 challenge

f = open("high.score", "r")
scores = f.read().split("\n")
f.close()

highscore = 0
name = None

for rows in scores:
  data = rows.split()
  if data != []:
    if int(data[1]) > highscore:
      highscore = int(data[1])
      name = data[0]

print("The winner is", name, "with", highscore)
