'''

@Author: Rohan Vetale

@Date: 2024-01-10 09:00:30

@Last Modified by: Rohan Vetale

@Last Modified time: 2024-01-10 18:00:30

@Title : Program to create a contact of a user normally

''' 
import csv
import json
class Contact:
    def __init__(self, contact_detalis_dict):
        self.first_name = contact_detalis_dict.get("first_name")
        self.last_name = contact_detalis_dict.get("last_name")
        self.address = contact_detalis_dict.get("address")
        self.city = contact_detalis_dict.get("city")
        self.state = contact_detalis_dict.get("state")
        self.pin = contact_detalis_dict.get("pin")
        self.phone = contact_detalis_dict.get("phone")
        self.email = contact_detalis_dict.get("email")
        self.file = "my_contact.txt"
        self.csv_file = "csv_file.csv"
        
    def add_contact_file(self):
        """
        Description: This function return all the contact info.
        Parameter: self object as parameter.
        Return:contact information.
        """
        return [f'{self.first_name} | {self.last_name} | {self.address} | {self.city} | {self.state} | {self.pin} | '
                f'{self.phone} | {self.email}']

    def add_contact_csv(self):
        """
        Description: This function return contact info dict.
        Parameter: self object as parameter.
        Return:contact info dict.
        """
        return {"first_name": self.first_name, "last_name": self.last_name,
                "address": self.address, "city": self.city, "state": self.state,
                "pin": self.pin, "phone": self.phone, "email": self.email}

    def display_contact(self):
        """
        Description: This function for display all contact by city name or state name.
        Parameter: None.
        Return:None
        """
        print(f"""
                first name: {self.first_name} 
                last name: {self.last_name} 
                phone number: {self.phone}
                address : {self.address}
                city : {self.city}
                state : {self.state}
                email : {self.email}
                Zip code : {self.pin}
        """)
        print("---------------------------------------------------------")

    def update_contact(self):
        """
        Description: This function for updating contact.
        Parameter: None.
        Return:None
        """
        while True:
            choice = int(input("""
                        1. change first name
                        2. change last name
                        3. change address
                        4. change city
                        5. change state
                        6. change phone number
                        7. change email
                        8. change Zip code
                        9. exit
            """))
            match choice:
                case 1:
                    change_first_name= input("Enter new first name: ")
                    self.first_name = change_first_name
                case 2:
                    change_last_name = input("Enter new last name: ")
                    self.last_name = change_last_name
                case 3:
                    change_address = input("Enter new address: ")
                    self.address = change_address
                case 4:
                    change_city = input("Enter new city: ")
                    self.city = change_city
                case 5:
                    change_state = input("Enter new state: ")
                    self.state = change_state
                case 6:
                    change_num = input("Enter new phone number: ")
                    self.phone = change_num
                case 7:
                    change_mail = input("Enter new email address: ")
                    self.email = change_mail
                case 8:
                    change_pin = input("Enter new zip code: ")
                    self.pin = change_pin
                case 9:
                    break
            
    def write_contact_file(self):
        """
        Description: This function write contact data in a text file.
        Parameter: self object as parameter.
        Return:None
        """
        with open(self.file, 'a', newline="") as f:
            f.write(str(f"{self.add_contact_file()}\n"))
    
    def add_contact_json(self):
        """
        Description: This function return contact info dict.
        Parameter: self object as parameter.
        Return: contact info dict.
        """
        return {"first_name": self.first_name, "last_name": self.last_name, "address": self.address,
                "city": self.city, "state": self.state, "pin": self.pin, "phone": self.phone, "email": self.email}

    def add_address_book_file(self):
        """
        Description: This function write contact data in a text file.
        Parameter: self object as parameter.
        Return:None
        """
        with open(self.file, 'a', newline="") as f:
            f.write(str(f"{self.add_contact_file()}\n"))

    

class AddressBook:
    def __init__(self, address_book_name):
        self.address_book_name = address_book_name
        self.contact_dict = {}
        self.person_by_city = {}
        self.person_by_state = {}
        self.csv_file = 'csv_file.csv'
        self.json_contact_dict = {}

    def add_contact(self, contact_obj):
        """
        Description: This function for adding a contact to contact dictionary.
        Parameter: contact class object as parameter.
        Return:None
        """
        if contact_obj.first_name not in self.contact_dict:
            self.contact_dict.update({contact_obj.first_name: contact_obj})

        else:
            raise Exception("Contact all. present")

    def contact_details(self):
        """
        Description: This function get all contact details from contact dictionary.
        Parameter: None
        Return:None
        """
        for key, value in self.contact_dict.items():
            print(f"""
                    first name: {key} 
                    last name: {value.last_name} 
                    phone number: {value.phone}
                    address : {value.address}
                    city : {value.city}
                    state : {value.state}
                    email : {value.email}
                    Zip code : {value.pin}
            """)

    def contact_update(self, name):
        """
        Description: This function for updating contact.
        Parameter: string
        Return:None
        """
        contact_obj: Contact = self.contact_dict.get(name)
        if contact_obj:
            contact_obj.update_contact()
        else:
            print("contact not present!!")

    def delete_contact(self, name):
        """
        Description: This function for delete a contact.
        Parameter: string
        Return:None
        """
        if name in self.contact_dict:
            self.contact_dict.pop(name)
        else:
            print("contact not found!!")

    def display_person_in_city_or_state(self, city):
        """
        Description: This function is displaying all the contact info using city and state .
        Parameter: city : string name of the city
        Return: None
        """
        # for key, value in self.contact_dict.items():
        #     if value.city == name or value.state == name:
        #         value.display_contact()
        #     else:
        #         print("city or state is not present!!")
        #         continue
        #     count += 1
        #     return count
        contacts = dict(filter(lambda x: x[1].city.lower() == city.lower() or x[1].state.lower() == city.lower(),
                               self.contact_dict.items()))
        for i in contacts.values():
            i.display_contact()
        return len(contacts)

    
    def sort_by_name(self):
        """
        Description: This function is sorting the contact using person name.
        Parameter: None
        Return: None
        """
        for key, value in dict(sorted(self.contact_dict.items())).items():
            value.display_contact()
            
    def sort_by_city(self, name):
        """
        Description: This function is sorting the contact using city, state, zip.
        Parameter: string
        Return: None
        """
        sorted_contact = sorted(self.contact_dict.values(), key=lambda x: x.city == name, reverse=True)
        for i in sorted_contact:
            i: Contact
            print(i.first_name, '>>>>', i.city)
    def read_write_csv(self):
        """
        Description: This function is read and write data in csv file.
        Parameter: self object as parameter.
        Return: None
        """
        with open(self.csv_file, 'w', newline="") as file:
            field_names = ['address_book_name', 'first_name', 'last_name', 'address', 'city', 'state', 'pin', 'phone',
                            'email']
            writer = csv.DictWriter(file, fieldnames=field_names)
            writer.writeheader()
            for key, value in self.contact_dict.items():
                data = value.add_contact_csv()
                data.update({'address_book_name': key})
                writer.writerow(data)
    def add_json_contact(self):
        """
        Description: This function is read and write data in csv file.
        Parameter: self object as parameter.
        Return: None
        """
        for key, value in self.contact_dict.items():
            self.json_contact_dict.update({key: value.add_contact_json()})


        
        


class MegaBook:

    def __init__(self):
        self.book_dict = {}
        self.json_file = 'json_file.json'
        

    def add_multiple_book(self, addressbook_obj):
        """
        Description: This function add multiple book.
        Parameter: address book object
        Return:None
        """
        self.book_dict.update({addressbook_obj.address_book_name: addressbook_obj})

    def get_book(self, name):
        """
        Description: This function for getting the name of address book from address book dictionary .
        Parameter: string
        Return:name of address book present in address book dictionary.
        """
        return self.book_dict.get(name)
    
    def write_json(self):
        """
        Description: This function for writing data in json file.
        Parameter: self object as parameter.
        Return: None
        """
        json_dict = {}
        for name, obj in self.book_dict.items():
            json_dict.update({name: obj.json_contact_dict})
        with open(self.json_file, 'w') as file:
            json.dump(json_dict, file, indent=4)
            file.close()

    @staticmethod
    def read_json():
        """
        Description: This function for reading data from json file.
        Parameter: self object as parameter.
        Return: None
        """
        json_file = open("json_file.json")
        data = json.load(json_file)
        for i in data.items():
            print(i)
        json_file.close()


def main():
    """
    Description: This function for calling all the methods in all classes.
    Parameter: None
    Return: None
    """
    # Creating an instance of MegaBook
    multiple_book_obj = MegaBook()
    try:
        while True:
            # Displaying a menu for user choices
            choice = int(input("""
                        1. Add contact
                        2. Get all details of contact
                        3. Update contact info
                        4. Delete contact
                        5. Display all contacts by city or state
                        6. Display in sorted by name form
                        7. Display in sorted by city name form
                        8. Write an address book in a CSV file
                        9. Write an address book in a JSON file
                        10. Exit the program
            """))
            # Using match statement for different user choices
            match choice:
                # Case 1: Adding a contact
                case 1:
                    address_book_name = input("Enter the book name: ")
                    addressbook_obj = multiple_book_obj.get_book(address_book_name)
                    if addressbook_obj is None:
                        addressbook_obj = AddressBook(address_book_name)
                    first_name = input("Enter First Name: ")
                    last_name = input("Enter Last Name: ")
                    address = input("Enter Address: ")
                    city = input("Enter City: ")
                    state = input("Enter State: ")
                    pin = int(input("Enter Pin: "))
                    phone = int(input("Enter Phone: "))
                    email = input("Enter Email: ")
                    contact_detalis_dict = {"first_name": first_name, "last_name": last_name, "address": address,
                                            "city": city, "state": state, "pin": pin, "phone": phone, "email": email}
                    contact_obj = Contact(contact_detalis_dict)
                    addressbook_obj.add_contact(contact_obj)
                    multiple_book_obj.add_multiple_book(addressbook_obj)
                    contact_obj.add_address_book_file()
                    addressbook_obj.add_json_contact()
                # Case 2: Getting all details of contacts in an address book
                case 2:
                    address_book_name = input("Enter the book name: ")
                    addressbook_obj = multiple_book_obj.get_book(address_book_name)
                    # If the address book exists, display all contact details
                    if addressbook_obj is not None:
                        addressbook_obj.contact_details()
                    else:
                        print("Please try again")
                # Case 3: Updating contact information
                case 3:
                    address_book_name = input("Enter the book name: ")
                    addressbook_obj = multiple_book_obj.get_book(address_book_name)
                    name = input("Enter name of contact: ")
                    # Update the contact information in the address book
                    addressbook_obj.contact_update(name)
                # Case 4: Deleting a contact
                case 4:
                    address_book_name = input("Enter the book name: ")
                    addressbook_obj = multiple_book_obj.get_book(address_book_name)
                    name = input("Enter name: ")
                    # Delete the contact from the address book
                    addressbook_obj.delete_contact(name)
                # Case 5: Displaying all contacts by city or state
                case 5:
                    address_book_name = input("Enter the book name: ")
                    addressbook_obj = multiple_book_obj.get_book(address_book_name)
                    name = input("Enter city or state name: ")
                    # Display contacts by city or state and print the count
                    print(addressbook_obj.display_person_in_city_or_state(name))
                # Case 6: Exit the program
                case 6:
                    #sort the addressbook by person's name
                    address_book_name = input("Enter the book name: ")
                    addressbook_obj = multiple_book_obj.get_book(address_book_name)
                    if addressbook_obj is None:
                        addressbook_obj = AddressBook(address_book_name)
                    addressbook_obj.sort_by_name()
                  
                case 7:
                    address_book_name = input("Enter the book name: ")
                    addressbook_obj = multiple_book_obj.get_book(address_book_name)
                    if addressbook_obj is None:
                        addressbook_obj = AddressBook(address_book_name)
                    addressbook_obj.sort_by_city()
                    
                case 8:
                    address_book_name = input("Enter the book name: ")
                    addressbook_obj = multiple_book_obj.get_book(address_book_name)
                    if addressbook_obj is None:
                        addressbook_obj = AddressBook(address_book_name)
                    addressbook_obj.read_write_csv()
                    
                case 9:
                    multiple_book_obj.write_json()
                    multiple_book_obj.read_json()
                    
                case 10:
                    break

    except Exception as e:
        # Print any exceptions that occur during execution
        print(e)


if __name__ == '__main__':
    # Call the main function if the script is executed directly
    main()
