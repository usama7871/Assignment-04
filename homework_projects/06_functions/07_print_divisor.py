def print_divisors(num: int):
    """
    This function takes an integer 'num' and prints all of its divisors.
    A divisor is a number that divides 'num' evenly (without a remainder).
    """
    print(f"Here are the divisors of {num}")
    # Loop over numbers from 1 to num (inclusive)
    for i in range(1, num + 1):
        if num % i == 0:  # If the remainder when dividing num by i is 0, i is a divisor
            print(i)

def main():
    num = int(input("Enter a number: "))  # Take input from the user
    print_divisors(num)  # Call the print_divisors function

# This line ensures that the main function runs when the script is executed.
if __name__ == '__main__':
    main()
