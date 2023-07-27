import tkinter as tk

root = tk.Tk()

for row, text in enumerate(("Hello", "short", "All the buttons are not the same size", "Options", "Test2", "ABC", "This button is so much larger")):
    button = tk.Button(root, text=text)
    button.grid(row=row, column=0, sticky="ew")

root.mainloop()