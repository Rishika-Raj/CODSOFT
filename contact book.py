class ContactBook:
    def __init__(self):
        self.contacts = {}

    def add_contact(self):
        name = input("Enter the contact's name: ")
        phone_number = input("Enter the contact's phone number: ")
        email = input("Enter the contact's email: ")
        address = input("Enter the contact's address: ")
        self.contacts[name] = {"phone_number": phone_number, "email": email, "address": address}
        print("Contact added successfully!")

    def view_contact_list(self):
        if not self.contacts:
            print("No contacts found.")
        else:
            print("Contact List:")
            for name, details in self.contacts.items():
                print(f"{name}: {details['phone_number']}")

    def search_contact(self):
        search_term = input("Enter the name or phone number to search: ")
        for name, details in self.contacts.items():
            if search_term in name or search_term in details["phone_number"]:
                print(f"Contact found: {name} - {details['phone_number']}")
                break
        else:
            print("Contact not found.")

    def update_contact(self):
        name = input("Enter the name of the contact to update: ")
        if name in self.contacts:
            details = self.contacts[name]
            details["phone_number"] = input("Enter the new phone number: ")
            details["email"] = input("Enter the new email: ")
            details["address"] = input("Enter the new address: ")
            print("Contact updated successfully!")
        else:
            print("Contact not found.")

    def delete_contact(self):
        name = input("Enter the name of the contact to delete: ")
        if name in self.contacts:
            del self.contacts[name]
            print("Contact deleted successfully!")
        else:
            print("Contact not found.")

    def run(self):
        while True:
            print("\nContact Book Options:")
            print("1. Add Contact")
            print("2. View Contact List")
            print("3. Search Contact")
            print("4. Update Contact")
            print("5. Delete Contact")
            print("6. Exit")
            choice = input("Choose an option: ")
            if choice == "1":
                self.add_contact()
            elif choice == "2":
                self.view_contact_list()
            elif choice == "3":
                self.search_contact()
            elif choice == "4":
                self.update_contact()
            elif choice == "5":
                self.delete_contact()
            elif choice == "6":
                print("Exiting Contact Book.")
                break
            else:
                print("Invalid choice. Please choose a valid option.")


if __name__ == "__main__":
    contact_book = ContactBook()
    contact_book.run()