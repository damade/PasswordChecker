import tkinter as tk
from tkinter import *
import CheckMyPassForGui as passwordCheckerModule;


class App(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()


def printPasswordResult():
    inputForPassword = passwordInput.get()
    outputForPasswordChecker = passwordCheckerModule.main(inputForPassword)
    for output in outputForPasswordChecker:
        mylist.insert(END,str(output)+"\n")
    return

def clearTextField():
    passwordInput.delete(0,'end')
    mylist.delete(0,'end')
    return

def showPassword():
    passwordInput.show
# create the application
myapp = App()
top = Frame(myapp)
bottom = Frame(myapp)
listBottom = Frame(myapp)
# passwordChecker = CheckMyPassForGui()

scrollbar = Scrollbar(myapp)
scrollbar.pack(side="right", fill="y")

listScrollBar = Scrollbar(listBottom,orient="vertical")
listScrollBar.pack(side="right",fill="y")

top.pack()
passwordLabel = Label(top, text="Enter Password")
passwordLabel.pack(side="left", pady=(20, 0), padx=(4, 4))

passwordInput = Entry(top, bd=5, width=150)
passwordInput.pack(side="right", pady=(20, 0))

#showButton = Button(top,text="show",command= showPassword)
# here are method calls to the window manager class'''


bottom.pack()
getResult = Button(bottom, text="Check Password", command=printPasswordResult, justify="center", width="15")
getResult.pack(side="left", pady=(20, 0), padx=(10,40))

clearButton = Button(bottom, text="Clear",command= clearTextField,justify="center",width="15")
clearButton.pack(side="right", pady=(20, 0), padx=(30,20))



listBottom.pack(side="bottom", fill="both")
mylist = Listbox(listBottom)
mylist.config( yscrollcommand=listScrollBar.set)
mylist.pack(side="bottom", fill="both", padx=(10, 10), pady=(20, 10))
listScrollBar.config(command=mylist.yview)




# Gets the requested values of the height and widht.
windowWidth = myapp.winfo_reqwidth()
windowHeight = myapp.winfo_reqheight()

# Gets both half the screen width/height and window width/height
positionRight = int(myapp.winfo_screenwidth() / 2 - windowWidth / 2)
positionDown = int(myapp.winfo_screenheight() / 2 - windowHeight / 2)

# Positions the window in the center of the page.
myapp.master.geometry("+{}+{}".format(positionRight, positionDown))
myapp.master.resizable(0,0)
myapp.master.title("PassWord Checker")
myapp.master.maxsize(400, 500)
myapp.master.iconphoto(False,tk.PhotoImage(file='iconPassword.png'))
# start the program
myapp.mainloop()
