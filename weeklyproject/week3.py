students = []

while True:
    option = int(input("\n=== Student Record CLI ===\n" \
    "1. Add Student\n2. View All\n3. Search by Name\n4. Delete Student\n5. Exit\nChoose: "))

    if option == 5:
        print("Goodbye!")
        break

    elif option == 1:
        name = input("Enter name: ")
        age = int(input("Enter age: "))
        grade = int(input("Enter grade: "))
        students.append({"name": name, "age": age, "grade": grade})
        print("Student added!")

    elif option == 2:
        if not students:
            print("No students yet.")
        for student in students:
            print(f"Name: {student['name']}, Age: {student['age']}, Grade: {student['grade']}")

    elif option == 3:
        search_name = input("Enter name to search: ")
        found = False
        for student in students:
            if student["name"] == search_name:
                print(f"Found: {student['name']}, Age: {student['age']}, Grade: {student['grade']}")
                found = True
                break
        if not found:
            print("Student not found.")

    elif option == 4:
        delete_name = input("Enter name to delete: ")
        found = False
        for student in students:
            if student["name"] == delete_name:
                students.remove(student)
                print(f"{delete_name} deleted.")
                found = True
                break
        if not found:
            print("Student not found.")

    else:
        print("Please choose a valid option (1-5).")