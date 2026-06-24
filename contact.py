import json
import os

def load_contacts():
    if os.path.exists("contact.json"):
        with open("contact.json", "r") as f:
            return json.load(f)
    return []

def save_contacts(contacts):
    with open("contact.json", "w") as f:
        json.dump(contacts,f, indent=2)

def add_contacts(contacts):
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    contacts.append({
        "name": name,
        "phone": phone,
        "email": email
    })
    save_contacts(contacts)
    print(f"Contact '{name}' added! ✅")

def view_contacts(contacts):
    if not contacts:
        print("No Contacts!")
        return
    for index, contact in enumerate(contacts):
        print(f"\n{index + 1}. 👤 {contact['name']}")
        print(f"   📞 {contact['phone']}")
        print(f"   📧 {contact['email']}")

def search_contact(contacts):
    query = input("Enter name to search: ")
    result = [c for c in contacts if query.lower() in c["name"].lower()]
    if not result:
        print("No contacts found!")
    else:
        for contact in result:
            print(f"\n👤 {contact['name']}")
            print(f"📞 {contact['phone']}")
            print(f"📧 {contact['email']}")

def delete_contact(contacts):
    view_contacts(contacts)
    index = int(input("Enter contact number to delete: ")) - 1
    if 0 <= index < len(contacts):
        removed = contacts.pop(index)
        save_contacts(contacts)
        print(f"Contact '{removed['name']}' deleted! 🗑️")
    else:
        print("Invalid number!")


def main():
    contacts = load_contacts()
    
    while True:
        print("\n📒 Contact Book")
        print("1. View all contacts")
        print("2. Add contact")
        print("3. Search contact")
        print("4. Delete contact")
        print("5. Exit")
        
        choice = input("\nEnter choice (1-5): ")
        
        if choice == "1":
            view_contacts(contacts)
        elif choice == "2":
            add_contacts(contacts)
        elif choice == "3":
            search_contact(contacts)
        elif choice == "4":
            delete_contact(contacts)
        elif choice == "5":
            print("Bye! 👋")
            break
        else:
            print("Invalid choice!")

main()
    