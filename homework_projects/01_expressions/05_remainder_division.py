"""
Division with Remainder Calculator
---------------------------------
This program performs integer division and calculates the remainder
between two numbers provided by the user.

The program demonstrates:
- Integer input handling
- Division operations (both quotient and remainder)
- String formatting for output
"""

def main():
    """
    Main function that handles the program workflow:
    1. Gets two integers from the user (dividend and divisor)
    2. Calculates the quotient using integer division
    3. Calculates the remainder using modulo operation
    4. Displays both results in a formatted string
    """
    
    # Get the dividend (number to be divided)
    # int() converts the input string to an integer
    # This ensures we're working with whole numbers only
    dividend = int(input("Please enter an integer to be divided: "))
    
    # Get the divisor (number to divide by)
    # Same conversion as above
    # Note: Program will crash if user enters 0 (division by zero error)
    divisor = int(input("Please enter an integer to divide by: "))
    
    # Calculate the quotient using floor division (//)
    # This discards any remainder and returns an integer result
    quotient = dividend // divisor
    
    # Calculate the remainder using modulo operator (%)
    # This gives what's left after integer division
    remainder = dividend % divisor
    
    # Format and display the results
    # Using f-string for cleaner string formatting (Python 3.6+)
    # str() conversions are handled automatically in f-strings
    print(f"The result of this division is {quotient} with a remainder of {remainder}")

    # Alternative version using concatenation (as in starter code):
    # print("The result of this division is " + str(quotient) + 
    #      " with a remainder of " + str(remainder))

# Standard Python idiom to check if running directly
if __name__ == '__main__':
    # Execute the main program
    main()