class Contact:
    def __init__(self, name, phone_number):
        self.name = name
        self.phone_number = phone_number

class ContactManagementSystem:
    def __init__(self):
        self.contacts = []

    def add_contact(self):
        name = input("Enter the contact name: ")
        phone_number = input("Enter the contact phone number: ")

        new_contact = Contact(name, phone_number)
        self.contacts.append(new_contact)

        print("Contact added successfully!")

    def view_contacts(self):
        if not self.contacts:
            print("No contacts available.")
        else:
            print("Contacts:")
            for contact in self.contacts:
                print(f"Name: {contact.name}, Phone Number: {contact.phone_number}")

    def search_contact(self):
        search_name = input("Enter the name to search: ")

        for contact in self.contacts:
            if contact.name.lower() == search_name.lower():
                print("Contact found:")
                print(f"Name: {contact.name}, Phone Number: {contact.phone_number}")
                return

        print(f"Contact not found for name: {search_name}")

if __name__ == "__main__":
    contact_manager = ContactManagementSystem()

    while True:
        print("\nContact Management System Menu:")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            contact_manager.add_contact()
        elif choice == '2':
            contact_manager.view_contacts()
        elif choice == '3':
            contact_manager.search_contact()
        elif choice == '4':
            print("Exiting Contact Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")
