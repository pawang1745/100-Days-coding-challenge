import schedule

def printMe():
  print("⏰")

schedule.every(2).seconds.do(printMe)

while True:
  schedule.run_pending()

print()
import schedule, time # Import the time library

def printMe():
  print("⏰")

schedule.every(2).seconds.do(printMe)

while True:
  schedule.run_pending()
  time.sleep(1)

print()
import schedule, time, os

password = os.environ['mailPassword']
username = os.environ['mailUsername']

def printMe():
  print("⏰")

schedule.every(2).seconds.do(printMe)

while True:
  schedule.run_pending()
  time.sleep(1)

#setup Email
import schedule, time, os, smtplib 
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText
password = os.environ['mailPassword']
username = os.environ['mailUsername']
def sendMail():
  email = "Don't forget to take a break!" 
  server = "smtp.gmail.com" 
  port = 587 
  s = smtplib.SMTP(host = server, port = port) 
  s.starttls() 
  s.login(username, password) 
  msg = MIMEMultipart() 
  msg['To'] = "recipient@email.com"  
  msg['From'] = username 
  msg['Subject'] = "Take a BREAK" 
  msg.attach(MIMEText(email, 'html')) 
  s.send_message(msg) 
  del msg 
sendMail()

def printMe():
  print("⏰")
schedule.every(2).seconds.do(printMe)
while True:
  schedule.run_pending()
  time.sleep(1)
