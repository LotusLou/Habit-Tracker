import tkinter as tk
import datetime
#.\\venv\Scripts\Activate.ps1

#Root Settings
root = tk.Tk()
root.title("Mein Habit Tracker")
root.geometry("400x300")
root.minsize(450, 350)
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight= 0)
root.rowconfigure(1, weight= 0)
root.rowconfigure(2, weight= 1)

def update():
    root.after(1000, update)
colors = {
    "Text" : "#04080F",
    "Primary Action" : "#507DBC",
    "Header-Bar" : "#A1C6EA",
    "Card/Panel" : "#BBD1EA",
    "App-Background" : "#DAE3E5",
}
#window
root.config(bg= colors["App-Background"])

#Header
header = tk.Frame(root, bg=colors["Header-Bar"])
header.grid(row= 0, column= 0, sticky= "ew" )
label = tk.Label(header, text="Tracker", bg=colors["Header-Bar"])
label.pack()

#Date-bar
date_bar = tk.Frame(root)
date_bar.grid(row= 1, column= 0, sticky= "ew" )
tracker_date = tk.Label(date_bar, text= str(datetime.datetime.today()).split()[0])
tracker_date.pack(fill="x")
#Content
content = tk.Frame(root)
content.grid(row= 2, column= 0, sticky= "nsew")

habits = ["Journaling", "2", "3", "4"]

for i, habit in enumerate(habits):
    card = tk.Frame(content, bg= colors["Card/Panel"])
    card.grid(row= i // 2 , column= i % 2, sticky="nsew")
    habit_titel = tk.Label(card, text= habit , bg= colors["Card/Panel"])
    habit_titel.grid(column= 0, row= 0, sticky= "ew")

root.mainloop()
update()