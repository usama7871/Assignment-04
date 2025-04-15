# Define the main function where the main code will run
def main():
    # We want to print the first 20 even numbers.
    # Even numbers are numbers that can be divided by 2 with no remainder (e.g., 0, 2, 4, 6...).
    # We'll use a for loop to repeat an action 20 times.

    # range(20) creates a sequence of numbers from 0 to 19 (total 20 numbers).
    for i in range(20):
        # Multiply the current number by 2 to get the corresponding even number.
        # For example: 0*2 = 0, 1*2 = 2, 2*2 = 4, ..., 19*2 = 38
        print(i * 2)  # Print the even number on each line

# This line checks if this file is being run directly (not imported somewhere else)
# If it is, then call the main() function to start the program.
if __name__ == '__main__':
    main()
