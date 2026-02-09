import json

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


data= load_state()
print(data)