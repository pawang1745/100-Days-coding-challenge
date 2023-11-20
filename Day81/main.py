from flask import Flask, request

app = Flask(__name__)

@app.route("/robot", methods=["POST"])
def robot():
  form = request.form
  if form['metal']=="yes":
    return "You are a robot!"
  elif "error" in form['infinity'].lower():
    return "You are a robot!"
  elif form['food']=="synthetic oil":
    return "You are a robot!"
  else:
    return "Hi there fellow human"
  

@app.route('/')
def index():
  page = ""
  f = open("form.html","r")
  page = f.read()
  f.close()
  return page
    

app.run(host= '0.0.0.0', port= 81)
