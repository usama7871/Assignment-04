def print_ones_digit(num):
    # The ones digit of num is obtained by taking num modulo 10
    print("The ones digit is", num % 10)

def main():
    # Get user input and convert it to an integer
    num = int(input("Enter a number: "))
    # Call the function to print the ones digit
    print_ones_digit(num)

# This line ensures that main() is called when the script is executed
if __name__ == '__main__':
    main()
