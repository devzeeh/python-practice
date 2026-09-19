from pathlib import Path

file_path = Path("notes.txt")
print(file_path.exists())   # True or False — checks if the file exists before trying to open it

with open(file_path, "a") as file:
    file.write("\nIdols")
with open(file_path, "r") as files:
    content = files.read()
    print(content)