"""
Right Triangle Hypotenuse Calculator
------------------------------------
This program calculates the length of the hypotenuse (BC) of a right triangle
using the Pythagorean theorem: BC² = AB² + AC²

The program demonstrates:
- Mathematical calculations
- Square root function
- User input handling
- Type conversion
"""

# Import the math module to access mathematical functions
# We specifically need math.sqrt() for square root calculation
import math

def main():
    """
    Main function that handles the program workflow:
    1. Gets lengths of sides AB and AC from user
    2. Calculates hypotenuse BC using Pythagorean theorem
    3. Displays the result
    """
    
    # Get length of side AB from user
    # float() converts the input string to a floating-point number
    # This handles both whole numbers and decimal inputs
    ab = float(input("Enter the length of AB in cms: "))
    
    # Get length of side AC from user
    # Same conversion as above for consistency
    ac = float(input("Enter the length of AC in cms: "))
    
    # Calculate hypotenuse using Pythagorean theorem:
    # BC = √(AB² + AC²)
    # math.sqrt() calculates the square root
    # ** is the exponent operator (AB**2 means AB squared)
    bc = math.sqrt(ab**2 + ac**2)
    
    # Display the result
    # str() converts the number to string for concatenation
    # The result will show with decimal point even for whole numbers
    # (e.g., 5.0 instead of 5) to indicate it's a float result
    print("The length of BC in cms(the hypotenuse) is: " + str(bc))

# Standard Python idiom to check if running directly
# This prevents execution when imported as a module
if __name__ == '__main__':
    # Execute the main program
    main()