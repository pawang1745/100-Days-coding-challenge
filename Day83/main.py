#day 83 task
from flask import Flask, redirect, request
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
@app.route('/hello',methodes = [GET])
def hello():
    data = request.args
    template = "default"
    if data != {}:
        template = data['template']
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
    page = page.replace("{template}", template)
    return page

@app.route('/bye', methodes = [GET])
def bye():
    data = request.args
    template = "default"
    if data != {}:
      template = data['template']
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
    page = page.replace("{template}", template)
    return page
