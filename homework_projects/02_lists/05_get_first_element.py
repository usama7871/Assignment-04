"""
First Element Retrieval Program
------------------------------
This program demonstrates how to:
1. Collect a list from user input
2. Access and print the first element of a list
3. Handle guaranteed non-empty lists

Key Concepts:
- List indexing
- User input collection
- Function composition
"""

def get_first_element(lst):
    """
    Prints the first element of a provided list.
    
    Args:
        lst: A non-empty list containing elements of any type
        
    Behavior:
        - Accesses the first element using index 0
        - Prints the element directly
        - Does not return any value
    """
    # Access and print the first element (index 0)
    # Since the list is guaranteed non-empty, we don't need error checking
    print("The first element is:", lst[0])

def get_lst():
    """
    Collects a list from user input one element at a time.
    
    Returns:
        A list containing all user-entered elements
        
    Behavior:
        - Prompts user for elements until empty input
        - Adds each element to the growing list
        - Returns the complete list when done
    """
    lst = []  # Initialize empty list to store elements
    
    # Get first element (empty string stops collection)
    elem = input("Please enter an element of the list or press enter to stop. ")
    
    # Continue collecting until empty input
    while elem != "":
        lst.append(elem)  # Add element to list
        elem = input("Please enter an element of the list or press enter to stop. ")
    
    return lst  # Return the completed list

def main():
    """
    Main program workflow:
    1. Collect list from user
    2. Print first element
    3. (Implicitly handles empty list case via problem constraints)
    """
    # Step 1: Get list from user
    lst = get_lst()
    
    # Step 2: Print first element
    # Problem states list is guaranteed non-empty
    get_first_element(lst)

# Standard Python idiom to execute main() when run directly
if __name__ == '__main__':
    main()