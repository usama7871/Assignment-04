def greet(name):
    # Returns a greeting message by concatenating "Greetings" with the user's name
    return "Greetings " + name + "!"

def main():
    # Prompt the user for their name
    name = input("What's your name? ")
    # Call the greet function and print the greeting message
    print(greet(name))

# Call the main function to run the program
if __name__ == '__main__':
    main()
