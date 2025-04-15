"""
Program: add2numbers
--------------------
This program asks the user for two integers and prints their sum.
"""

def main():
    print("This program adds two numbers.")
    
    # Prompt user for first number and convert to integer
    num1 = int(input("Enter the first number: "))
    
    # Prompt user for second number and convert to integer
    num2 = int(input("Enter the second number: "))
    
    # Calculate the sum
    total = num1 + num2
    
    # Display the result
    print(f"The sum of {num1} and {num2} is {total}.")

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()

