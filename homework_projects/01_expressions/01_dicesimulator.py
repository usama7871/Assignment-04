"""
Dice Rolling Simulator with Scope Demonstration
----------------------------------------------
This program simulates rolling two dice three times and prints the results.
It also demonstrates how variable scope works in Python by showing that
variables with the same name in different functions don't interfere with each other.

Key Concepts:
- Random number generation
- Function definitions
- Variable scope
- Printing formatted output
"""

# Import the random module to generate random numbers for dice rolls
import random

# Constant defining the number of sides on each die
# Standard dice have 6 sides, numbered 1 through 6
NUM_SIDES = 6

def roll_dice():
    """
    Simulates rolling two dice and displays the results.
    
    This function:
    1. Generates two random numbers between 1 and NUM_SIDES
    2. Calculates their sum
    3. Prints the individual dice values and the total
    
    Note: The die1 and die2 variables here are local to this function
    and don't affect variables with the same names in other functions.
    """
    
    # Generate random numbers for each die (between 1 and NUM_SIDES)
    die1 = random.randint(1, NUM_SIDES)  # First die roll
    die2 = random.randint(1, NUM_SIDES)  # Second die roll
    
    # Calculate the total of both dice
    total = die1 + die2
    
    # Print the results using an f-string for clean formatting
    print(f"Rolled: {die1} and {die2} (Total: {total})")

def main():
    """
    Main function that coordinates the program execution.
    
    This function:
    1. Demonstrates variable scope by creating a die1 variable
    2. Shows that calling roll_dice() doesn't affect this variable
    3. Calls roll_dice() three times to simulate multiple rolls
    """
    
    # Create a variable in main()'s scope to demonstrate it won't be affected
    # by the die1 variable in roll_dice()
    die1 = 10  # This variable is local to main() only 
    
    
    # Show the initial value of die1 in main()
    print(f"Before rolling, die1 in main(): {die1}")
    
    # Roll the dice three times by calling roll_dice() in a loop
    print("\nRolling the dice three times:")
    for roll_number in range(3):
        print(f"Roll {roll_number + 1}: ", end="")
        roll_dice()  # Call the dice rolling function
    
    # Show that die1 in main() wasn't affected by the roll_dice() calls
    print(f"\nAfter rolling, die1 in main(): {die1}")
    print("Note: die1 in main() stayed the same, proving it's a different variable!")

# This special condition checks if the script is being run directly
# (as opposed to being imported as a module)
if __name__ == '__main__':
    # If run directly, call the main() function to start the program
    main()