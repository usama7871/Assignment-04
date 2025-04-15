import random

# This constant controls the likelihood of the done() function returning True
DONE_LIKELIHOOD = 0.3  # For example, there's a 30% chance to stop early

def chaotic_counting():
    for i in range(10):
        curr_num = i + 1  # Count from 1 to 10
        if done():  # Check if we should stop early
            return  # Stop the function and exit
        print(curr_num)  # Print the current number

def done():
    """ Returns True with a probability of DONE_LIKELIHOOD """
    return random.random() < DONE_LIKELIHOOD  # Randomly returns True with the likelihood

def main():
    print("I'm going to count until 10 or until I feel like stopping, whichever comes first.")
    chaotic_counting()  # Start counting
    print("I'm done")  # Print once counting is finished

if __name__ == "__main__":
    main()  # Run the program
