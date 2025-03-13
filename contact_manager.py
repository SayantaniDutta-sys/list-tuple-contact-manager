# Contact manager application

contacts = []

def add_contact(name, phone, email):
    for contact in contacts:
        if contact[0] == name:
            print("Contact with this name already exists!")
            return
    contacts.append((name, phone, email))
    print("Contact added successfully!")

def view_contacts():
    if not contacts:
        print("No contacts found!")
        return
    print("\nList of Contacts:")
    index = 1
    for contact in contacts:
        print(f"{index}. {contact[0]} - {contact[1]} - {contact[2]}")
        index += 1

def search_contact(name):
    for contact in contacts:
        if contact[0] == name:
            print(f"Contact Found: {contact[0]} - {contact[1]} - {contact[2]}")
            return
    print("Contact not found!")

def update_contact(name, new_phone):
    global contacts
    for index in range(len(contacts)):
        if contact[0] == name:
            contacts[index] = (name, new_phone, contacts[index][2])
            print("Contact updated successfully!")
            return
    print("Contact not found!")

def delete_contact(name):
    global contacts
    for contact in contacts:
        if contact[0] == name:
            contacts.remove(contact)
            print("Contact deleted successfully!")
            return
    print("Contact not found!")

def main():
    while True:
        print("\nWelcome to Contact Manager")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            name = input("Enter Name: ")
            phone = input("Enter Phone Number: ")
            email = input("Enter Email: ")
            add_contact(name, phone, email)
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            name = input("Enter name to search: ")
            search_contact(name)
        elif choice == "4":
            name = input("Enter name to update: ")
            new_phone = input("Enter new phone number: ")
            update_contact(name, new_phone)
        elif choice == "5":
            name = input("Enter name to delete: ")
            delete_contact(name)
        elif choice == "6":
            print("Thank you for using Contact Manager. Have a great day!")
            break
        else:
            print("Invalid choice! Please try again.")

main()

