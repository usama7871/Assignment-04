def get_user_numbers():
    """
    This function keeps asking the user to enter numbers one by one.
    It stops when the user inputs a blank line (presses Enter without typing anything).
    All entered numbers are stored in a list and returned.
    """
    user_numbers = []  # This list will hold all numbers entered by the user
    
    while True:  # Keep asking until the user enters nothing
        user_input = input("Enter a number: ")
        
        # If the input is blank, we stop asking for more input
        if user_input == "":
            break
        
        # Convert the input string to an integer
        num = int(user_input)
        
        # Add the number to our list
        user_numbers.append(num)
    
    # Return the full list of numbers
    return user_numbers


def count_nums(num_lst):
    """
    This function takes a list of numbers and counts how many times each number appears.
    It returns a dictionary where each key is a number, and the value is how many times it appeared.
    """
    num_dict = {}  # An empty dictionary to store counts of each number
    
    for num in num_lst:  # Go through each number in the list
        if num not in num_dict:
            # If the number is not already in the dictionary, add it with value 1
            num_dict[num] = 1
        else:
            # If it is already there, increase the count by 1
            num_dict[num] += 1
    
    # Return the dictionary of number counts
    return num_dict


def print_counts(num_dict):
    """
    This function prints each number and how many times it appeared.
    It loops through the dictionary and prints the key (number) and its value (count).
    """
    for num in num_dict:
        print(str(num) + " appears " + str(num_dict[num]) + " times.")


def main():
    """
    This is the main function where the whole program runs.
    Step 1: Get all the numbers from the user.
    Step 2: Count how many times each number appeared.
    Step 3: Print the results.
    """
    user_numbers = get_user_numbers()       # Step 1
    num_dict = count_nums(user_numbers)     # Step 2
    print_counts(num_dict)                  # Step 3


# This is standard Python boilerplate.
# It means: "If this script is being run directly (not imported), call the main() function."
if __name__ == '__main__':
    main()
