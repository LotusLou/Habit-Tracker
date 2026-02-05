import tkinter as tk

root = tk.Tk()
root.title("Mein Habit Tracker")

def update():
    root.after(1000, update)

frame = tk.Frame(root).pack()
label = tk.Label(frame, text="Hello World").pack()
root.geometry("400x300")

root.mainloop()
update()