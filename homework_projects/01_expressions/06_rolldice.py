"""
Dice Rolling Simulator
----------------------
This program simulates rolling two standard 6-sided dice,
displays the result of each die, and calculates their total.

Key Features:
- Random number generation
- Constant usage
- Multiple variable assignments
- Formatted output
"""

# Import the random module to generate random numbers
# We'll use random.randint() to simulate dice rolls
import random

# Constant defining the number of sides on each die
# Standard dice have 6 sides, numbered 1 through 6
# Using ALL_CAPS naming convention for constants
NUM_SIDES = 6

def main():
    """
    Main function that handles the dice rolling simulation:
    1. Generates two random dice rolls
    2. Calculates their total
    3. Displays all results in a user-friendly format
    """
    
    # For testing/debugging purposes, you can uncomment the line below
    # to get the same random numbers each time (seed value 1)
    # random.seed(1)
    
    # Simulate rolling the first die
    # random.randint(a, b) returns a random integer N where a <= N <= b
    die1 = random.randint(1, NUM_SIDES)
    
    # Simulate rolling the second die
    die2 = random.randint(1, NUM_SIDES)
    
    # Calculate the total of both dice
    total = die1 + die2
    
    # Display the results
    print("Dice have", NUM_SIDES, "sides each.")  # Show dice configuration
    print("First die:", die1)  # Result of first die
    print("Second die:", die2)  # Result of second die
    print("Total of two dice:", total)  # Combined total
    
    # Alternative output using f-strings (Python 3.6+ preferred style):
    # print(f"Dice have {NUM_SIDES} sides each.")
    # print(f"First die: {die1}")
    # print(f"Second die: {die2}")
    # print(f"Total of two dice: {total}")

# Standard Python idiom to check if running directly
# This prevents execution when imported as a module
if __name__ == '__main__':
    # Execute the main program
    main()