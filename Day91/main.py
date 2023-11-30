import requests, json

result = requests.get("https://icanhazdadjoke.com/", headers={"Accept":"application/json"})

joke = result.json()
print(json.dumps(joke, indent=2))

#Day 91 challenge
import requests
from replit import db

while True:
      result = requests.get("https://icanhazdadjoke.com/", headers={"Accept": "application/json"})
      joke = result.json()
      jk = joke["joke"]
      id = joke["id"]
      print(jk)
      answer = input("\n(s)ave joke, (l)oad old jokes, (n)ew joke\n>").lower()
      if answer == "n":
        continue
      elif answer == "s":
        db[id] = jk
        print("\nSAVED\n")
        continue
      else:
        keys = db.keys()
        for key in keys:
          result = requests.get(f"https://icanhazdadjoke.com/j/{key}", headers={"Accept": "application/json"})
          joke = result.json()
          print(joke["joke"])
          print(db[key])
          print("\n")
