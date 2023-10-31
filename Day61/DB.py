# Storing Data
from replit import db

db["test"] = "Hello there"
keys = db.keys()
print(keys)

# Single key
value = db["test"]
print(value)

# Removing Data
del db["test"]
# Accessing By Prefix
db["login1"] = "ram"
db["login2"] = "jack"
db["login3"] = "hari"
db["login4"] = "rohit"

# Keys and Dictionaries
db["pawan"] = {"username": "pawan", "password": "hm45"}
keys = db.keys()
print(keys)
value = db["pawan"]
print(value["password"])

# Looping Access
keys = db.keys()
for key in keys:
    print(f"""{key}: {db[key]}""")

# Day 61 challenge

from replit import db
import datetime, os, time


def addTweet():
    tweet = input("🐥 > ")
    timestamp = datetime.datetime.now()
    key = f"mes{timestamp}"
    db[key] = tweet


def viewTweet():
    matches = db.prefix("mes")
    matches = matches[::-1]
    counter = 0
    for i in matches:
        print(db[i])
        print()

        counter += 1
        if (counter % 10 == 0):
            carryOn = input("Next 10?: ")
            if (carryOn.lower() == "no"):
                break


while True:
    print("Tweeter")
    menu = input("1: Add Tweet\n2: View Tweets\n> ")
    if menu == "1":
        addTweet()
    else:
        viewTweet()
