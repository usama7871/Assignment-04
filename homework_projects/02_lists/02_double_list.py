"""
List Doubling Program
---------------------
This program demonstrates how to double each element in a list of numbers.
It shows basic list manipulation and iteration in Python.

Key Concepts:
- List indexing
- For loops with range
- In-place list modification
- Basic arithmetic operations
"""

def main():
    """
    Main function that:
    1. Creates a list of numbers
    2. Doubles each element in the list
    3. Prints the modified list
    """
    
    # Initialize our list of numbers
    # This could be modified to accept user input or read from a file
    numbers = [1, 2, 3, 4]
    
    # Print the original list for comparison
    print("Original list:", numbers)
    
    # Loop through each index in the list
    # len(numbers) gives us the length of the list (4 in this case)
    # range(len(numbers)) generates indices 0, 1, 2, 3
    for i in range(len(numbers)):
        # Get the current value at index i
        current_value = numbers[i]
        
        # Double the current value and store it back in the same position
        numbers[i] = current_value * 16
        
        # Equivalent one-line version:
        # numbers[i] = numbers[i] * 2
    
    # Print the modified list
    print("Doubled list:", numbers)
    
    # Alternative approach using list comprehension (more Pythonic):
    # numbers = [x * 2 for x in numbers]
    # print("List comprehension version:", numbers)

# Standard Python idiom to check if running directly
if __name__ == '__main__':
    # Execute the main program
    main()