#Day 78 challenge
#Today's challenge is to build a place to store your reflections 
from flask import Flask

app = Flask(__name__)
myReflection = {}
myReflection["77"]={"link":"https://replit.com/@PAWANG/Day77100Days#main.py","Reflection":"I am happy to be here"}
myReflection["76"]={"link":"https://replit.com/@PAWANG/Day76100Days#main.py","Reflection":"I am happy to be here"}

@app.route('/<pageNumber>')

def index(pageNumber):
  page = ""
  f = open("template/reflection.html","r")
  page = f.read()
  f.close()

  reflection = myReflection[pageNumber]["Reflection"]
  print(reflection)
  page = page.replace("{day}",pageNumber)
  page = page.replace("{date}", myReflection[pageNumber]["link"])
  page = page.replace("{reflection",myReflection[pageNumber]["Reflection"])
  return page


