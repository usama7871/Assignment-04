# Define the main function where our program logic will go
def main():
    # Ask the user to enter a year
    # We use int() to convert the input (which is a string) to an integer
    year = int(input('Please input a year: '))

    # ----------------------
    # According to the Gregorian calendar:
    # A year is a leap year if:
    # 1. It is divisible by 4
    #    BUT if it is divisible by 100, it must also be divisible by 400
    # Let's check that step by step

    if year % 4 == 0:
        # If the year is divisible by 4, it might be a leap year

        if year % 100 == 0:
            # If it is also divisible by 100, it is usually NOT a leap year

            if year % 400 == 0:
                # EXCEPTION: If the year is divisible by 400, then it IS a leap year
                print("That's a leap year!")
            else:
                # If divisible by 100 but NOT divisible by 400, then it's NOT a leap year
                print("That's not a leap year.")
        else:
            # If it's divisible by 4 but NOT divisible by 100, then it IS a leap year
            print("That's a leap year!")
    else:
        # If it's NOT divisible by 4, then it's definitely NOT a leap year
        print("That's not a leap year.")

# -------------------------------------------
# This ensures that the main() function runs when this script is executed directly
if __name__ == '__main__':
    main()
