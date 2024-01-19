import pytest
from add_book_sys import Contact, AddressBook

# Fixture for creating a Contact object
@pytest.fixture
def contact_obj():
    contact_details_dict = {"first_name": 'Rohan', "last_name": 'Vetale'}
    return Contact(contact_details_dict)

# Fixture for creating an AddressBook object
@pytest.fixture
def address_obj():
    address_book_name = 'MAHA'
    return AddressBook(address_book_name)

# Test to check if contact details are set correctly
def test_check_contact_success(contact_obj):
    assert contact_obj.first_name == 'Rohan'
    assert contact_obj.last_name == 'Vetale'

# Test to check if a contact is successfully added to the address book
def test_add_contact_success(contact_obj, address_obj):
    assert len(address_obj.contact_dict) == 0
    address_obj.add_contact(contact_obj)
    assert len(address_obj.contact_dict) != 0

# Test to check if a contact is successfully deleted from the address book
def test_delete_contact(contact_obj, address_obj):
    address_obj.add_contact(contact_obj)
    assert 'Rohan' in address_obj.contact_dict
    address_obj.delete_contact('Rohan')
    assert 'Rohan' not in address_obj.contact_dict

# Test to check if contacts are sorted by name
def test_sort_by_name(contact_obj, address_obj, capsys):
    address_obj.add_contact(contact_obj)
    address_obj.sort_by_name()
    captured = capsys.readouterr()
    assert 'Rohan' in captured.out

# Test to check if contacts are sorted by city
def test_sort_by_city(contact_obj, address_obj, capsys):
    address_obj.add_contact(contact_obj)
    address_obj.sort_by_city('MAHA')
    captured = capsys.readouterr()
    assert 'Rohan' in captured.out

# Test to check if contact details can be read and written to a CSV file
def test_read_write_csv(contact_obj, address_obj, tmp_path):
    address_obj.add_contact(contact_obj)
    csv_file_path = tmp_path / "test_csv_file.csv"
    address_obj.csv_file = csv_file_path
    address_obj.read_write_csv()
    assert csv_file_path.is_file()
    
# Test to check displaying of a contact's first name    
def test_display_contact(contact_obj):
    assert contact_obj.display_contact() == "Rohan"
    
    
# Test to check wrong contact name from a given contact 
def test_display_contact_wrong(contact_obj):
    assert contact_obj.display_contact() != "Omkar"
    
    