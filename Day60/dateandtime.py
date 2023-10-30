#datetime
import datetime

myDate = datetime.date(year=2022, month=12, day= 7)

print(myDate)
print()
#Asking For A Date
import datetime

today = datetime.date.today()

print(today)

print()
#Getting Date Input
import datetime

day = int(input("Day: "))
month = int(input("Month: "))
year = int(input("Year: "))

date = datetime.date(year, month, day)

print(date)

print()
#Delta Force
import datetime

today = datetime.date.today()

difference = datetime.timedelta(days=14)

newDate = today + difference

print(newDate)
print()
#If Statements With Dates
import datetime

today = datetime.date.today()

holiday = datetime.date(year = 2022, month = 10, day = 30) # The date of my holiday

if holiday > today:
  print("Coming soon")
elif holiday < today:
  print("Hope you enjoyed it")
else:
  print("HOLIDAY TIME!")

print()
#Day 60 Challenge
import datetime

today = datetime.date.today()

print("EVENT COUNTDOWN")
day = int(input("Day: "))
month = int(input("Month: "))
year = int(input("Year: "))
event = datetime.date(year, month, day)

difference = event - today
difference = difference.days

if difference>0:
  print(f"{difference} days to go")
elif difference<0:
  print(f" You missed it by {difference} days!")

else:
  print(" Today!")
