class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def view_contacts(self):
        for contact in self.contacts:
            print(f"Name: {contact.name}, Phone: {contact.phone}")

    def search_contact(self, search_term):
        matching_contacts = [contact for contact in self.contacts if search_term.lower() in contact.name.lower()]
        if matching_contacts:
            print("Matching contacts found:")
            for contact in matching_contacts:
                print(f"Name: {contact.name}, Phone: {contact.phone}")
        else:
            print("No matching contacts found.")

    def update_contact(self, name, new_phone):
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                contact.phone = new_phone
                print(f"Updated phone number for {contact.name} is.")

    def delete_contact(self, name):
        self.contacts = [contact for contact in self.contacts if contact.name.lower() != name.lower()]
        print(f"{name} has been deleted from the contact book.")

def main():
    contact_book = ContactBook()

    while True:
        print("\nContact Book Menu:")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            name = input("Enter the name: ")
            phone = input("Enter the phone number: ")
            email = input("Enter the email: ")
            address = input("Enter the address: ")
            contact = Contact(name, phone, email, address)
            contact_book.add_contact(contact)
            print(f"{name} has been added to the contact book.")
        elif choice == "2":
            contact_book.view_contacts()
        elif choice == "3":
            search_term = input("Enter search term (name or phone): ")
            contact_book.search_contact(search_term)
        elif choice == "4":
            name = input("Enter name of the contact to update: ")
            new_phone = input("Enter new phone number: ")
            contact_book.update_contact(name, new_phone)
        elif choice == "5":
            name = input("Enter name of the contact to delete: ")
            contact_book.delete_contact(name)
        elif choice == "6":
            print("Exiting Contact Book. Goodbye!")
            break
        else:
            print("Invalid choice! Please select a valid option.")

if __name__ == "__main__":
    main()
