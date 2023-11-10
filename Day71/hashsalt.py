#Hashing
password = "66pawan"
password = hash(password)
print(password)

from replit import db

userName = "PAWAN"
password = "66pawan"
password = hash(password)
db[userName] = password 

print(password)

from replit import db

print(db["PAWAN"])

from replit import db

ask = input("Password >") 
ask = hash(ask) 

if ask == db["PAWAN"]: 
  print("Login successful") 
from replit import db
password = "66pawan"
salt = 10221
newPassword = f"{password}{salt}" 
newPassword = hash(newPassword) 
print(newPassword)
print()

#Second User
from replit import db
password = "66pawan"
salt = 10221
newPassword = f"{password}{salt}"
newPassword = hash(newPassword)
print(newPassword)
print()

password = "66pawan"
salt = 39820
newPassword = f"{password}{salt}"
newPassword = hash(newPassword)
print(newPassword)
print()

from replit import db
password = "66pawan"
salt = 10221
newPassword = f"{password}{salt}"
newPassword = hash(newPassword)
print(newPassword)
db["PAWAN"] = {"password":newPassword, "salt": salt}
print()

from replit import db
ans = input("Password >") 
salt = db["PAWAN"]["salt"] 
newPassword = f"{ans}{salt}"
newPassword = hash(newPassword) 
if newPassword == db["PAWAN"]["password"]: 
  print("Login successful")
#Day 71 challenge
#LOGIN system
import os, random
from replit import db
def createUser():
  username = input("Username: ")
  password = input("Password: ")
  keys = db.keys()
  if username in keys:
    print("ERROR: Username exists")
    return
  salt = random.randint(1000, 9999)
  newPassword = f"{password}{salt}"
  newPassword = hash(newPassword)

  db[username] = {"password": newPassword, "salt": salt}

  print("User added")
def login():
  username = input("Username: ")
  password = input("Password: ")
  keys = db.keys()
  if username not in keys:
    print("ERROR: Username does not exists")
    return
  salt = db[username]["salt"]
  newPassword = f"{password}{salt}"
  newPassword = hash(newPassword)

  if db[username]["password"]==newPassword:
    print("Logged in")
  else:
    print("Username or password incorrect")
while True:
  menu = input("1: New User\n2: Login\n> ")
  if menu == "1":
    createUser()
  elif menu == "2":
    login()
  else:
    keys = db.keys()
    for key in keys:
      print(db[key])
