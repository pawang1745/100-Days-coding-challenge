#List a file

import os

print(os.listdir())

files = os.listdir()
if "quickSave.txt" not in files:
  print("Error: Quick Save not found.")

#Create a folder
import os

os.mkdir("Hello")

#Renames a file
import os

os.rename("Inventory.txt", "inventory.txt")

#Day55 challenge
  # | Name | Date | Priority
import  os,random
todo = []
fileExists = True
try:
  f = open("to.do", "r")
  todo = eval(f.read())
  f.close()
except:
  fileExists = False

def add():
  name = input("Name > ")
  date = input("Due Date > ")
  priority = input("Priority > ").capitalize()
  row = [name, date, priority]
  todo.append(row)
  print("Added")

def view():
  options = input("1: All\n2: By Priority\n> ")
  if options=="1":
    for row in todo:
      for item in row:
        print(item, end=" | ")
      print()
    print()
  else:
    priority = input("What priority? > ").capitalize()
    for row in todo:
      if priority in row:
        for item in row:
          print(item, end=" | ")
        print()
    print()


def edit():
  find = input("Name of todo to edit > ")
  found = False
  for row in todo:
    if find in row:
      found = True
  if not found:
    print("Couldn't find that")
    return
  for row in todo:
    if find in row:
      todo.remove(row)
  name = input("Name > ")
  date = input("Due Date > ")
  priority = input("Priority > ").capitalize()
  row = [name, date, priority]
  todo.append(row)
  print("Added")

def remove():
  find = input("Name of todo to remove > ")
  for row in todo:
    if find in row:
      todo.remove(row)

while True:
  menu = input("1: Add\n2: View\n3: Edit\n4: Remove\n> ")
  if menu == "1":
    add()
  elif menu == "2":
    view()
  elif menu == "3":
    edit()
  else:
    remove()

  if fileExists:
    try:
      os.mkdir("backups")
    except:
      pass
    name = f"backup{random.randint(1,1000000000)}.txt"
    os.popen(f"cp to.do backups/{name}")


  f = open("to.do", "w")
  f.write(str(todo))
  f.close()
