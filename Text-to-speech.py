from tkinter import *
import pyttsx3

root = Tk()

root.title("Text to Speech")
root.geometry("500x200")
root.resizable(False,False)

def talk():
    engine = pyttsx3.init()
    engine.say(myEntry.get())
    engine.runAndWait()
    myEntry.delete(0,END)
myTitle = Label(root, text="My Epic Text to Speech", font=("Arial", 30))
myTitle.pack(pady=20)
myEntry = Entry(root, font=("Arial", 28))
myEntry.pack(pady=10)

myButton = Button(root, text="Speak", command=talk)
myButton.pack(pady=5)

root.mainloop()
