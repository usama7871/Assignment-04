"""
Feet to Inches Converter
------------------------
This program converts a measurement in feet to its equivalent in inches.
The conversion factor is 12 inches per foot, as this is the standard
relationship between these American units of measurement.

Key Features:
- Demonstrates constant usage
- Shows simple unit conversion
- Handles user input with type conversion
- Provides clear output
"""

# Conversion constant - never changes
# Defined in ALL_CAPS to indicate it's a constant
# There are always 12 inches in 1 foot
INCHES_IN_FOOT = 12

def main():
    """
    Main program function that handles:
    1. Getting user input
    2. Performing the conversion
    3. Displaying the result
    
    Uses clear variable names and includes type hints for better understanding.
    """
    
    # Get user input and convert to float
    # float() is used instead of int() to handle decimal values
    # Example: Can convert 5.5 feet to inches
    feet = float(input("Enter number of feet: "))
    
    # Perform the conversion by multiplying feet by inches-per-foot
    # The constant makes the calculation clear and maintainable
    inches = feet * INCHES_IN_FOOT
    
    # Display the result using multiple print methods
    # Method 1: Comma-separated values (automatically adds spaces)
    print("That is", inches, "inches!")
    
    # Alternative method using f-string (Python 3.6+ preferred style)
    # print(f"That is {inches} inches!")
    
    # The comma version is used here to match the sample output exactly
    # but f-strings are generally preferred for modern Python code

# Standard Python idiom to check if this script is being run directly
# This prevents the code from running if imported as a module
if __name__ == '__main__':
    # Execute the main function
    main()