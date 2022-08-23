from tkinter import *

class MyAwesomePythonApp:

    def __init__(self):
        self.root = self.initRoot()
        print(self.root)

    def initRoot(self):
        root = Tk()
        root.title("My awesome python app :)")
        root.geometry("720x480")
        root.maxsize(1280, 720)
        self.label = self.addLabel(root, "Hello World")
        self.text = StringVar()
        self.entry = self.addEntry(root, self.text)
        self.addButton(root, "Change title", self.handleClick)
        root.mainloop()
        return root

    def handleClick(self):
        title = self.entry.get()
        self.label.configure(text=title)

    def addButton(self, root, text, command):
        button = Button(root, text=text, command=command)
        button.pack()
        button.configure(font=("Arial", 24))
        return button

    def addEntry(self, root, text):
        entry = Entry(root, textvariable=text)
        entry.pack()
        entry.configure(font=("Courier", 36))
        return entry

    def addLabel(self, root, text):
        label = Label(root, text=text)
        label.pack()
        label.configure(font=("Courier", 36)) 
        return label   