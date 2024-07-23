# Task 1: Input Length Validator
def check_name_length():
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")

    if len(first_name) < 2:
        print("Error: First name must be at least 2 characters long.")
    if len(last_name) < 2:
        print("Error: Last name must be at least 2 characters long.")

    if len(first_name) >2 and len(last_name) >= 2:
        print("Both names are valid.")

check_name_length()
