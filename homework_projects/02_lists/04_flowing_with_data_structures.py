"""
Mutable vs Immutable Data Types Demonstration
--------------------------------------------
This program demonstrates how mutable data types (like lists) behave differently
from immutable types (like numbers and strings) when passed to functions.

Key Concepts:
- Mutability in Python
- List modification in functions
- Reference vs value behavior
"""

def add_three_copies(my_list, data):
    """
    Adds three copies of the given data to the list.
    Demonstrates mutability by modifying the list in-place.
    
    Args:
        my_list: The list to modify (will be changed in-place)
        data: The item to add three copies of to the list
    """
    # Add three copies of the data to the list
    # Note: We're modifying the original list directly (mutability)
    for _ in range(3):  # _ is used when we don't need the loop variable
        my_list.append(data)  # Append modifies the list in-place
    
    # No return statement needed because we modified the original list

def main():
    """
    Main function that demonstrates mutable list behavior:
    1. Gets user input
    2. Shows list before modification
    3. Calls function to modify list
    4. Shows list after modification
    """
    # Get user input
    message = input("Enter a message to copy: ")
    
    # Create empty list
    my_list = []
    print("List before:", my_list)
    
    # Call function to modify the list
    add_three_copies(my_list, message)
    
    # Show modified list - changes persist even though we didn't return anything
    print("List after:", my_list)

    # Compare with immutable behavior (numbers)
    x = 5
    print("\nImmutable example:")
    print("x before:", x)
    
    def try_to_change(number):
        number += 10  # This change won't persist
        print("Inside function:", number)
    
    try_to_change(x)
    print("x after:", x)  # x remains unchanged

if __name__ == "__main__":
    main()