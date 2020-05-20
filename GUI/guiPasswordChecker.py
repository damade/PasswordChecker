import tkinter as tk
from tkinter import *

import CheckMyPassForGui as passwordCheckerModule


class App(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()


def printPasswordResult():  # The function that prints out the result of what is parsed
    inputForPassword = passwordInput.get()
    outputForPasswordChecker = passwordCheckerModule.main(inputForPassword)
    for output in outputForPasswordChecker:
        mylist.insert(END, str(output) + "\n")
    return


def clearTextField():  # It is the function that clears the entry and result list box
    passwordInput.delete(0, 'end')
    mylist.delete(0, 'end')
    return


# create the application frame though the root Tkinter Object
myapp = App()
top = Frame(myapp)
bottom = Frame(myapp)
listBottom = Frame(myapp)

# create the scrollbar for the app
scrollbar = Scrollbar(myapp)
scrollbar.pack(side="right", fill="y")

# create the scrollbar for the listbox
listScrollBar = Scrollbar(listBottom, orient="vertical")
listScrollBar.pack(side="right", fill="y")

# creating objects that would stack at the top part of the frame
top.pack()

# Create the label
passwordLabel = Label(top, text="Enter Password")
passwordLabel.pack(side="left", pady=(20, 0), padx=(4, 4))

# create the input or entry for data
passwordInput = Entry(top, bd=5, width=150)
passwordInput.pack(side="right", pady=(20, 0))

# creating objects that would stack at the middle part of the frame
bottom.pack()

# create the button for result
getResult = Button(bottom, text="Check Password", command=printPasswordResult, justify="center", width="15")
getResult.pack(side="left", pady=(20, 0), padx=(10, 40))

# create the button to clear screen
clearButton = Button(bottom, text="Clear", command=clearTextField, justify="center", width="15")
clearButton.pack(side="right", pady=(20, 0), padx=(30, 20))

##creating objects that would stack at the bottom part of the frame
listBottom.pack(side="bottom", fill="both")

# creating the output listbox for output
mylist = Listbox(listBottom)
mylist.config(yscrollcommand=listScrollBar.set)
mylist.pack(side="bottom", fill="both", padx=(10, 10), pady=(20, 10))
listScrollBar.config(command=mylist.yview)

# Gets the requested values of the height and widht.
windowWidth = myapp.winfo_reqwidth()
windowHeight = myapp.winfo_reqheight()

# Gets both half the screen width/height and window width/height
positionRight = int(myapp.winfo_screenwidth() / 2 - windowWidth / 2)
positionDown = int(myapp.winfo_screenheight() / 2 - windowHeight / 2)

if __name__ == "__main__":
    # here are method calls to the window manager class

    # Positions the window in the center of the page.
    myapp.master.geometry("+{}+{}".format(positionRight, positionDown))

    # it hides the maximize button on the window
    myapp.master.resizable(0, 0)

    # it sets title to the windows panel class
    myapp.master.title("PassWord Checker")

    # set the maximum dimension of the frame
    myapp.master.maxsize(400, 500)

    # stting the icon for the window frame
    myapp.master.iconphoto(False, tk.PhotoImage(file='iconPassword.png'))

    # start the program
    myapp.mainloop()
