import tkinter as tk

window = tk.Tk()
window.title("Memory Card Game")
window.geometry("500x500")

# Distributing space eveny between each row and each column
for i in range(4):
    window.grid_columnconfigure(i, weight = 1)
for i in range(4):
    window.grid_rowconfigure(i, weight = 1)

# Board Window
for row in range(4):
    for column in range(4):
        button = tk.Button(window, text="?")
        button.grid(row=row, column=column, padx = 5, pady = 5, sticky = "nsew")

window.mainloop()