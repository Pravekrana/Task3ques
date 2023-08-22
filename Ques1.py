import re

def is_valid_contact_number(contact_number):
    # Define a regular expression pattern for a valid contact number
    pattern = r'^(\+?\d{1,3}[-.\s]?)?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}$'
    
    # Use the re.match function to check if the contact number matches the pattern
    if re.match(pattern, contact_number):
        return True
    else:
        return False

# Input from the user
contact_number = input("Enter a contact number: ")

# Check if the contact number is valid
if is_valid_contact_number(contact_number):
    print("Valid contact number.")
else:
    print("Invalid contact number.")
