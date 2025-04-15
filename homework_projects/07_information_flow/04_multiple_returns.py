def get_user_data():
    # Ask the user for their first name, last name, and email address
    first_name = input("What is your first name?: ")
    last_name = input("What is your last name?: ")
    email_address = input("What is your email address?: ")
    
    # Return all three pieces of data as a tuple
    return first_name, last_name, email_address

########## No need to edit code past this point :) ##########

def main():
    # Call the function to get the user's data and store it in a variable
    user_data = get_user_data()

    # Print out the received user data as a tuple
    print("Received the following user data:", user_data)

if __name__ == "__main__":
    main()
