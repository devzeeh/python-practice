import json
from pathlib import Path

file_path = Path("students.json")

# Load on startup
if file_path.exists():
    with open(file_path, "r") as file:
        data = json.load(file)
else:
    data = []   # start empty if no file yet

# Modify in memory
data.append({"name": "ahye", "age": 20, "grade": 92})

# Save after every change
with open(file_path, "w") as file:
    json.dump(data, file, indent=4)