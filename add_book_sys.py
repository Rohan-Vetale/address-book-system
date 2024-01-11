'''

@Author: Rohan Vetale

@Date: 2024-01-10 09:00:30

@Last Modified by: Rohan Vetale

@Last Modified time: 2024-01-10 18:00:30

@Title : Program to create a contact of a user normally

''' 

class Contact:
    def __init__(self, first_name, last_name, address, city, state, phone_num, e_mail) :
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.phone_num = phone_num
        self.e_mail = e_mail

        
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
            print("First Name:", contact.first_name)
            print("Last Name:", contact.last_name)
            print("Address:", contact.address)
            print("City:", contact.city)
            print("State:", contact.state)
            print("ZIP Code:", contact.zip_code)
            print("Phone Number:", contact.phone_num)
            print("Email:", contact.e_mail)
            print("--------------------")
        

if __name__ == "__main__":
    first_name = input("Enter your first name : ")
    last_name = input("Enter your last name : ")
    address = input("Enter your address in short : ")
    city_name = input("Enter your city name : ")
    state = input("Enter your state name : ")
    phone_num = int(input("Enter your phone_num : "))
    zip_code = int(input("Enter your zip code : "))
    e_mail = input("Enter your e-mail id : ")
    add_book_obj = AddressBook()
    contact_obj = Contact(first_name, last_name, address, city_name, state, phone_num, e_mail)
    add_book_obj.add_contact(contact_obj)
    add_book_obj.display_contacts()
    
