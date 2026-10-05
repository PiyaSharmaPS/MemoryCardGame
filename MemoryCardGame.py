import tkinter as tk
import random as rd

# Variables
cards = ["🍎", "🍌", "🍇", "🍒", "🍉", "🍓", "🥝", "🍍"]*2
# Shuffled card list
rd.shuffle(cards)
first_card = None
second_card = None
first_button = None
second_button = None
matched_cards = set()
moves=0
busy = False
hide_job = None
buttons=[]

window = tk.Tk()
window.title("Memory Card Game")
window.geometry("500x500")

# Distributing space eveny between each row and each column
for i in range(4):
    window.grid_columnconfigure(i, weight = 1)
for i in range(7):
    window.grid_rowconfigure(i, weight = 1)

def reset_game():
    global hide_job, busy, first_card, second_card, first_button, second_button, moves
    
    if(hide_job != None):
        window.after_cancel(hide_job)
        hide_job=None

    first_card = None
    second_card = None
    first_button = None
    second_button = None
    moves = 0
    busy = False
    matched_cards.clear()

    rd.shuffle(cards)
    for button in buttons:
        button.config(text = "?")
    moves_label.config(text = "Moves: 0")
    win_label.config(text = "")

# Title label
title_label = tk.Label(window, text = "----Memory Card Game----", font = ("Arial", 20, "bold"))
title_label.grid(row = 0, column = 0, columnspan = 4)

# Moves label
moves_label = tk.Label(window, text = "Moves: 0", font = ("Arial", 16))
moves_label.grid(row = 1, column = 0, columnspan = 2)

# Reset button
reset_button = tk.Button(window, text = "Reset", font = ("Arial", 14, "bold"), relief = "raised" , borderwidth = 2, command=reset_game)
reset_button.grid(row = 1, column = 2, columnspan = 2)

# Win label
win_label = tk.Label(window, text = "", font = ("Arial", 16, "bold"))
win_label.grid(row =6, column = 0, columnspan = 4)

def hide_cards():
    global busy, hide_job, first_card, second_card, first_button, second_button

    if(first_button != None and second_button != None):
        first_button.config(text = "?")
        second_button.config(text = "?")

    first_card = None
    second_card = None
    first_button = None
    second_button = None
    busy = False
    hide_job = None  

def card_clicked(index, button):
    global hide_job, busy, first_card, second_card, first_button, second_button, moves

    if busy:
        return

    # Returns when an already matched card is clicked
    if index in matched_cards:
        return

    # First Card
    if(first_card == None):
        first_card = index
        first_button = button
        button.config(text=cards[index])

    # Second Card
    else:
        second_card = index
        second_button = button
        button.config(text=cards[index])

        # Same card clicked twice
        if(first_card == second_card):
            busy = True
            hide_job = window.after(1000, hide_cards)
            return

        moves+=1
        moves_label.config(text = f"Moves: {moves}")


        # Matched Pair
        if(cards[first_card] == cards[second_card]):
            matched_cards.add(first_card)
            matched_cards.add(second_card)

            # Winning Condition
            if(len(matched_cards) == 16):
                win_label.config(text = "You Won!")

            first_card = None
            second_card = None
            first_button = None
            second_button = None
        
        # Non-matching pair
        else:
            busy = True
            hide_job = window.after(1000, hide_cards)

# Board Window
for row in range(4):
    for column in range(4):
        index = row*4+column
        button = tk.Button(window, text="?")
        buttons.append(button)
        button.config(command= lambda i=index, b=button: card_clicked(i,b), font = ("Arial", 28), relief = "solid", borderwidth = 2)
        button.grid(row=row+2, column=column, padx = 5, pady = 5, sticky = "nsew")
    
window.mainloop()