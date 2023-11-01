#Day 62 challenge
#Building dairy
from replit import db
import datetime, os, time

def addEntry():

  timestamp = datetime.datetime.now()
  print(f"Diary entry for {timestamp}")
  print()
  entry = input("> ")
  db[timestamp] = entry

def viewEntry():
  keys = db.keys()
  for key in keys:

    print(f"""{key}
    {db[key]}""")
    print()
    opt = input("Next or exit? > ")
    if(opt.lower()[0]=="e"):
      break


password = input("Password: ")
if password != "codeforjoy":
  print("Incorrect")
  exit()
while True:
  menu = input("1: Add\n2: View\n> ")
  if menu == "1":
    addEntry()
  else:
    viewEntry()

