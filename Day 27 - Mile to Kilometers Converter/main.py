from tkinter import *

# Creating a new window and configurations
window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=150, height=100)
window.config(padx=10, pady=10)

# Entries
entry = Entry(width=10)
# Add some text to begin with
entry.insert(END, string="0")
entry.grid(row=0, column=1)

# Labels
miles = Label(text="Miles")
miles.grid(row=0, column=2)

# Labels
equal_to = Label(text="is equal to")
equal_to.grid(row=1, column=0)

# Labels
km = Label(text="Km")
km.grid(row=1, column=2)

# Labels
result = Label(text="0")
result.grid(row=1, column=1)


# Buttons
def action():
    to_km = int(entry.get()) * 1.609344
    result.config(text= to_km)


# calls action() when pressed
button = Button(text="Calculate", command=action)
button.grid(row=2, column=1)

window.mainloop()
