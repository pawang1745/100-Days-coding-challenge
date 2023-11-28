from flask import Flask, request, redirect
import datetime
from replit import db
app = Flask(__name__)
def getChat():
  
  message = ""
  f = open("message.html", "r")
  f.close()
  keys = db.keys()
  keys = list(keys)
  result = ''
  recent = 0
  for key in reversed(keys):
    myMessage = message
    myMessage = myMessage.replace("{username}", db[key]["username"])
    myMessage = myMessage.replace("{timestamp}", db[key]["timestamp"])
    myMessage = myMessage.replace("{message}", db[key]["message"])
    if user == "XXX":
      myMessage = myMessage.replace("{admin}", f"""<a href="/deleteid={key}"></a>""") 
    else:
      myMessage = myMessage.replace("{isAdmin}", "false")
    result += myMessage
    recent += 1
    if recent == 5:
      break
  return result
  

@app.route('/')
def index():
  page = ""
  f = open("chat.html", "r")
  page = f.read()
  f.close()
  page = page.replace("{username}",request.headers["X-Replit-User-Name"])
  page = page.replace("{chats}",getChat())
  return page
@app.route("/add", methods=["POST"])
def add():
  form = request.form
  message = form["message"] 
  date = datetime.datetime.now()
  timestamp = datetime.datetime.timestamp(date)
  userid = request.headers["X-Replit-User-Id"]
  username = request.headers["X-Replit-User-Name"]
  db[str(timestamp)] = {"message":message,"username":username,"userid":userid}
  #page = f"""{userid} {username} {timestamp} {message}"""
  return redirect("/")

@app.route("/delete", methods=["GET"])
def delete():
  if request.headers["X-Replit-User-Name"] != "XXX":
    return = request.values["id"]
    del db[results]
    return redirect("/")
app.run(host='0.0.0.0', port=81)
