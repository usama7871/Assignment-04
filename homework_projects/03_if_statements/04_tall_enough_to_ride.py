# This constant stores the minimum height required to go on the ride
# You can think of it as a rule set by the amusement park for safety
MINIMUM_HEIGHT: int = 50  # You can use any unit (like inches, cm, etc.)

def main():
    # Ask the user for their height
    # We use float() here so the user can enter decimal numbers like 48.5
    height = float(input("How tall are you? "))

    # Check if the user's height is greater than or equal to the required minimum height
    if height >= MINIMUM_HEIGHT:
        # If yes, they are allowed to ride
        print("You're tall enough to ride!")
    else:
        # If not, they are too short for now but might grow in the future!
        print("You're not tall enough to ride, but maybe next year!")

# This line makes sure our main() function runs when we run the program
if __name__ == '__main__':
    main()
