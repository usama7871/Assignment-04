"""
Seconds in a Year Calculator
---------------------------
This program calculates how many seconds are in one year using
constant values for time conversions. It demonstrates:
- Constant usage for maintainability
- Basic arithmetic operations
- String formatting for output
"""

# Time conversion constants
# Using ALL_CAPS naming convention for constants
# These values never change during program execution
DAYS_PER_YEAR = 365    # Number of days in a year (non-leap year)
HOURS_PER_DAY = 24     # Hours in one day
MINUTES_PER_HOUR = 60   # Minutes in one hour
SECONDS_PER_MINUTE = 60 # Seconds in one minute

def main():
    """
    Main function that:
    1. Calculates total seconds in a year by multiplying time constants
    2. Formats and prints the result in a user-friendly message
    """
    
    # Calculate total seconds by multiplying all time conversion factors
    # The calculation reads naturally from largest to smallest units:
    # years → days → hours → minutes → seconds
    seconds_in_year = DAYS_PER_YEAR * HOURS_PER_DAY * MINUTES_PER_HOUR * SECONDS_PER_MINUTE
    
    # Format and display the result
    # Using f-string for clean string interpolation (Python 3.6+)
    print(f"There are {seconds_in_year} seconds in a year!")
    
    # Alternative version using string concatenation:
    # print("There are " + str(seconds_in_year) + " seconds in a year!")

# Standard Python idiom to check if running directly
# This prevents execution when imported as a module
if __name__ == '__main__':
    # Execute the main program
    main()