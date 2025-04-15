"""
Number Sum Calculator
--------------------
This program demonstrates how to sum a list of numbers in Python.
It includes both a function to calculate the sum and a main program
to demonstrate its usage.

Key Concepts:
- List operations
- For loops
- Variable accumulation
- Function definition and usage
"""

def add_many_numbers(numbers: list[int]) -> int:
    """
    Calculates the sum of all numbers in a list.
    
    Args:
        numbers: A list of integers to be summed
        
    Returns:
        The total sum of all numbers in the input list
    """
    # Initialize our accumulator variable
    # Starting at 0 because we haven't added anything yet
    total_so_far = 0
    
    # Iterate through each number in the input list
    for number in numbers:
        # Add the current number to our running total
        total_so_far += number  # Equivalent to total_so_far = total_so_far + number
    
    # Return the final accumulated total
    return total_so_far

def main():
    """
    Main program that demonstrates the add_many_numbers function.
    Creates a list of numbers, calculates their sum, and prints the result.
    """
    
    # Create a list of numbers to sum
    # This could be modified to accept user input instead
    numbers = [1, 2, 3, 4, 5]
    
    # Calculate the sum using our function
    sum_of_numbers = add_many_numbers(numbers)
    
    # Print the result
    print(f"The sum of the numbers is: {sum_of_numbers}")
    
    # Additional demonstration with a different list
    another_list = [10, 20, 30]
    print(f"Sum of another list: {add_many_numbers(another_list)}")

# Standard Python idiom to check if running directly
if __name__ == '__main__':
    # Execute the main program
    main()