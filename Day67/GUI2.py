
import tkinter as tk

window = tk.Tk()
window.title("Hello World") 
window.geometry("300x200") 

def changeImage(): 
  canvas.itemconfig(container, image = newImage)

hello = tk.Label(text = "Hello World") 
hello.pack() 

button = tk.Button(text = "Click me!", command=changeImage) 
button.pack()


canvas = tk.Canvas(window, width = 300, height=150) 
canvas.pack()
image = tk.PhotoImage(file="img1.jpg") 
image = image.subsample(5)

newImage = tk.PhotoImage(file="img2.jpg") 
newImage = newImage.subsample(5) 

container = canvas.create_image(150,1,image=image)


tk.mainloop()

#Day67 challenge
import tkinter as tk
from PIL import Image, ImageTk

window = tk.Tk()
window.title("Guess Who?")
window.geometry("400x400")

label = "Guess Who?"

def showImage():
  person = text.get("1.0", "end")
  if person.lower().strip() == "ronaldo":
    canvas.itemconfig(container, image=ronaldo)
  elif person.lower().strip() == "virat kohli":
    canvas.itemconfig(container, image=virat kohli)
  elif person.lower().strip() == "messi":
    canvas.itemconfig(container, image=messi)
  elif person.lower().strip() == "sachin":
    canvas.itemconfig(container, image=sachin)
  else:
    hello["text"] = "Unable to find this user"

hello = tk.Label(text=label)
hello.pack()
text = tk.Text(window, height=1, width=30)
text.pack()
button = tk.Button(text="Find", command=showImage)
button.pack()
canvas = tk.Canvas(window, width=400, height=380)
canvas.pack()
viratkohli = ImageTk.PhotoImage(Image.open("virat kohli.jpg"))
messi = ImageTk.PhotoImage(Image.open("messi.jpeg"))
sachin = ImageTk.PhotoImage(Image.open("sachin.jpeg"))
ronalde = ImageTk.PhotoImage(Image.open("ronaldo.jpeg"))
container = canvas.create_image(150,1,image=mo)

tk.mainloop()
