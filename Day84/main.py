from flask import Flask, request, redirect
from replit import db

app = Flask(__name__, static_url_path='/static')

users = {}
users["pawan"] = {"password" : "pk17"}
users["kumar"] = {"password" : "pk45"}


db["pawan"] = {"password" : "pk17"}
db["kumar"] = {"password" : "pk45"}
@app.route('/login', methods=["POST"])
def login():
  form = request.form

  try:
    if users[request.form["username"]]["password"]== request.form["password"]:
      return redirect("/yup")
    else:
      return redirect("/nope")
  except:
    return redirect("/nope")


@app.route("/nope")
def nope():
  return """<img src="static/nerdy.gif" height="100">"""

@app.route("/yup")
def yup():
  return """<img src="static/yup.gif" height="100">"""


@app.route('/')
def index():
  page = ""
  f = open("login.html", "r")
  page = f.read()
  f.close()
  return page


app.run(host='0.0.0.0', port=81)
