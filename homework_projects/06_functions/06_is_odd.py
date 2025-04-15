def main():
    for i in range(10, 20):  # Loop from 10 to 19 inclusive
        if is_odd(i):  # Check if the number is odd
            print(f"{i} odd")  # Print if it's odd
        else:  # Otherwise, it's even
            print(f"{i} even")  # Print if it's even

def is_odd(value: int):
    """
    Checks to see if a value is odd. If it is, returns true.
    """
    remainder = value % 2  # 0 if value is divisible by 2, 1 if it isn't
    return remainder == 1  # Return True if the value is odd, else False

# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()
