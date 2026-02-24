import json
import tkinter as tk
dateiname = "habits.json"
default_state = { "habits" : [
            {
                "id": "h1",
                "name": "Journaling",
                "entries" : {}
                
            },
            {
                "id": "h2",
                "name": "Streching",
                "entries" : {}
            },
            {
                "id": "h3",
                "name": "Sublements",
                "entries" : {}
            },
            {
                "id": "h4",
                "name": "No Socialmedia",
                "entries" : {}
            }
        ]
        }

def load_state():
    try:
        with open(dateiname, "r", encoding="utf-8") as f:
            daten= json.load(f)
        
    except FileNotFoundError:
        print(f"Fehler: Laden der Json hat nicht Funktioniert weil das File nicht gefunden wurde oder Kaputt ist. Standart Json wird geladen.")
        daten = default_state
    return daten

def save_state(state):
    try: 
        with open(dateiname, "w", encoding="utf-8") as f:
            json.dump(state, f , indent= 4, ensure_ascii=False)
        with open(dateiname, "r") as f:
            print(f.read())
    except OSError:
        print("Fehler: Beim Speichern der neuen Daten. Zugang wurde Verweigert")

def show_existing_Habits(daten):
    habits = []
    ids = []
    for i, habit in enumerate(daten["habits"]):
        habit_name = habit["name"]
        habits.append(habit_name)
        dic_id = habit["id"]
        ids.append(dic_id)
    return habits, ids

def find_habit_obj(id, state):
    for habit in state["habits"]:
        if id == habit["id"]:
            return habit
            break

def close_Handler (state, root):
    try:
        save_state(state)
    except:
        print("Fehler beim Speichern des State")
    root.destroy()
