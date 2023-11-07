import tkinter as tk

window = tk.Tk()
window.title("Hello World")
window.geometry("300x200")

labelOn = True

def hideLabel():
  global labelOn

  if labelOn: # if labelOn is Python shorthand for 'if labelOn == True'
    hello.pack_forget()
    labelOn = False
  else:
    button.pack_forget
    hello.pack()
    button.pack()
    labelOn = True

hello = tk.Label(text = "Hello World")
hello.pack()

button = tk.Button(text = "Click me!", command = hideLabel)
button.pack()

tk.mainloop()

import tkinter as tk
window = tk.Tk()
window.title("Hello World") 
window.geometry("300x200") 

def changeImage():
  canvas.itemconfig(container, image = newImage)
#### NEW SUBROUTINE ######
def hideImage():
  canvas.pack_forget()
hello = tk.Label(text = "Hello World") 
hello.pack() 
button = tk.Button(text = "Click me!", command=changeImage) 
button.pack()
#### NEW BUTTON ######
button2 = tk.Button(text = "Hide Image!", command=hideImage) 
button2.pack()
canvas = tk.Canvas(window, width = 300, height=150) 
canvas.pack()
image = tk.PhotoImage(file="messi.jpeg") 
image = image.subsample(5)
newImage = tk.PhotoImage(file="ronaldo.jpeg") 
newImage = newImage.subsample(5) 

container = canvas.create_image(150,1,image=image) 

tk.mainloop()

#Day68 challenge
import tkinter as tk
from PIL import Image, ImageTk
window = tk.Tk()
window.title("Guess Who?")
window.geometry("400x400")
label = "Guess Who?"
def showImage():
  person = text.get("1.0", "end")
  if person.lower().strip() == "mo":
    canvas.itemconfig(container, image=mo)
  elif person.lower().strip() == "charlotte":
    canvas.itemconfig(container, image=charlotte)
  elif person.lower().strip() == "gerald":
    canvas.itemconfig(container, image=gerald)
  elif person.lower().strip() == "katie":
    canvas.itemconfig(container, image=katie)
  else:
    canvas.pack_forget()
    warning.pack()
    return
  warning.pack_forget()
  canvas.pack()

hello = tk.Label(text=label)
hello.pack()
warning = tk.Label(text="Unable to find this user")
text = tk.Text(window, height=1, width=30)
text.pack()
button = tk.Button(text="Find", command=showImage)
button.pack()
canvas = tk.Canvas(window, width=400, height=380)

charlotte = ImageTk.PhotoImage(Image.open("guessWho/charlotte.jpg"))
gerald = ImageTk.PhotoImage(Image.open("guessWho/gerald.jpg"))
katie = ImageTk.PhotoImage(Image.open("guessWho/katie.jpg"))
mo = ImageTk.PhotoImage(Image.open("guessWho/mo.jpg"))
container = canvas.create_image(150,1,image=mo)

tk.mainloop()
