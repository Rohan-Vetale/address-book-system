'''

@Author: Rohan Vetale

@Date: 2024-01-10 09:00:30

@Last Modified by: Rohan Vetale

@Last Modified time: 2024-01-10 18:00:30

@Title : Program to create a contact of a user normally

''' 

class Contact:
        
    def new_contact(self) :
        self.first_name = input("Enter your first name : ")
        self.last_name = input("Enter your last name : ")
        self.address = input("Enter your address in short : ")
        self.city = input("Enter your city name : ")
        self.state = input("Enter your state name : ")
        self.phone_num = int(input("Enter your phone_num : "))
        self.zip_code = int(input("Enter your zip code : "))
        self.e_mail = input("Enter your e-mail id : ")
        

        
class AddressBook :
    def __init__(self) :
        self.contacts = []
        
    def add_contact(self, contact_obj):
        self.contacts.append(contact_obj)
        print("Contact added successfully")
        
    def display_contacts(self):
        if len(self.contacts) == 0:
            print("No contacts found.")
            return
        for contact in self.contacts:
            print("----------------------------- \n ")
            print("First Name:", contact.first_name)
            print("Last Name:", contact.last_name)
            print("Address:", contact.address)
            print("City:", contact.city)
            print("State:", contact.state)
            print("ZIP Code:", contact.zip_code)
            print("Phone Number:", contact.phone_num)
            print("Email:", contact.e_mail)
            print("--------------------")
    
    def edit_contact(self):
        first_name = input("Enter the first name to search : ")
        last_name = input("Enter the last name to search : ")
        for contact in self.contacts:
            if contact.first_name == first_name and contact.last_name == last_name:
                new_address = input("Enter new address: ")
                new_city = input("Enter new city: ")
                new_state = input("Enter new state: ")
                new_zip_code = input("Enter new ZIP code: ")
                new_phone_number = input("Enter new phone number: ")
                new_email = input("Enter new email: ")
                contact.address = new_address
                contact.city = new_city
                contact.state = new_state
                contact.zip_code = new_zip_code
                contact.phone_num = new_phone_number
                contact.e_mail = new_email
                print("Contact updated successfully.")
                return
        print("Contact not found.")
        
    def delete_contact(self):
        first_name = input("Enter the first name to search : ")
        last_name = input("Enter the last name to search : ")
        for contact in self.contacts:
            if contact.first_name == first_name and contact.last_name == last_name:
                self.contacts.remove(contact)
                print("Contact deleted successfully.")
                return
        print("Contact not found.")
        
    
        

if __name__ == "__main__":
    
    addr_book_obj = AddressBook()
    while True:

        choice_num = int(input("Enter the choice number you want for: \n 1. Add New Contact \n 2. Edit a contact \n --> "))

        match choice_num:
            case 1:
                contact_obj = Contact()
                contact_obj.new_contact()
                addr_book_obj.add_contact(contact_obj=contact_obj)
                addr_book_obj.display_contacts()
            case 2:
                addr_book_obj.edit_contact()
                addr_book_obj.display_contacts()
            case 3:
                addr_book_obj.delete_contact()
                addr_book_obj.display_contacts()
            case 10:
                break
    
    
