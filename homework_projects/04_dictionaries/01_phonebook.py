def read_phone_numbers():
    """
    Ask the user to input names and phone numbers.
    This information is stored in a dictionary (phonebook),
    where the key is the name and the value is the phone number.
    The input process continues until the user presses Enter without typing a name.
    """
    phonebook = {}  # Empty dictionary to store name-number pairs

    while True:
        name = input("Name: ")
        if name == "":  # If name is blank, stop asking
            break
        number = input("Number: ")  # Ask for corresponding phone number
        phonebook[name] = number  # Add to the dictionary

    return phonebook  # Return the full phonebook


def print_phonebook(phonebook):
    """
    Go through the dictionary and print each name with its corresponding number.
    Format: name -> number
    """
    print("\nPhonebook Entries:")
    for name in phonebook:
        print(f"{name} -> {phonebook[name]}")


def lookup_numbers(phonebook):
    """
    Let the user search for phone numbers by entering names.
    Keeps asking until the user enters a blank line.
    If the name is in the phonebook, it shows the number.
    If not, it prints a message saying it wasn’t found.
    """
    print("\nPhonebook Lookup:")
    while True:
        name = input("Enter name to lookup: ")
        if name == "":
            break
        if name in phonebook:
            print(f"{name}'s number is {phonebook[name]}")
        else:
            print(f"{name} is not in the phonebook")


def main():
    """
    1. Read phone numbers into a dictionary.
    2. Display all saved contacts.
    3. Let the user search for contacts by name.
    """
    phonebook = read_phone_numbers()       # Step 1: Create phonebook
    print_phonebook(phonebook)             # Step 2: Print all entries
    lookup_numbers(phonebook)              # Step 3: Allow lookups


# Python boilerplate code: Ensures main() runs if script is executed directly.
if __name__ == '__main__':
    main()
