import json

students = [
    {"name": "Rei", "age": 20, "grade": 88},
    {"name": "Won", "age": 22, "grade": 91},
    {"name": "Rina", "age": 26, "grade": 95}
]

# Write to a JSON file
with open("students.json", "w") as file:
    json.dump(students, file, indent=4)

# Read it back
with open("students.json", "r") as file:
    loaded_students = json.load(file)
    print(loaded_students)

for student in loaded_students:
    print(student["name"], type(student["age"]), type(student["grade"]))