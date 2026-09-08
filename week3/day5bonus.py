students = [
    {"name": "Alex", "grade": 75},
    {"name": "Jamie", "grade": 80},
    {"name": "Sam", "grade": 85}
]

students.append({"name": "Riley", "grade": 90})
students[0].update({"grade": 95})
print(students)