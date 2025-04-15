# Importing the random module so we can generate random numbers
import random

# These constants define how many numbers we want and the range of those numbers
N_NUMBERS: int = 10      # Total number of random numbers we want to print
MIN_VALUE: int = 1       # The smallest possible random number
MAX_VALUE: int = 100     # The largest possible random number

def main():
    # We use a loop to generate and print 10 random numbers
    for _ in range(N_NUMBERS):  # This loop runs 10 times
        # Generate a random integer between MIN_VALUE and MAX_VALUE (inclusive)
        random_number = random.randint(MIN_VALUE, MAX_VALUE)
        
        # Print the random number to the screen
        print(random_number)

# This makes sure the main function runs when we execute the program
if __name__ == '__main__':
    main()
