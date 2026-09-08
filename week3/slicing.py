# A nested collection is just a collection inside another collection
# e.g., a list of dictionaries, or a dictionary containing a list.

students = [
    {"name": "Alex", "grade": 75},
    {"name": "Jamie", "grade": 80},
    {"name": "Sam", "grade": 85}
]

print(students[1]) # the whole first dictionary
print(students[2]["name"]) # "Sam" — drill into the dict inside the list

# print the value of name and grade
for student in students: 
    print(student["name"], student["grade"])