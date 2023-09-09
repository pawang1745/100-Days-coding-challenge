#casting
myScore = int(input("Your score: "))
if myScore > 100000:
  print("Winner!")
else:
  print("Try again 😭")

score = int(input("What was your score on the test?"))
if score >= 80:
  print("Not too shabby")
elif score > 70:
  print("Acceptable.")
else:
  print("Dude, you need to study more!")

#day 9 challenge
print("Generation Identifier")
print("~~~~~~~~~~~~~~~~~~~~~~")
birthyear = int(input("what is your age? "))
if birthyear <=1946:
  print("you are a traditionalist.")
elif birthyear <= 1964:
  print("Hey , baby boomer! How are you?")
elif birthyear >= 1965 and birthyear <= 1981:
  print("Gen X! what's up?")
elif birthyear >= 1982 and birthyear <= 1995:
  print("Millenials! The age of tech!")
elif birthyear >=1996:
  print("Hey, Gen Z! Insta much?")
else:
  print("Try again!")
