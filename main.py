import tkinter as tk
import datetime
from app import *
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

colors = {
    "Text" : "#04080F",
    "Primary Action" : "#507DBC",
    "Header-Bar" : "#A1C6EA",
    "Card/Panel" : "#BBD1EA",
    "App-Background" : "#DAE3E5",
}
t = str(datetime.datetime.today()).split()[0]
#window
root.config(bg= colors["App-Background"])

#Header
header = tk.Frame(root, bg=colors["Header-Bar"])
header.grid(row= 0, column= 0, sticky= "ew" )
label = tk.Label(header, text="Tracker", bg=colors["Header-Bar"])
label.pack()

#Date-bar
date_bar = tk.Frame(root, bg=colors["App-Background"])
date_bar.grid(row= 1, column= 0, sticky= "ew" )
date_bar.columnconfigure(0, weight= 1)
date_bar.rowconfigure(0, weight= 1)
tracker_date = tk.Label(date_bar, text= t, bg= colors["App-Background"])
tracker_date.columnconfigure(0, weight= 1)
tracker_date.rowconfigure(0, weight= 1)
tracker_date.grid(row=0, column= 0, sticky= "nsew", pady=5)
#Content
content = tk.Frame(root, bg=colors["App-Background"])
content.grid(row= 2, column= 0, sticky= "nsew", padx= 10, pady= 10)
content.columnconfigure(1, weight= 1)
content.columnconfigure(0, weight= 1)
content.rowconfigure(0, weight= 1)
content.rowconfigure(1, weight= 1)

state = load_state()
habits, ids = show_existing_Habits(state)
# Created the Habits

def on_button_toggle(var, habit_name, id):
    for i ,habit in enumerate(state['habits']):
        if id == habit["id"]:
            if var.get( ) == True:
                state["habits"][i]["entries"].update({t : True})
                n = state["habits"][i]["entries"]
                print(f"Update: {habit_name} done")
                print(f"Json: {n}")
            else:
                state["habits"][i]["entries"].update({t : False})
                print(f"Update: {habit_name} undone")



for i, habit in enumerate(habits):
    card = tk.Frame(content, bg= colors["Card/Panel"])
    card.grid(row= i // 2 , column= i % 2, sticky="nsew", padx= 5, pady= 5)
    card.columnconfigure(0, weight= 1)
    card.rowconfigure(1, weight= 1)
    habit_titel = tk.Label(card, text= habit , bg= colors["Card/Panel"], anchor="center")
    var = tk.BooleanVar()
    check_box = tk.Checkbutton(card, bg= colors["Card/Panel"], variable=var, onvalue=True, offvalue= False, command= lambda v=var, h=habit, id = ids[i]: on_button_toggle(v, h, id))
    habit_titel.grid(column= 0, row= 0, sticky= "ew")
    check_box.grid(column= 0, row= 1, sticky= "ns")

root.mainloop()