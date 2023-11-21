from flask import Flask, request

app = Flask(__name__)


@app.route('/', methods=["GET"])
def index():
  get = request.args
  if get["name"].lower() == "david":
    return "Hello baldie"

app.run(host='0.0.0.0', port=81)

print()

#day 82 challenge
from flask import Flask

app = Flask(__name__)
@app.route('/language', methods=["GET"])
def lang():
  data = request.args
  if data == {}:
    return "Nothing here"
  if data["lang"]=="eng":
    return "Hello and welcome to my website"
  elif data["lang"]=="wel":
    return "Hello, a chroesa i'n gwefan y gwenyn"
  

@app.route('/')
def index():
  return 'Hello from Flask'

app.run(host='0.0.0.0', port=81)
