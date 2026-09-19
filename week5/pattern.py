import json
from pathlib import Path

file_path = Path("data.json")

# 1. Load on startup
if file_path.exists():
    with open(file_path, "r") as file:
        data = json.load(file)
else:
    data = []   # start empty if no file yet

# 2. Modify in memory
data.append({"name": "New Entry"})

# 3. Save after every change
with open(file_path, "w") as file:
    json.dump(data, file, indent=4)