import contacts

contact_list = contacts.load_contacts()

while True:
    option = int(input("\n1. Add Contact  2. View All  3. Search  4. Delete  5. Exit\nChoose: "))

    if option == 5:
        print("Goodbye!")
        break

    elif option == 1:
        name = input("Name: ")
        phone = input("Phone: ")
        email = input("Email: ")
        new_contact = contacts.add_contact(contact_list, name, phone, email)
        print(f"Added! ID: {new_contact['id']}")

    elif option == 2:
        contacts.view_contacts(contact_list)

    elif option == 3:
        name = input("Enter name to search: ")
        result = contacts.search_contact(contact_list, name)
        if result:
            print(f"[{result['id']}] {result['name']} - {result['phone']} - {result['email']} (Added: {result['added_on']})")
        else:
            print("Contact not found.")

    elif option == 4:
        name = input("Enter name to delete: ")
        if contacts.delete_contact(contact_list, name):
            print(f"{name} deleted.")
        else:
            print("Contact not found.")

    else:
        print("Please choose a valid option (1-5).")