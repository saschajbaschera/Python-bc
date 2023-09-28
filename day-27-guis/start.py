from tkinter import *

window = Tk()
window.title("My first GUI program")
window.minsize(width=500, height=300)
window.config(padx=50, pady=50)


def button_click():
    print("I got clicked")
    my_label.config(text=input.get())


# Label
my_label = Label(text="I'm a label", font=("Arial", 22, "bold"))
my_label.config(text="New Text")
my_label.grid(column=0, row=0)

# Button 1
button = Button(text="Click me", command=button_click)
button.grid(column=1, row=1)

# Button 2
button2 = Button(text="Another Button")
button2.grid(column=2, row=0)

# Entry (Same as Input)
input = Entry(width=30)
input.grid(column=3, row=2)



window.mainloop()


