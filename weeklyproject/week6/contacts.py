import json
import random
from datetime import datetime
from pathlib import Path

file_path = Path(__file__).parent / "contacts.json"


def load_contacts():
    if file_path.exists():
        with open(file_path, "r") as file:
            return json.load(file)
    return []


def save_contacts(contacts):
    with open(file_path, "w") as file:
        json.dump(contacts, file, indent=4)


def add_contact(contacts, name, phone, email):
    contact = {
        "id": random.randint(1000, 9999),
        "name": name,
        "phone": phone,
        "email": email,
        "added_on": datetime.now().strftime("%Y-%m-%d")
    }
    contacts.append(contact)
    save_contacts(contacts)
    return contact


def view_contacts(contacts):
    if not contacts:
        print("No contacts yet.")
        return
    for contact in contacts:
        print(f"[{contact['id']}] {contact['name']} - {contact['phone']} - {contact['email']} (Added: {contact['added_on']})")


def search_contact(contacts, name):
    for contact in contacts:
        if contact["name"].lower() == name.lower():
            return contact
    return None


def delete_contact(contacts, name):
    contact = search_contact(contacts, name)
    if contact:
        contacts.remove(contact)
        save_contacts(contacts)
        return True
    return False