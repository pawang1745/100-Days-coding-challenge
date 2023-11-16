from flask import Flask, redirect

app = Flask(__name__, static_url_path='/static')


@app.route('/56')
def fiftySix():
  myName = "PAWAN"
  title = "Day 56 Solution"
  text = "So, day 56 was all about using csv reading and file and folder manipulation to make 100 files in dozens of folders. This was tricky because the names of the folders and files were based on the top 100 streaming songs and so weren't simple to encode."
  image = "56.png"
  link = "https://replit.com/@PAWANG/Day-056-Solution#main.py"

  page = ""
  f = open("template/portfolio.html", "r")
  page = f.read()
  f.close()
  page.replace("{name}", myName)
  page.replace("{title}", title)
  page.replace("{text}", text)
  page.replace("{image}", image)
  page.replace("{link}", link)
  return page
#redirecting
from flask import Flask, redirect

@app.route('/77')
def seventySeven():
  return redirect("https://replit.com/@PAWANG/Day-077-Solution#main.py")



#Day 77 challenge
from flask import Flask, redirect

app = Flask(__name__)


@app.route('/')
def index():
  
  page = ""
  return page
@app.route('/portfolio/hello')
def br():
  return redirect('/hello')
@app.route('/portfolio/bye')
def hr():
  return redirect('/bye')

@app.route('/hello')
def hello():
    title="Hello world"
    date="Nov 16th"
    text="Here is my first blog entry"

    page = ""
    f= open('templates/portfolio.html', 'r')
    page = f.read()
    f.close()
    page = page.replace("{{title}}", title)
    page = page.replace("{{date}}", date)
    page = page.replace("{{text}}", text)
    return page

@app.route('/bye')
def hello():
    title="bye world"
    date="Nov 16th"
    text="Here is my first blog entry"

    page = ""
    f= open('templates/portfolio.html', 'r')
    page = f.read()
    f.close()
    page = page.replace("{{title}}", title)
    page = page.replace("{{date}}", date)
    page = page.replace("{{text}}", text)
    return page
  
