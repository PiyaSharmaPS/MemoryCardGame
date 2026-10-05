import tkinter as tk
import random as rd

# Variables
cards = ["🍎", "🍌", "🍇", "🍒", "🍉", "🍓", "🥝", "🍍"]*2
# Shuffled card list
rd.shuffle(cards)

first_card = None

window = tk.Tk()
window.title("Memory Card Game")
window.geometry("500x500")

# Distributing space eveny between each row and each column
for i in range(4):
    window.grid_columnconfigure(i, weight = 1)
for i in range(4):
    window.grid_rowconfigure(i, weight = 1)


def card_clicked(index, button):
    global first_card

    # First Card
    if(first_card == None):
        first_card = index
        button.config(text=cards[index])

    # Second Card
    else:
        button.config(text=cards[index])


# Board Window
for row in range(4):
    for column in range(4):
        index = row*4+column
        button = tk.Button(window, text="?")
        button.config(command= lambda i=index, b=button: card_clicked(i,b))
        button.grid(row=row, column=column, padx = 5, pady = 5, sticky = "nsew")


window.mainloop()