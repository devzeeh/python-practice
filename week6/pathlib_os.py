from pathlib import Path
import os

folder = Path("week6/contacts_data")
folder.mkdir(parents=True, exist_ok=True)   # creates the folder if it doesn't exist

file_path = folder / "contacts.json"        # the / operator joins paths cleanly
print(file_path)                             # weeklyproject/week6/contacts.json

print(os.listdir("."))          # lists all files/folders in the current directory
print(os.getcwd())               # prints the current working directory (where the script is running from)