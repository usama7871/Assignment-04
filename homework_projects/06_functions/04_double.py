def double(num: int):
    # Multiply the input number by 2 and return the result
    return num * 2

# This provided line is required at the end of the Python file to call the main() function.
def main():
    # Prompt the user to enter a number
    num = int(input("Enter a number: "))
    
    # Call the double function and store the result
    num_times_2 = double(num)
    
    # Print the result
    print("Double that is", num_times_2)

if __name__ == '__main__':
    main()
