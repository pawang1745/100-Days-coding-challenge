#Day 100
#price scraper

from replit import db
import time
import requests,schedule,os,smtplib
from email.miime import MIMEMultipart
from email.mime.text import MIMEText
from bs4 import BeautifulSoup

def emailMe(level, price, link):
  password = os.environ['mailPassword']
  username = os.environ['mailUsername']
  host = "smtp.gmail.com"
  port = 587
  s = smtplib.SMTP(host = host, port = port)
  s.starttls()
  s.login(username, password)

  msg = MIMEMultipart()
  msg['To'] = "username"
  msg['From'] = username
  msg['Subject'] = "Price Drop Alert"
  text = f"""<p><a href='{link}'>This item</a> is now {level}</p>"""
  msg.attach(MIMEText(text, 'html'))
  s.send_message(msg)
  del msg


def addToDB():
  link = input("Link:")
  price = float(input("Price:"))
  db[time.time()] = {"link": link,"price":None,"level":500}

def update():
  keys = db.keys()
  for key in keys:
    url = db[key]["link"]
    price = db[key]["price"]
    level = db[key]["level"]
    response = requests.get(url)
    html = response.text
  
    soup = BeautifulSoup(html, "html.parser")
    myPrice = soup.find_all("span",{"class":"price"})
    thisprice = float(myPrice[0].text[1:]).replace(",","")
    
    if thisprice != price:
      db[key]["price"] = thisprice
      if thisprice <= level:
        print("Cheaper")
        emailMe(level, price, url)
    
schedule.every(1).minutes.do(update)

while True:
  schedule.run_pending()
  time.sleep(1)
