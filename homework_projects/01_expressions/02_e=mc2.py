"""
Mass-Energy Equivalence Calculator
---------------------------------
This program calculates the energy equivalent of a given mass using Einstein's
famous equation E = mc², where:
- E is energy in joules
- m is mass in kilograms
- c is the speed of light (299,792,458 m/s)

The program demonstrates:
- Constant definitions
- User input handling
- Scientific calculations
- Formatted output
"""

# Define the speed of light as a constant
# This value never changes and is used in the E=mc² calculation
# Units: meters per second (m/s)
C = 299792458

def main():
    """
    Main function that handles the program workflow:
    1. Gets mass input from user
    2. Calculates energy equivalent
    3. Displays the calculation and result
    """
    
    # Get mass input from user and convert to float
    # float() handles both whole numbers and decimals
    mass_in_kg = float(input("Enter kilos of mass: "))
    
    # Calculate energy using E = mc²
    # C**2 means C raised to the power of 2 (C squared)
    energy_in_joules = mass_in_kg * (C ** 2)
    
    # Display the calculation steps and result
    print("\ne = m * C^2...")  # \n adds a blank line before output
    
    # Show the mass that was entered
    # str() converts numbers to strings for concatenation
    print("m = " + str(mass_in_kg) + " kg")
    
    # Show the constant speed of light
    print("C = " + str(C) + " m/s")
    
    # Display the final calculated energy
    # Scientific notation is used automatically for large numbers
    print("\n" + str(energy_in_joules) + " joules of energy!")

# This standard Python idiom checks if the script is being run directly
# (as opposed to being imported as a module)
if __name__ == '__main__':
    # If run directly, execute the main function
    main()