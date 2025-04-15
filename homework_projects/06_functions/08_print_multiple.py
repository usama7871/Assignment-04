def print_multiple(message: str, repeats: int):
    """
    This function takes a string 'message' and an integer 'repeats', and prints
    the message 'repeats' number of times.
    """
    for i in range(repeats):
        print(message)

def main():
    message = input("Please type a message: ")  # Prompt the user for a message
    repeats = int(input("Enter a number of times to repeat your message: "))  # Prompt the user for how many times to repeat the message
    print_multiple(message, repeats)  # Call the print_multiple function to print the message

# This line ensures that the main function runs when the script is executed.
if __name__ == '__main__':
    main()
