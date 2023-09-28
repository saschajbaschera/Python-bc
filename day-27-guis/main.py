from tkinter import *

window = Tk()
window.minsize(width=200, height=100)
window.title("Mile to Km Converter")
window.config(pady=30, padx=30)


#Calculate function
def calculate():
    km = round(float(input.get()) * 1.609)
    km_value.config(text=f"{km}")

# Input Miles
input = Entry(width=7)
input.insert(END, string="0")
input.grid(column=1, row=0)

# Miles Label
miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)
miles_label.config(anchor="w")

# is equal label
equal_label = Label(text="is equal to")
equal_label.grid(column=0, row=1)
equal_label.config(anchor="e")

# Calculated km value
km_value = Label(text="0")
km_value.grid(column=1, row=1)

# Km label
km_label = Label(text="Km")
km_label.grid(column=2, row=1)
km_label.config(anchor="w")

#Calculate Button
calc_button = Button(text="Calculate", command=calculate)
calc_button.grid(column=1, row=2)


window.mainloop()

