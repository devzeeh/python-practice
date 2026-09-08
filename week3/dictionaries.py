# dictionary stores data as key-value pairs
# instead of accessing items by position (like a list), you access them by a meaningful key.

student = {
    "name": "Alex",
    "age": 20,
    "course": "CpE"
}

print(student["name"]) # "Alex"
print(student["course"]) # 20

student["age"] = 21 # update a value
student["year_level"] = "4" # add a new key-value pair
print(student)

del student["course"] # remove a key-value pair
print(student)

print(student.keys()) # all the keys
print(student.values()) # all the values

print("name" in student) # True — checks if a key exists