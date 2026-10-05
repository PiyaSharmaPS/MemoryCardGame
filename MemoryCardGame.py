import tkinter as tk
import random as rd

# Variables
cards = ["🍎", "🍌", "🍇", "🍒", "🍉", "🍓", "🥝", "🍍"]*2
# Shuffled card list
rd.shuffle(cards)

first_card = None
second_card = None
matched_cards = set()

window = tk.Tk()
window.title("Memory Card Game")
window.geometry("500x500")

# Distributing space eveny between each row and each column
for i in range(4):
    window.grid_columnconfigure(i, weight = 1)
for i in range(4):
    window.grid_rowconfigure(i, weight = 1)


def card_clicked(index, button):
    global first_card, second_card

    # Returns when an already matched card is clicked
    if index in matched_cards:
        return

    # First Card
    if(first_card == None):
        first_card = index
        button.config(text=cards[index])

    # Second Card
    else:
        second_card = index
        button.config(text=cards[index])

        # Same card clicked twice
        if(first_card == second_card):
            return

        # Matched Pair
        if(cards[first_card] == cards[second_card]):
            matched_cards.add(first_card)
            matched_cards.add(second_card)

            first_card = None
            second_card = None


# Board Window
for row in range(4):
    for column in range(4):
        index = row*4+column
        button = tk.Button(window, text="?")
        button.config(command= lambda i=index, b=button: card_clicked(i,b))
        button.grid(row=row, column=column, padx = 5, pady = 5, sticky = "nsew")


window.mainloop()