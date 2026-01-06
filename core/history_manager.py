import json
from datetime import datetime

def save_history(target, risk):
    entry = {
        "target": target,
        "risk": risk,
        "time": datetime.now().strftime("%Y-%m-%d %H:%M")
    }

    try:
        with open("history/scans.json", "r") as f:
            data = json.load(f)
    except:
        data = []

    data.append(entry)

    with open("history/scans.json", "w") as f:
        json.dump(data, f, indent=2)
